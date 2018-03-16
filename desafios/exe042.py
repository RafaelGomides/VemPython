# Projeto: VemPython/exe042
# Autor: rafael
# Data: 16/03/18 - 10:55
# Objetivo: TODO Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será
# formado:
# Equilatero: todos lados =
# Isósceles: dois lados =
# Escaleno: todos os lados diferentes

print('DE DOER ESSE TRIANGULO PT.2\n')

a = float(input('Informe a primeira Reta: '))
b = float(input('Informe a segunda Reta: '))
c = float(input('Informe a terceira Reta: '))

if b-c < a < b+c:
    la = 1
else:
    la = 0

if a-c < b < a+c:
    lb = 1
else:
    lb = 0

if a-b < c < a+b:
    lc = 1
else:
    lc = 0

if la+lb+lc == 3:
    print('É possível formar um triangulo\n')
    if a == b == c:
        print('E é um triangulo Equilatero')
    elif a == b or a == c or b == c:
        print('E é um triangulo Isósceles')
    else:
        print('E é um triangulo Escaleno')
else:
    print('Não é possível formar um triangulo')


