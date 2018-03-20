# Projeto: VemPython/exe055
# Autor: rafael
# Data: 16/03/18 - 17:37
# Objetivo: TODO Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o meior e o menor peso lidos

peso = [0, 0, 0, 0, 0, 0]

for i in range(0, 5):
    peso[i] = float(input('Informe o peso da {}ª pessoa: ').format(i))