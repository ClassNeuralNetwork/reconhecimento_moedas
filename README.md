# Sistema de Reconhecimento e Contagem de Moedas

---
#### Projeto da Disciplina PET1706 - TÓPICOS ESPECIAIS EM ENGENHARIA DE SOFTWARE (Redes Neurais Artificiais) - 2023.2 
###### Professora: [Rosana Rego](https://github.com/roscibely)
<div>
  <img src="https://raw.githubusercontent.com/roscibely/algorithms-and-data-structure/main/root/ufersa.jpg" width="700" height="250">
</div>
<i> <a href="https://engsoftwarepaudosferros.ufersa.edu.br/apresentacao/"> Curso Bacharel em Engenharia de Software  </a> - UFERSA - Campus Pau dos Ferros </a></i>

---

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
git clone https://github.com/ClassNeuralNetwork/Reconhecimento_de_Moedas.git
```

2. Navegue até o diretório do projeto:

```bash
cd Reconhecimento_de_Moedas
```

3. Instale as dependências usando pip:

```bash
pip install -r requirements.txt
```

## Uso

1. Execute o script principal do sistema:

```bash
python main.py
```

2. Carregue uma imagem contendo moedas que deseja analisar.

3. Aguarde o processamento. O sistema identificará as moedas presentes na imagem e exibirá os resultados.

4. Você também pode explorar outras funcionalidades disponíveis na interface, como visualizar as regiões de interesse identificadas nas moedas.

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, por favor, abra uma issue para discutir as mudanças propostas ou envie um pull request.
## Equipe
<table align="center">
  <tr>    
    <td align="center">
      <a href="https://github.com/brunowellington">
        <img src="https://avatars.githubusercontent.com/u/83995825?v=4" 
        width="120px;"  alt="Foto de Bruno Wellington no GitHub"/><br>
        <sub>
          <b>Bruno Wellington</b>
         </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/EricSantosdm">
        <img src="https://avatars.githubusercontent.com/u/33100571?v=4" 
        width="120px;" alt="Foto de Eric Santos no GitHub"/><br>
        <sub>
          <b>Eric Santos</b>
         </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/DanielFernandess">
        <img src="https://avatars.githubusercontent.com/u/80116546?v=4" 
        width="120px;" alt="Foto de Daniel Fernandes no GitHub"/><br>
        <sub>
          <b>Daniel Fernandes</b>
         </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/wellespaiva-dev">
        <img src="https://avatars.githubusercontent.com/u/69151464?v=4" 
        width="120px;" alt="Foto de Welles Paiva no GitHub"/><br>
        <sub>
          <b>Welles Paiva</b>
         </sub>
      </a>
    </td>
  </tr>
</table>

<p align="center">
Cada contribuidor desempenhou um papel essencial no desenvolvimento e aprimoramento deste projeto.
</p>



## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Consulte o arquivo `LICENSE` para obter mais detalhes.

## Agradecimentos

Agradecemos aos desenvolvedores e à comunidade de código aberto que contribuíram com ferramentas como OpenCV e scikit-learn, que tornaram possível o desenvolvimento deste sistema de identificação de moedas.
