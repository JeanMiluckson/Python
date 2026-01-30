# Crie um script que peça para o usuário digitar o titulo de uma tarefa
# Peça para ele digitar o prazo em dias
# Exiba uma mensagem de confirmação no final usando, algo como: "Tarefa '[titulo]' registrada. voce tem [prazo] dias para concluir"

titulo = input("Digite o Titulo de sua tarefa: ")
prazo = int(input("Digite o Prazo da tarefa: "))

print(f'Tarefa {titulo} registrada. voce tem {prazo} dias para concluir-la')