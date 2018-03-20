# Projeto: VemPython/exe052
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Faça um programa que leia um nmero inteiro e diga se ele é um numero primo

num = int(input('Informe um numero para saber se é primo: '))
i = 1
cp = 0

while i < num+1:
    if num % i == 0:
        cp += 1
        print('\033[32m{}\033[m'.format(i))
    else:
        print('\033[31m{}\033[m'.format(i))
    i += 1

if cp > 2:
    print('O número {} não é primo'.format(num))
else:
    print('O número {} é primo!'.format(num))
