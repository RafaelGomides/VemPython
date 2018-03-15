# Projeto: VemPython/exe025
# Autor: rafael
# Data: 14/03/18 - 16:54
# Objetivo: TODO Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Informe um Nome: '))
print('É verdadeiro que tem Silva no seu nome? {}'.format('silva' in nome.lower()))