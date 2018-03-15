# Projeto: VemPython/exe034
# Autor: rafael
# Data: 15/03/18 - 15:15
# Objetivo: TODO Escre um programa que pergunte o salario de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%
# Para salarios inferiores ou iguais, o aumento é de 15%

sal = float(input('Informe seu salario: R$'))

if sal > 1250:
    print('Seu aumento é de 10%: R${}'.format(sal+(sal*0.1)))
else:
    print('Seu aumento é de 15%: R${}'.format(sal+(sal*0.15)))