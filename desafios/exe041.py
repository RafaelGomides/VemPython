# Projeto: VemPython/exe041
# Autor: rafael
# Data: 16/03/18 - 10:49
# Objetivo: TODO A configuração Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade.
# Até 9: MIRIM
# Até 14: INFANTIL
# Até 19: JUNIOR
# Até 20: SENIOR
# Acima: Master

from datetime import date

ano = date.today().year-int(input('>>>> SEM APELAR COM OS AMIGUINHOS <<<<\n\nInforme o ano de nascimento do atleta: '))

if ano > 0 and ano <= 9:
    print("MIRIM")
elif ano > 9 and ano <= 14:
    print('INFANTIL')
elif ano > 14 and ano <= 19:
    print('JUNIOR')
elif ano == 20:
    print('SENIOR')
elif ano > 20:
    print('MASTER')
else:
    print('ESSE SERUMANO NEM NASCEU AINDA!!!')
