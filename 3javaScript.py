# 3- Elabore um programa de computador que realize o cálculo de notas. Este programa deverá solicitar o nome do aluno e quatro notas, todo este conjunto deverá estar contido em um laço que confirme se deseja encerrar o programa ou continuar solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e a sua média, se a nota for  menor que 6 imprimir Reprovado, senão, se a nota for igual ou maior que 6, imprimir Aprovado.

res = True
notas = []
while res:
    nome = str((input('informe seu nome: ')))
    for i in range(4):
        notas.append(int(input('informe suas notas: ')))
        print(notas)
    media = sum(notas) / 4
    if media >= 6:
        print(f'nome: {nome} media: {media} condição: Aprovado')
    else:
        print(f'nome: {nome}, media: {media}, condição: Reprovado')
    res = input('Quer continuar? [s/n] ')
    if res == 's' | res == 'sim':
        notas = []
        res = True
    else:
        res = False
