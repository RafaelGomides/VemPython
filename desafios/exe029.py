# Projeto: VemPython/exe029
# Autor: rafael
# Data: 15/03/18 - 14:59
# Objetivo: TODO Escreva um programa que leia a velocidade de um carro.
# Se ela passar de 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite

print('RADAR FELA\n')
vel = float(input('Informe a velocidade detectada: Km/h '))
if vel > 80.0:
    mul = (vel - 80) * 7
    print('MULTADO!\nValor: R$ {}'.format(mul))
else:
    print('Relaxa ai Fião!')