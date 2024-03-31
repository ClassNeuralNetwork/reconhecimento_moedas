import cv2
import numpy as np
from keras.models import load_model

# Dicionário de valores das moedas
coin_values = {
    "1 real": 1.00,
    "50 centavos": 0.50,
    "25 centavos": 0.25,
    "10 centavos": 0.10,
    "5 centavos": 0.05
}

# Função para detecção e contagem de moedas em um frame de vídeo
def detect_and_count_coins(frame, coin_classifier):
    # Conversão para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicação de um filtro de suavização
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    
    # Detecção de bordas
    edges = cv2.Canny(blurred, 30, 150)
    
    # Dilatação e erosão para fechar lacunas nos contornos
    kernel = np.ones((3,3), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    # Detecção de contornos
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Contador de moedas
    coins_count = {}
    
    # Iteração sobre os contornos encontrados
    for contour in contours:
        area = cv2.contourArea(contour)
        if 1000 < area < 500000:  # Ajuste os valores de área conforme necessário para filtrar os contornos
            # Recorta a região da moeda
            x, y, w, h = cv2.boundingRect(contour)
            coin_roi = frame[y:y+h, x:x+w]
            
            # Classificação da moeda
            coin_class = classify_coin(coin_roi, coin_classifier)
            
            # Atualiza o contador de moedas
            coins_count[coin_class] = coins_count.get(coin_class, 0) + 1
            
            # Desenha o contorno da moeda no frame original
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, coin_class, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return frame, coins_count

# Função para classificar uma moeda usando um modelo de classificação
def classify_coin(coin_roi, coin_classifier):
    # Redimensiona a região da moeda para o tamanho esperado pelo modelo
    coin_roi_resized = cv2.resize(coin_roi, (64, 64))
    
    # Pré-processamento da imagem conforme necessário pelo modelo
    coin_roi_preprocessed = coin_roi_resized / 255  # Normalização
    
    # Adapta a entrada do modelo para corresponder ao formato esperado pelo modelo
    coin_roi_input = np.expand_dims(coin_roi_preprocessed, axis=0)
    
    # Realiza a classificação usando o modelo
    predictions = coin_classifier.predict(coin_roi_input)
    
    # Obtém a classe prevista (índice do valor máximo da saída do modelo)
    predicted_class_index = np.argmax(predictions)
    
    # Mapeia o índice da classe prevista para a classe real
    coin_classes = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]
    predicted_coin_class = coin_classes[predicted_class_index]
    
    return predicted_coin_class

# Carrega o modelo de classificação treinado
coin_classifier = load_model("reconhecimento_moedas/modelo/mode_acurracy89.h5")

# Captura de vídeo da webcam
video_capture = cv2.VideoCapture(1)

while True:
    # Captura um frame do vídeo
    ret, frame = video_capture.read()
    if not ret:
        break
    
    # Realiza a detecção e contagem de moedas no frame
    frame_with_coins, coins_count = detect_and_count_coins(frame, coin_classifier)
    
    # Calcula o valor total das moedas detectadas
    total_value = 0
    for coin_class, count in coins_count.items():
        total_value += coin_values[coin_class] * count
    
    # Exibe o valor total das moedas
    cv2.putText(frame_with_coins, f"Total: R$ {total_value:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Exibe o frame com as moedas detectadas e classificadas
    cv2.imshow('Video', frame_with_coins)
    
    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
video_capture.release()
cv2.destroyAllWindows()
