# Projeto: VemPython/exe017
# Autor: rafael
# Data: 14/03/18 - 11:25
# Objetivo: TODO Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
# um triangulo retangulo, calculo e mostre o comprimento da hipotenusa

from math import hypot

catO = float(input('Informe o Cateto Oposto: '))
catA = float(input('Informe o Cateto Adjacente: '))
#hip = (catO ** 2 + catA ** 2) ** (1/2)
print('A hipotenusa vale: {:.2f}'.format(hypot(catO, catA)))
