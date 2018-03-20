# Projeto: VemPython/exe051
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
# termos dessa progressão

a = int(input('Informe o 1º Termo da PA: '))
r = int(input('Informe a Razão da PA: '))

for n in range(1, 11):
    an = a + (n - 1) * r
    print('{}'.format(an))
