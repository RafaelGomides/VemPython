# Projeto: VemPython/exe018
# Autor: rafael
# Data: 14/03/18 - 11:30
# Objetivo: TODO Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo

from math import radians, sin, cos, tan

ang = float(input('Informe um angulo: '))
print('O Valor do SENO: {:.2f}\nO Valor do COSSENO: {:.2f}\nO Valor da TANGENTE: {:.2f}'.format(sin(radians(ang)),
                                                                                         cos(radians(ang)),
                                                                                         tan(radians(ang))))
