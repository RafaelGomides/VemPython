# Projeto: VemPython/exe037
# Autor: rafael
# Data: 16/03/18 - 10:41
# Objetivo: TODO escreva um programa que leia um numero inteiro qualquer e peça para o usuário
# escolher qual a base de conversão;
# 1 - BINARIO; 2 - OCTAL; 3 - HEXADECIMAL

print('Sistema Conversão')

num = int(input('Informe um número inteiro: '))

print('Hexadecimal: {}\n'
      'Octal: {}\n'
      'Binário: {}'
      .format(hex(num)[2:].upper(),
              oct(num)[2:],
              bin(num)[2:]))
