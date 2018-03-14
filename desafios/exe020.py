# Projeto: VemPython/exe020
# Autor: rafael
# Data: 14/03/18 - 11:37
# Objetivo: TODO O mesmo professor do desafio anterior quer a ordem de apresentação de trabalhos dos
# quatro alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

alunos = []
for cont in range(0, 4):
    alunos.append(str(input('Informe o nome do aluno {}: '.format(cont+1))))

shuffle(alunos)

for cont in range(0, 4):
    print('O {}º aluno é: {}'.format(cont+1, alunos[cont]))
