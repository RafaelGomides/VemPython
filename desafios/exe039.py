# Projeto: VemPython/exe039
# Autor: rafael
# Data: 16/03/18 - 10:46
# Objetivo: TODO Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# Se ele ainda ai se alistar
# Se é hora de se alistar
# Se já passou do tempo do alistamento
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

print('>>>> ALISTAMENTO FIÃO <<<<')

ano = int(input('Informe o Ano de nascimento: '))

dif = date.today().year-ano

if dif > 18:
    print('Você já passou do tempo de se alistar por {} ano'.format(dif-18))
elif dif < 18:
    print('Acalma o coração faltam {} ano ainda'.format(18-dif))
else:
    print('VAI SE ALISTAR CÃO!!!')
