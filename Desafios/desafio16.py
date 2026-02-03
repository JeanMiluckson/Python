# Crie uma lista vazia chamada lista_tarefas = []
# Crie um loop while que pergunte ao usuario: "Digite uma tarefa (ou 'sair' para finalizar):"
# Se o usuario digitar 'sair', o loop deve parar caso contrario, adicione o que digitou na lista

lista_tarefas= []

while True:
   tarefa = input("Digite uma tarefa (ou 'sair' para finalizar): ")
   if tarefa == "sair":
      print("saindo...")
      break 
   else:
      lista_tarefas.append(tarefa)
for t in lista_tarefas:
   print(f"- {t}")
