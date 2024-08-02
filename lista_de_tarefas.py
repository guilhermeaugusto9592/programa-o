# Criar lista
lista_de_tarefas = []

# Menu de escolha
def menu():
    print('''
          
          
██╗░░░░░██╗░██████╗████████╗░█████╗░  ██████╗░███████╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░
███████╗██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝

████████╗░█████╗░██████╗░███████╗███████╗░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
░░░██║░░░███████║██████╔╝█████╗░░█████╗░░███████║╚█████╗░
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══╝░░██╔══██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░
          
          ''')
    print('''𝟙 - 𝔸𝕕𝕚𝕔𝕚𝕠𝕟𝕒𝕣 𝕥𝕒𝕣𝕖𝕗𝕒𝕤''')
    print('''𝟚 - 𝕍𝕚𝕤𝕦𝕒𝕝𝕚𝕫𝕒𝕣 𝕥𝕒𝕣𝕖𝕗𝕒𝕤''')
    print('''𝟛 - ℝ𝕖𝕞𝕠𝕧𝕖𝕣 𝕥𝕒𝕣𝕖𝕗𝕒𝕤''')
    print('''𝟜 - 𝕊𝕒𝕚𝕣
          ''')

# Adicionar Tarefas
def adicionar_tarefa():
    tarefa = input('\nDigite a tarefa que deseja incluir: ')
    lista_de_tarefas.append(tarefa)
    print(f'\nTarefa {tarefa} incluída com sucesso!')

# Visualizar tarefas
def visualizar_tarefas():
    if lista_de_tarefas == []:
        print('\nNão há tarefas na lista')
    else:
        for tarefa in lista_de_tarefas:
            print(f'\n{lista_de_tarefas.index(tarefa) + 1} - {tarefa}') # 1 - Limpar a casa

# Remover tarefas
def remover_tarefa():
    visualizar_tarefas()
    if lista_de_tarefas == []:
        main()
    else:
        retirar = int(input('\nDigite o numero da tarefa que deseja retirar: ')) - 1
        print(f'\nA tarefa {lista_de_tarefas[retirar]} foi retirada com sucesso!')
        lista_de_tarefas.pop(retirar)

# Opção de escolha
def main():
    while True:
        try:
            menu()
            opcao = int(input('\nDigite o numero da opção desejada: '))

            if opcao == 1:
                print('Adicionar tarefa')
                adicionar_tarefa()
            
            elif opcao == 2:
                print('Visualizar tarefa')
                visualizar_tarefas()
            elif opcao == 3:
                print('Remover tarefa')
                remover_tarefa()
            elif opcao == 4:
                print('sair')
                break
            else:
                print('Opçao invalida')
        except:
            print('Digite uma opção valida!')

main()