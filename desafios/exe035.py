# Projeto: VemPython/exe035
# Autor: rafael
# Data: 15/03/18 - 15:16
# Objetivo: TODO Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triangulo

print('DE DOER ESSE TRIANGULO\n')

a = float(input('Informe a primeira Reta: '))
b = float(input('Informe a segunda Reta: '))
c = float(input('Informe a terceira Reta: '))

if b-c < a < b+c:
    la = 1
else:
    la = 0

if a-c < b < a+c:
    lb = 1
else:
    lb = 0

if a-b < c < a+b:
    lc = 1
else:
    lc = 0

if la+lb+lc == 3:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')
