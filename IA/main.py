from groq import Groq
client = Groq(
    api_key= "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"
)
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
