# Projeto: VemPython/exe004
# Autor: rafael
# Data: 13/03/18 - 16:36
# Objetivo: TODO Faça um programa que leia alfo pelo teclado e mostre na tela o seu tipo e todas as informações possiveis sobre ele.

algo = input('Escreva algo: ')
print('É do tipo: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É totalmente maiusculo? {}'.format(algo.isupper()))
print('É numérico? {}'.format(algo.isnumeric()))
print('É alfanumerico? {}'.format(algo.isalnum()))
print('É alfabético? {}'.format(algo.isalpha()))
print('Está minusculo? {}'.format(algo.islower()))
print('Está Captalizada? {}'.format(algo.istitle()))
