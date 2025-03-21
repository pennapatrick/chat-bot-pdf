# Chat-Bot com OpenAI e PDFs

Este projeto implementa um chatbot simples que usa a API da OpenAI para responder perguntas com base em informações extraídas de arquivos PDF. Os PDFs são armazenados na pasta inputs/, e o chatbot processa o conteúdo desses documentos para gerar respostas relevantes.

## Estrutura do Projeto

- **inputs/**: Pasta onde você deve colocar os arquivos PDF que servirão como fontes de informações para o chatbot.
- **main.py**: Script Python que contém o código do chatbot. Ele lê os PDFs e interage com o usuário.
- **requirements.txt**: Arquivo contendo as dependências do projeto.
- **README.md**: Este arquivo, que fornece informações sobre o projeto.

## Como Usar

### Passo 1: Instalar as dependências

Este projeto utiliza as bibliotecas openai, PyPDF2 e python-dotenv. Para instalar as dependências, execute o seguinte comando:

``` pip install -r requirements.txt```

### Passo 2: Configurar a chave da API da OpenAI
Crie uma conta no OpenAI (se ainda não tiver uma).

Obtenha sua chave da API.

Crie um arquivo .env na raiz do projeto e adicione sua chave da API nele:

OPENAI_API_KEY=Sua_Chave_De_API_Aqui

### Passo 3: Adicionar arquivos PDF
Coloque seus arquivos PDF no diretório inputs/. O conteúdo desses arquivos será utilizado para gerar respostas do chatbot.

### Passo 4: Executar o chatbot
Após configurar tudo, execute o script Python main.py para iniciar o chatbot:


```python main.py```

O chatbot irá processar os PDFs e, em seguida, você poderá interagir com ele. Basta digitar suas perguntas, e o chatbot tentará fornecer respostas com base nas informações dos documentos.