# Projeto: VemPython/exe010
# Autor: rafael
# Data: 13/03/18 - 17:02
# Objetivo: TODO Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$ 1,00 = R$ 3,27

reais = float(input('Quantidade de dinheiro em R$: '))
conve = reais*0.327
print('Você consegue comprar: US$ {}'.format(conve))
