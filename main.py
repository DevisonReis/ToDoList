lista_de_tarefas = []
tarefas_removidas = []

def adicionar_tarefa():
    tarefa = input('Digite uma nova tarefa: ')
    lista_de_tarefas.append(tarefa)

def mostrar_tarefas():
    if len(lista_de_tarefas) == 0:
        tarefa = input("""
        Você não possui nenhuma tarefa
        Vamos começar? [s/n] 
        """)
        if tarefa == 's':
            adicionar_tarefa()
        else:
            pass
    else:
        print(lista_de_tarefas)

def desfazer_tarefa():
    try:
        removida = lista_de_tarefas.pop()
        tarefas_removidas.append(removida)
        print(f'A tarefa {removida} foi desfeita.')
    except IndexError:
        print("""
        Todas as tarefas foram desfeitas.
        Refaça ou adicione uma nova tarefa.
        """)

def refazer_tarefa():
    try:
        refaz = tarefas_removidas.pop()
        lista_de_tarefas.append(refaz)
        print(f'A tarefa {refaz} foi refeita.')
    except IndexError:
        print('Nada para refazer.')

while True:
    menu = input("""
    ------------------------------------------------
    Bem vindo ao seu ToDo List
    ------------------------------------------------
    Escolha uma das opções abaixo
    ------------------------------------------------
    1 - Adicionar nova tarefa
    2 - Mostrar tarefas
    3 - Desfazer tarefa
    4 - Refazer tarefa
    5 - Sair
    """)

    if menu == '1':
        adicionar_tarefa()
    elif menu == '2':
        mostrar_tarefas()
    elif menu == '3':
        desfazer_tarefa()
    elif menu == '4':
        refazer_tarefa()
    elif menu == '5':
        break
