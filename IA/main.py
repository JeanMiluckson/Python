import os
from dotenv import load_dotenv
from groq import Groq

# Carrega o arquivo .env
load_dotenv()

# Lê a variável de ambiente
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

print("chat ia com Groq iniciado!")
print("Digite 'Sair' para encerrar")

while True:
    user_input = input("Voce: ")

    if user_input .lower() == "sair":
        print("IA: Até mais")
        break

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Você é uma IA educada, clara e didática."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )
    resposta = response.choices[0].message.content
    print(f'IA: {resposta}\n')
