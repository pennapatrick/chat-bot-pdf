import os
import PyPDF2
import openai
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env (se necessário)
load_dotenv()

# Defina sua chave da API do OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para ler PDFs e extrair texto
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

# Função para processar PDFs na pasta inputs/
def process_pdfs():
    pdf_texts = []
    pdf_folder = './inputs/'

    # Itera por todos os PDFs na pasta
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            pdf_text = extract_text_from_pdf(pdf_path)
            pdf_texts.append(pdf_text)
    
    return pdf_texts

# Função para buscar respostas usando a OpenAI API com base no conteúdo extraído dos PDFs
def get_openai_response(question, context):
    prompt = f"Pergunta: {question}\n\nContexto: {context}\n\nResposta:"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ou outro modelo disponível
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao buscar resposta: {str(e)}"

# Função principal do chatbot
def chat_bot():
    # Processa todos os PDFs
    pdf_texts = process_pdfs()
    
    # Junta todo o texto dos PDFs em um único contexto
    full_context = "\n".join(pdf_texts)
    
    print("ChatBot: Olá! Eu posso responder com base nos documentos PDF que tenho.")
    
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == "sair":
            print("ChatBot: Até logo!")
            break
        else:
            # Busca uma resposta usando o OpenAI com o conteúdo extraído dos PDFs
            print("ChatBot: Vou tentar encontrar informações sobre isso nos documentos...")
            answer = get_openai_response(user_input, full_context)
            print(f"ChatBot: {answer}")

if __name__ == "__main__":
    chat_bot()
