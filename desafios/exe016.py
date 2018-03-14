# Projeto: VemPython/exe016
# Autor: rafael
# Data: 14/03/18 - 11:19
# Objetivo: TODO Crie um programa que leia um numero Real qualquer e mostre na tela a sua porção inteira
# Ex: Digite um Numero: _6.127
# O numero 6.127 tem 6 na sua parte inteira

import math

num = float(input('Informe um numero real [Ex.: 6.127]: '))
print('O numero {} tem {} na sua parte inteira.'.format(num, math.trunc(num)))

# print('O numero {} tem {} na sua parte inteira.'.format(num, int(num)))
# print('O numero {} tem {:.0f} na sua parte inteira.'.format(num, num))
