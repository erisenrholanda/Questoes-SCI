#  1 - Solicitar a inserção de 5 números, ao final, imprimir os números pares, números ímpares e a média geral desses números.
pares = []
impares = []
lista = []
for i in range(5):
    num = int(input('informe um numero: '))
    lista.append(num)
    media_total = sum(lista)/5
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('pares: ', pares)
print('impares: ', impares)
print('lista: ', lista)
print('media: ', media_total)
