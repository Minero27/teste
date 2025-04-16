compras = []
while True:
    print("===== LISTA DE COMPRAS =====")
    print("1 - Para adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Ver marca do item")
    print("5 - Editar pedido")
    print("6 - Limpar lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in compras:
            compras.remove(item)
            print(f'"{item}" foi removido.')
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        print("\nSua lista de compras:")
        print(compras)

    elif opcao == "4":
        item = input("Digite o nome do item: ")
        if item in compras:
            print(f"O item '{item}' está na posição {compras.index(item)}.")
        else:
            print("Item não encontrado.")
    elif opcao == "5":
        item = input("Digite o item para contar: ")
        qtd = compras.count(item)
        print(f"O item '{item}' aparece {qtd} vezes na lista.")

    elif opcao == "6":
        compras.clear()
        print("Lista de compras esvaziada!")

    elif opcao == "0":
        print("Saindo... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
