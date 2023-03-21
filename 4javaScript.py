#  4- Criar um vetor de cinco posições, solicitar  cinco números e ao fim, imprimir o valor apresentado na posição três.
lista = []
for i in range(5):
    lista.append(int(input('informe um numero: ')))
print(lista[2])
