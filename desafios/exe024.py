# Projeto: VemPython/exe024
# Autor: rafael
# Data: 14/03/18 - 16:53
# Objetivo: TODO Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cid = str(input('Informe o Nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
