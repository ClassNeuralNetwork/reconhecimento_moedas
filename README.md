# Sistema de Reconhecimento e Contagem de Moedas com OpenCV

Este é um sistema de identificação de moedas desenvolvido em Python utilizando OpenCV. O sistema utiliza técnicas de Processamento de Imagem e Machine Learning para identificar diferentes tipos de moedas em uma imagem.

## Funcionalidades Principais

- **Identificação de Moedas**: O sistema é capaz de analisar imagens contendo moedas e identificar os tipos de moedas presentes, como moedas de 1 real, 50 centavos, etc.

- **Processamento de Imagem**: Utilizando OpenCV, o sistema realiza o pré-processamento das imagens, destacando características únicas das moedas para facilitar a identificação.

- **Modelo de Machine Learning**: O sistema utiliza um modelo de Machine Learning treinado previamente para reconhecimento de moedas. Este modelo foi treinado com uma variedade de imagens de diferentes tipos de moedas.

## Requisitos de Sistema

- Python 3.x
- OpenCV
- Bibliotecas Python: NumPy, scikit-learn, etc. (detalhes podem ser encontrados no arquivo requirements.txt)

## Instalação

1. Clone o repositório do GitHub:

```bash
git clone https://github.com/brunowellington/ContadorDeMoedasBrasileirasComOpenCV.git
```

2. Navegue até o diretório do projeto:

```bash
cd ContadorDeMoedasBrasileirasComOpenCV
```

3. Instale antes um ambiente virtual e inicie, depois instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute o script principal do sistema para criar as pastas de treino e validção a partir do dataset:

```bash
python main.py
```

2. Treine o modelo a partir do arquivo 'main.ipynb'

Caso queira analisar diretamente do modelo, faça:

2.1. Carregue uma imagem contendo moedas que deseja analisar.

2.2. Aguarde o processamento. O sistema identificará as moedas presentes na imagem e exibirá os resultados.

3. Caso queira testar usando o openCv execute o script

```bash
python reconhecimento&contagem.py
```

4. Caso queira executar pelo StreamLit execute o script no caminho APP

```bash
streamlit run Appstreamlit.py
```

5. Você também pode explorar outras funcionalidades disponíveis na interface, como visualizar as regiões de interesse identificadas nas moedas.

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, por favor, abra uma issue para discutir as mudanças propostas ou envie um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Consulte o arquivo `LICENSE` para obter mais detalhes.

## Agradecimentos

Agradecemos aos desenvolvedores e à comunidade de código aberto que contribuíram com ferramentas como OpenCV e scikit-learn, que tornaram possível o desenvolvimento deste sistema de identificação de moedas.
