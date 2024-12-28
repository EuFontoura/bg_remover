# Removedor de Fundo (Background Remover)

  <p align="center">
    <a href="#projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#como-usar">Como Usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#dependências">Dependências</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#atualizações-futuras">Atualizações Futuras</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#contribuição">Contribuição</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#licença">Licença</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000" />
  </p>

## Projeto
Este é um projeto em Python para remover o fundo de imagens automaticamente, usando a biblioteca rembg. Ele oferece uma interface gráfica simples para selecionar a imagem e o local para salvar a versão sem fundo.

## Instalação
#### 1. Clone o repositório:
```bash
git clone https://github.com/EuFontoura/bg_remover.git
cd bg_remover 
```

#### 2. Instale as dependências:

As dependências do projeto estão listadas no arquivo requirements.txt. Para instalá-las, basta rodar o seguinte comando:

```bash
pip install -r requirements.txt
```
Isso instalará todas as bibliotecas necessárias, incluindo rembg e onnxruntime.

## Como Usar
#### Executando o script:

Para usar o removedor de fundo, basta rodar o script Python. Ele abrirá uma janela para você selecionar a imagem de entrada e o local para salvar a imagem sem fundo.

```bash
python bgRemover.py
```
#### Passos Interativos:
O script é totalmente interativo. Ele guiará você pelas seguintes etapas:

- Escolher a imagem de entrada.
- Selecionar onde salvar a imagem sem fundo.
- Aguardar o processamento (isso pode levar alguns segundos).
- Aguardar uma mensagem de sucesso quando o processo for concluído.

##  Dependências
**rembg**: Para remover o fundo das imagens.
**Pillow**: Para manipulação e salvamento das imagens.
**onnxruntime**: Executa modelos de aprendizado de máquina utilizados nesse projeto.

## Atualizações Futuras
1. **Transformação em Executável (Sem Necessidade de Python)**
O objetivo é tornar o uso do projeto ainda mais simples, especialmente para aqueles que não têm experiência com programação. Estou trabalhando para converter o script Python em um executável. Isso significa que, no futuro, os usuários poderão simplesmente baixar e executar um arquivo (como um .exe no Windows ou um .app no macOS), sem precisar instalar o Python ou as dependências manualmente. Isso vai permitir um processo de uso mais direto e amigável.
&nbsp;
2. **Melhoria na Interface Gráfica (GUI)**
A interface atual é simples, mas estamos planejando uma versão com uma interface gráfica (GUI) mais robusta. A ideia é adicionar opções intuitivas, como:

    - Arrastar e soltar imagens para o aplicativo.
    - Exibir pré-visualizações da imagem com o fundo removido.
    &nbsp;
3. **Otimização e Suporte a Novos Modelos**
Estou planejando melhorias no desempenho do modelo de remoção de fundo, incluindo a integração de novos algoritmos de IA que podem oferecer resultados ainda mais rápidos e precisos, além de suportar diferentes tipos de imagens e fundos.

## Contribuição

- Faça um fork do repositório.
- Crie uma nova branch: git checkout -b minha-feature.
- Faça as alterações necessárias e adicione ao commit: git commit -am 'Adiciona minha feature'.
- Envie para o repositório remoto: git push origin minha-feature.
- Abra um pull request.

## Contribuidores

- Gabriel Fontoura

## Licença
Este projeto está licenciado sob a licença [MIT](https://github.com/EuFontoura/bg_remover/blob/main/LICENSE).