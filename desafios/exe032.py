# Projeto: VemPython/exe032
# Autor: rafael
# Data: 15/03/18 - 15:13
# Objetivo: TODO Faça um programa que leia um ano qualquer e mostre se é BISSEXTO

print("ANO BISSEXTO?")

ano = int(input('Informe o ano: '))

pm = ano % 4
sm = ano % 100
tm = ano % 400

if pm == 0:
    if sm == 0:
        if tm == 0:
            print('Ano Bissexto')
        else:
            print('Ano normal')
    else:
        print('Ano Bisexto')
else:
    print('Ano normal')
