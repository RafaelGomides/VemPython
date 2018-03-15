# Projeto: VemPython/exe027
# Autor: rafael
# Data: 14/03/18 - 16:58
# Objetivo: TODO Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza; Primeiro: Ana; Ultimo: Souza

nome = str(input('Informe seu nome completo: ')).strip().split()
print('O Primeiro nome é {} e o último nome é {}'.format(nome[0], nome[len(nome)-1]))
