lista = ['preto', 'branco', 'vermelho', 'azul']
print('Digite uma cor para remover da lista:')
cor = str(input())
if cor in lista:
    lista.remove(cor)
print(lista)