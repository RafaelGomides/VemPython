# Projeto: VemPython/exe038
# Autor: rafael
# Data: 16/03/18 - 10:43
# Objetivo: TODO Escreva um programa que leia dois numeros inteiros e compare-os. Mostrando na tela
# uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior os dois são iguais

vl1 = int(input('Informe um número Inteiro: '))
vl2 = int(input('Informe outro número Inteiro: '))

if vl1 > vl2:
    print('{} é maior que {}'.format(vl1, vl2))
elif vl2 > vl1:
    print('{} é maior que {}'.format(vl2, vl1))
else:
    print('{} e {} são iguais'.format(vl1, vl2))
