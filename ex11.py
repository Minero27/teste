lista = []
while True:
    print('Digite 1 para adicionar um item')
    print('Digite 2 para ver a lista')
    print('Digite 3 para remover um item')
    print('Digite 4 para sair do programa')
    
    opcao = int(input('Escolha uma opção:'))

    if opcao == 1:
        item = str(input('Digite um item que deseja adicionar a lista:'))
        lista.append(item)
        print('O item foi adicionado a lista')
    elif opcao == 2:
        item = str(input('Digite um item que deseja ver na lista:'))
        if item in lista:
            print('O item está na lista')
        else:
            print('O item não está na lista')
    elif opcao == 3:
        item = str(input('Digite um item que deseja remover da lista:'))
        if item in lista:
            lista.remove(item)
            print('O item foi removido da lista')
        else:
            print('O item não esta na lista')
    elif opcao == 4:
     print('Saindo do programa')
    break