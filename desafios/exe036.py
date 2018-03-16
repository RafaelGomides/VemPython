# Projeto: VemPython/exe036
# Autor: rafael
# Data: 16/03/18 - 10:38
# Objetivo: TODO Escreva um programa para aprovar o empréstimo bancário de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensaç, sabendo que ela não pode exceder 30% do salário ou entao o empréstimo será negado

print('Empréstimo Bancário')

vlrCasa = float(input('Informe o valor da casa: R$ '))
salComp = float(input('Informe o Salário do comprador: R$ '))
qtdPres = int(input('Informe em quantos anos ele deseja pagar '))

qtdPres = qtdPres*12
vlrPres = vlrCasa/qtdPres

if vlrPres > salComp*0.3:
    print('O Valor da prestação é: {:.2f}\nInfelizmente ele excede a faixa de segurança!\nSeu empreśtimo foi negado'.format(vlrPres))
else:
    print('Empréstimo aprovado!\nO valor a ser pago é de R$ {:.2f} em {}x de R$ {:.2f}'.format(vlrCasa, qtdPres, vlrPres))