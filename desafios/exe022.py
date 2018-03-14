# Projeto: VemPython/exe022
# Autor: rafael
# Data: 14/03/18 - 16:48
# Objetivo: TODO Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minusculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Infome um nome completo: '))
nse = nome.split()
pn = nse[0]
nse = ''.join(nse)
print('\nSeu nome com todas as letras MAIUSCULAS: {}\n'
      'Seu nome com todas as letras MINUSCULAS: {}\n'
      'Seu nome possui {} letras sem os espaços\n'
      'Seu primeiro nome possui: {} letras'.format(
    nome.upper(),
    nome.lower(),
    len(nse),
    len(pn)
))