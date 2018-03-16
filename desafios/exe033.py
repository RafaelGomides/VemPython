# Projeto: VemPython/exe033
# Autor: rafael
# Data: 15/03/18 - 15:14
# Objetivo: TODO Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor

n1 = float(input('Informe o 1º Número: '))
n2 = float(input('Informe o 2º Número: '))
n3 = float(input('Informe o 3º Número: '))

if n1 > n2 and n1 > n3:
    print('O Maior número é: {}'.format(n1))
elif n1 < n2 and n1 < n3:
    print('O Menor numero é: {}'.format(n1))

if n2 > n3 and n2 > n1:
    print('O Maior numero é: {}'.format(n2))
elif n2 < n3 and n2 < n3:
    print('O Menor número é: {}'.format(n2))

if n3 > n2 and n3 > n2:
    print('O Maior numero é: {}'.format(n3))
elif n3 < n2 and n3 < n1:
    print('O Menor número é: {}'.format(n3))
