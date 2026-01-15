from core.translator import traduzir
from core.detector import treinar_modelo
import os

# Treina o modelo se ainda não existir
if not os.path.exists("model/language_detector.pkl"):
    print("Treinando detector de idioma...")
    treinar_modelo()

print("Tradutor PT → FR com IA (Groq)")
print("Digite 'sair' para encerrar\n")

while True:
    texto = input("Texto: ")

    if texto.lower() == "sair":
        break

    resultado = traduzir(texto)
    print("Resultado:", resultado, "\n")
