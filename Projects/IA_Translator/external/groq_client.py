from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def traduzir_para_frances(texto):
    system_prompt = """
Você é um tradutor profissional.

Regras obrigatórias:
- Sempre responda APENAS com a tradução em francês.
- Nunca responda como uma conversa.
- Nunca explique nada.
- Se o texto já estiver em francês, retorne o texto original.
- Se o texto estiver em português ou outro idioma, traduza para francês.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": texto}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
