itens = []
opcoes_validas = ('a', 'b', 'c', 'd', 'sair')

def menu():
    while True:

        print('Opção disponíveis: ', "\n")
        print(' Lista; (A) ')
        print(' Incluir na lista; (B) ')
        print(' Remover da lista; (C) ')
        print(' Apagar da lista; (D) ', "\n")
        print(' Sair; (sair) ', "\n")

        opcao = input(f"Qual opção? ").lower()

        if opcao not in opcoes_validas:
            print('Opção não disponível, tente novamente.')
        else:
            return opcao
            break

def lista():
    print("Adicionado: ", "\n")
    print("\n".join(itens))

def remover():
    while True:
        data = input(f"Item para deletar: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            if data in itens:
                itens.remove(data)
                print("Removido")
            else:
                print("Item não existe")

            break

def limpar():
    itens.clear()
    print("lista apagada")

def adicionar():
    while True:
        data = input(f"item para adicionar: ")

        if not data:
            print(f"O valor informado é inválido")
        else:
            itens.append(data)
            print("Adicionado")
            break


while True:
    opcao = menu()
    if opcao == 'sair':
        break
    elif opcao == 'a':
        lista()
    elif opcao == 'b':
        adicionar()
    elif opcao == 'c':
        remover()
    elif opcao == 'd':
        limpar()