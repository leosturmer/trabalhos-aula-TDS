
### Visualizar agenda

def visualizar_agenda():
    print('''

-------------- Agenda de contatos --------------

''')
    if len(agenda_de_contatos) == 0:
        print('Nenhum contato cadastrado.')
    else:
        for chave, valor in agenda_de_contatos.items():
            print(f'Nome: {chave}, telefone: {valor}')

    voltar_ao_menu()        

### Adicionando contatos na agenda

def adicionar_contato():
    nome = input("Digite o nome do novo contato: ")
    telefone = input("Insira o telefone do novo contato: ")

    agenda_de_contatos.fromkeys([nome])
    agenda_de_contatos.update({nome : telefone})

    print(f'Contato {nome} adicionado com sucesso!')

    voltar_ao_menu()

### Remover contato da agenda

def remover_contato():
    contato_a_remover = input("Digite o nome do contato a ser removido: ")    

    if contato_a_remover in agenda_de_contatos:
        agenda_de_contatos.pop(contato_a_remover)
        print(f'{contato_a_remover} removido com sucesso!')
    else:
        print(f'{contato_a_remover} não cadastrado')

    voltar_ao_menu()

### Buscar contato na agenda

def busca_contato():
    contato_a_buscar = input("Digite o contato a ser buscado: ")

    if contato_a_buscar in agenda_de_contatos:
        print (f"Nome: {contato_a_buscar}. Telefone: {agenda_de_contatos[contato_a_buscar]}")
    else:
        print(f'{contato_a_buscar} não cadastrado')

    voltar_ao_menu()


#
# View 
#

def encerrar_programa():
    print('''
-------------- Programa encerrado --------------
          ''')

def menu_agenda():
    print('''
Menu de opções:
          
1 - Adicionar contato
2 - Remover contato
3 - Buscar contato          
4 - Visualizar agenda
5 - Encerrar programa          
''')

#
# Controller
#

def escolher_opcao():
    menu_agenda()

    opcao_escolhida = input("Digite a opção desejada: ")
    
    comandos = {
        '1' : adicionar_contato,
        '2' : remover_contato,
        '3' : busca_contato,
        '4' : visualizar_agenda,
        '5' : encerrar_programa
    }

    print(f'''
          
    Opção escolhida: {opcao_escolhida}

''')

    try:
        comandos[opcao_escolhida]() 
    except KeyError:
        print(f'Opção inválida! Voltando ao menu inicial.')
        escolher_opcao()
        

def voltar_ao_menu():
    print('''
--- Aperte enter para voltar ao menu inicial ---
          
------------------------------------------------
          ''')
    input()
    escolher_opcao()



########################### INÍCIO DO PROGRAMA ############################

### Criando a agenda

agenda_de_contatos = {}

escolher_opcao()
