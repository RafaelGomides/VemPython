# Projeto: VemPython/exe044
# Autor: rafael
# Data: 16/03/18 - 11:01
# Objetivo: TODO Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço noraml e condição de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

print('>>> VENDA DO IRINEU <<<\n')
vlr = float(input('Informe o valor do Produto: R$ '))
frp = int(input('\n>>> FORMAS DE PAGAMENTO: <<<'
                '\n1 - Dinheiro/Cheque 10% desc.'
                '\n2 - Cartão, a Vista 5% desc.'
                '\n3 - Cartão, 2x s/ Juros'
                '\n4 - Cartão, 3x+ 20% juros'
                '\nOpção: '))

qtdP = 0

if frp == 1:
    vlr = vlr-(vlr*0.1)
elif frp == 2:
    vlr = vlr-(vlr*0.05)
elif frp == 3:
    qtdP = 2
else:
    qtdP = int(input('Informe a quantidade de Prestações: '))
    vlr = vlr+(vlr*0.2)

print('O valor a ser cobrado é: R$ {} em {}x'.format(vlr, qtdP))
