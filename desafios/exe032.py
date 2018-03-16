# Projeto: VemPython/exe032
# Autor: rafael
# Data: 15/03/18 - 15:13
# Objetivo: TODO Faça um programa que leia um ano qualquer e mostre se é BISSEXTO

from datetime import date

print("ANO BISSEXTO?")

ano = int(input('Informe o ano. Ou coloque 0: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano Bissexto: {}'.format(ano))
else:
    print('Ano Normal: {}'.format(ano))


# PORRA PROFESSOR!
#if pm == 0:
#    if sm == 0:
#        if tm == 0:
#            print('Ano Bissexto')
#        else:
#            print('Ano normal')
#    else:
#        print('Ano Bisexto')
#else:
#    print('Ano normal')
