# Projeto: VemPython/exe054
# Autor: rafael
# Data: 16/03/18 - 17:35
# Objetivo: TODO Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda
# Não atingiram a maioridade e quantas já são maiores

from datetime import date

maior = 0
menor = 0

for i in range(0, 7):
    anoN = int(input('Informe o ano de nascimento: '))
    if (date.today().year-anoN) >= 21:
        maior += 1
    else:
        menor += 1

print('De 7 pessoas.\nExistem {} pessoas maiores e {} menores'.format(maior, menor))
