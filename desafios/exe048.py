# Projeto: VemPython/exe048
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Faça um programa que calcule a soma entre todos os numeros impares que são múltiplos de três e que se encontram
# no intervalo de 1 até 500

soma = 0
for i in range(0, 501):
    if i % 3 == 0:
        if i % 2 == 1:
            soma += i
            print(soma)
