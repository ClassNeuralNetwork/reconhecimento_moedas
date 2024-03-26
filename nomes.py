import os

def rename_photos(directory, prefix):
    # Listar todos os arquivos no diretório
    files = os.listdir(directory)
    
    # Contador para numerar as fotos
    count = 1
    
    # Iterar sobre cada arquivo
    for file in files:
        # Verificar se é um arquivo de imagem (pode ser necessário adicionar mais extensões)
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Novo nome para o arquivo
            new_name = f"{prefix}_{count:02}.jpg"  # Formata o contador para ter dois dígitos
            
            # Caminho completo atual e novo caminho
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            
            # Renomear o arquivo
            os.rename(old_path, new_path)
            print(f"Renomeado {file} para {new_name}")
            
            # Incrementar o contador
            count += 1

# Diretório onde estão as fotos
directory = 'dataset/100'
# Prefixo para os novos nomes das fotos
prefix = 'Moeda_Real'

# Chamar a função para renomear as fotos
rename_photos(directory, prefix)
