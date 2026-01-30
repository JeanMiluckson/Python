# Use o codigo que voce ja escreveu no desafio13.py
# Adicione uma estrutura if / else
# A condicao: - Se o prazo for menor ou igual a 3 dias, exiba: "Atencao! [Titulo] precisa de prioridade máxima!" caso contrario(se for mais de 3 dias), exiba: "O prazo para [Titulo] esta confortavel"

titulo = input("Digite o Titulo de sua tarefa: ")
prazo = int(input("Digite o Prazo de sua tarefa: "))

if prazo <= 3:
    print(f"Atencao {titulo} precisa de prioridade maxima")
else:
    print(f"O prazo para {titulo} esta confortavel")


