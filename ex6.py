frutas = ['açai', 'banana', 'caju',  'damasco']
legumes = ['abobrinha', 'batata', 'cenoura', 'tomate']
print(frutas)
print(legumes)

print('Digite um nome do alimento:')
alimento = str(input())
if alimento in frutas:
    print('O alimento digitado é uma fruta')
elif alimento in legumes:
    print('O alimento digitado é um legume')
else:
    print('O alimento digitado não esta nas listas')
