# Projeto: VemPython/exe031
# Autor: rafael
# Data: 15/03/18 - 15:02
# Objetivo: TODO Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem.
# Cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas

print('BUSÃO DA LOUCURA\n')

km = float(input('Informe a distância da viagem: Km '))
if km > 200:
    print('ETA QUE EU TÔ NO DE VOLTA PRA MINHA TERRA!')
    print('O valor da sua Viagem: R$ {}'.format(km*0.45))
else:
    print('Chama um Uber Poxa!')
    print('O Valor da sua viagem: R$ {}'.format(km*0.5))
