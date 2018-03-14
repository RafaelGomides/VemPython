# Projeto: VemPython/exe015
# Autor: rafael
# Data: 14/03/18 - 11:11
# Objetivo: TODO Escreva um programa que pergunta a quantidade de Km percorrido por um carro alugado e
# a qunatidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Informe a quantidades de dias utilizado: '))
kmr = float(input('Informe a quantidade de Kms rodados: '))
print('Você deve pagar: R${:.2f}'.format((dias*60)+(kmr*0.15)))