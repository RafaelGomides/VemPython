# Projeto: VemPython/exe028
# Autor: rafael
# Data: 15/03/18 - 14:50
# Objetivo: TODO Escreva um programa que faça o computador "pensar" em um número de 0 a 5 e peça para o usuário
# descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever se o usuário venceu ou perdeu

from random import randint
from time import sleep

num = randint(0, 5)
print("-="*50)
print('Estou pensando em um número de 0 a 5...\nTente adivinhar qual é!?')
print("-="*50)
adv = float(input('Eu acho que é: '))
print('\n\nProcessando...\n\n')
sleep(3)
if adv == num:
    print('Você é uma espécie de Mito!\nEu pensei em: {}'.format(num))
else:
    print('Hahah! Eu sempre Ganho!\nVOCE ERROU!\nEu pensei em: {}'.format(num))

