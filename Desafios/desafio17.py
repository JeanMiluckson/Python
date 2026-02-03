# Crie uma funcao chamada exibir_lista que receba uma lista como parametro e use o for para imprimi-la
# No seu codigo principal(dentro do while) continue adicionando as tarefas
# Quando o usuario digitar 'sair', em vez de apenas dar break, chame a sua funcao exibir_lista(lista_tarefas) para mostrar o resultado final

lista_tarefas = []

def exibir_lista(lista_tarefas):
    for t in lista_tarefas:
        print(f"- {t}")

while True:
    tarefas = input("Digite uma tarefa (ou 'sair' para finalizar): ")
    if tarefas == "sair":
        print("Saindo...")
        exibir_lista(lista_tarefas)
        break
    else:
        lista_tarefas.append(tarefas)
