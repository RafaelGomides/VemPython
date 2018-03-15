# Projeto: VemPython/aula010
# Autor: rafael
# Data: 15/03/18 - 14:30
# Objetivo: TODO Condições

# BASE DA HISTÓRIA
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro Velho')
print('-- FIM --')

# CONDIÇAO SIMPLIFICADA
print('Carro Novo' if tempo <= 3 else 'Carro Velho')
print('-- FIM 2 --')

# EXEMPLO 1
nome = str(input('Qual o seu nome? '))
if nome == 'Rafael':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}!'.format(nome))

# EXEMPLO 2
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
n = (n1 + n2)/2
print('Sua média é {}'.format(n))
if n >= 6:
    print('Sua média foi boa! PARABENS')
else:
    print('SUA MÉDIA FOI PÉSSIMA! SE MATA!')

