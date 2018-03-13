# Projeto: VemPython/exe011
# Autor: rafael
# Data: 13/03/18 - 17:04
# Objetivo:TODO Faça um programa que leia a largura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Informe quantos metros de ALtura: '))
largura = float(input('Informe quantos metros de Largura: '))
qutt = (largura*altura)/2
print('Você vai precisar de: {}l de tinta'.format(qutt))