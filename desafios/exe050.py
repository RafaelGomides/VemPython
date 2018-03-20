# Projeto: VemPython/exe050
# Autor: rafael
# Data: 16/03/18 - 17:29
# Objetivo: TODO Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor for impar, desconsidera-lo

num = []
soma = 0

for i in range(0, 6):
    num.append(int(input('Informe o {}º Valor: '.format(i+1))))
    if num[i] % 2 == 0:
        soma += num[i]
print('A soma dos pares é: {}'.format(soma))
