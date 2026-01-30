# Crie uma lista chamada [lista_tarefas] que já comece com duas tarefas de sua escolha
# Peça para o usuario digitar uma nova tarefa via input()
# Adicione essa nova tarefa a lista usando o .append()
# No final exiba a lista completa para o usuario ver como ela ficou
# Mantenha sua lista_tarefas (com as que você já tem e a nova que o usuário digitar).

# Use um laço for para percorrer essa lista.
# Dentro do laço, imprima cada tarefa com um prefixo, por exemplo: [ ] - Nome da Tarefa.
# No final do programa (fora do laço), imprima uma mensagem dizendo: "Total de tarefas: X", onde X é a quantidade de itens na lista.


lista_tarefas = ["C#", "C++", "C"]
lista_tarefas.append(input("Digite sua nova tarefa: "))


for t in lista_tarefas:
    print(f"[] {t}")

X=len(lista_tarefas)
print(f"Total de tarefas: {X}")