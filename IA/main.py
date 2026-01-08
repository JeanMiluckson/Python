import asyncio
import edge_tts
from groq import Groq
import os
import tempfile
import subprocess

client = Groq(api_key="api_key")

VOICE = "pt-BR-AntonioNeural"

async def falar_async(texto):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        audio_path = f.name

    communicate = edge_tts.Communicate(texto, voice=VOICE)
    await communicate.save(audio_path)

    subprocess.run(["mpg123", "-q", audio_path])
    os.remove(audio_path)


def falar(texto):
    asyncio.run(falar_async(texto))


def get_resposta(pergunta):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": pergunta}]
    )
    return response.choices[0].message.content


def main():
    print("🤖 Assistente com voz natural (edge-tts)")
    print("Digite 'sair' para encerrar.")

    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() == "sair":
            break

        resposta = get_resposta(pergunta)
        print("\nAssistente:", resposta)
        falar(resposta)


if __name__ == "__main__":
    main()