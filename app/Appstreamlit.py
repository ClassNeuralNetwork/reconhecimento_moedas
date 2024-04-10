import cv2
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, WebRtcMode
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

# Dicionário de valores das moedas
coin_values = {
    "1 real": 1.00,
    "50 centavos": 0.50,
    "25 centavos": 0.25,
    "10 centavos": 0.10,
    "5 centavos": 0.05
}

# Carregar o modelo treinado para reconhecimento de moedas

coin_classifier = load_model("reconhecimento_moedas/modelo/mode_acurracy89.h5")

class CoinRecognition(VideoTransformerBase):
    def __init__(self):
        self.frame_count = 0

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        coins_count = {"1 real": 0, "50 centavos": 0, "25 centavos": 0, "10 centavos": 0, "5 centavos": 0}

        # Converter imagem para escala de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Aplicar suavização para reduzir o ruído
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)

        # Detectar bordas na imagem
        edges = cv2.Canny(blurred, 30, 150)

        # Encontrar contornos na imagem
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterar sobre os contornos encontrados
        for contour in contours:
            area = cv2.contourArea(contour)
            if 1000 < area < 500000:  # Ajustar valores conforme necessário para filtrar contornos
                x, y, w, h = cv2.boundingRect(contour)
                coin_roi = img[y:y + h, x:x + w]

                # Classificar a moeda
                coin_class = classify_coin(coin_roi, coin_classifier)

                # Atualizar contador de moedas
                if coin_class in coins_count:
                    coins_count[coin_class] += 1

                # Desenhar contorno da moeda no frame original
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, coin_class, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        total_value = 0
    
        for coin, count in coins_count.items():
            total_value += count * coin_values[coin]
        
        # exibindo dinheiro total
        cv2.putText(img, f"Total: R$ {total_value:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return img

def classify_coin(coin_roi, coin_classifier):
    resized_image = cv2.resize(coin_roi, (64, 64))
    resized_image = resized_image.astype("float") / 255.0
    resized_image = img_to_array(resized_image)
    resized_image = np.expand_dims(resized_image, axis=0)

    # Faz a predição da moeda
    predictions = coin_classifier.predict(resized_image)[0]
    max_index = np.argmax(predictions)
    coin_classes = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]

    return coin_classes[max_index]

def main():
    st.write('<span style="font-size:40px;"><b>Reconhecimento e Contagem de Moedas Utilizando o OpenCV.</span>', unsafe_allow_html=True)
    activities = ["Início", "Reconhecimento de Moedas pelo CV2"]
    choice = st.sidebar.selectbox("Selecione", activities)
    if choice == "Início":
        st.write("**Projeto desenvolvido na disciplina de Redes Neurais - Curso Engenharia de Software - UFERSA - 2023.2**")

        st.write("Este é um sistema de identificação de moedas desenvolvido em Python utilizando OpenCV. O sistema utiliza técnicas de Processamento de Imagem e Machine Learning utilizando a arquitetura CNN para identificar diferentes tipos de moedas em uma imagem.")

        st.write("**Funcionalidades Principais:** <br>**Identificação de Moedas:** O sistema é capaz de analisar imagens contendo moedas e identificar os tipos de moedas presentes, como moedas de 1 real, 50 centavos, etc.<br> **Processamento de Imagem:** Utilizando OpenCV, o sistema realiza o pré-processamento das imagens, destacando características únicas das moedas para facilitar a identificação. <br>**Modelo de Machine Learning:** O sistema utiliza um modelo de Machine Learning treinado previamente para reconhecimento de moedas. Este modelo foi treinado com uma variedade de imagens de diferentes tipos de moedas.", unsafe_allow_html=True)

        st.write("**Equipe de Desenvolvimento:** Bruno Wellington, Eric Bezerra, Daniel Fernandes, Welles Paiva.")

    elif choice == "Reconhecimento de Moedas pelo CV2":
        st.header("Ativar câmera")
        st.write("Clique em 'Select Device' para selecionar a WebCam de sua preferência depois clique em selecionar 'Start' para ativar o reconhecimento de moedas")
        webrtc_streamer(key="coin-recognition", video_processor_factory=CoinRecognition)

    else:
        pass


if __name__ == "__main__":
    main()
