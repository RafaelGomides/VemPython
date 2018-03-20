# Projeto: VemPython/exe046
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogo de artificio, indo de 10 até 0.
# com uma pausa de 1 segundo entre eles.

from time import sleep

print('Contagem regressiva...')

for i in range(10, 0, -1):
    print(i)
    sleep(1)

print('FOGO NA BABILONIA')