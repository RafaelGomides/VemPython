# Projeto: VemPython/exe053
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Crie um programa que leia uma frase qualquer e diga se ela é um palindramo, desconsiderando os espaços

frase = str(input('Informe a frase: '))

fraseTest = frase.strip().replace(" ", "").upper()

if fraseTest == fraseTest[::-1]:
    print('A Frase: {}\nÉ um polindramo!'.format(frase))