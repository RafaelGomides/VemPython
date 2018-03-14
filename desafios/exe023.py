# Projeto: VemPython/exe023
# Autor: rafael
# Data: 14/03/18 - 16:51
# Objetivo: TODO Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Exemplo: Digite um numero: _1834 >> Unidade: 4; Dezena: 3; Centena: 8; Milhar: 1

num = int(input('Informe um numero de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidades: {}\nDezenas: {}\nCentenas: {}\nMilhares: {}'.format(u, d, c, m))