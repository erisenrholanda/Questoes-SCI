#  2 -  Solicitar 5 números, ao fim, imprimir o número maior e o número menor.
lista = []
maior = 0
menor = 0

for i in range(5):
    lista.append(int(input('informe um numero: ')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(f'o maior valor digitado foi {maior}')
print(f'o menor valor digitado foi {menor}')
