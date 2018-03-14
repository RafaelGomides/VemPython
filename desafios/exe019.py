# Projeto: VemPython/exe019
# Autor: rafael
# Data: 14/03/18 - 11:35
# Objetivo: TODO Um professor quer sortear um dos quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

alunos = []
for cont in range(0, 4):
    alunos.append(str(input('Informe o nome do aluno {}: '.format(cont+1))))

print('O Aluno escolhido para limpar o quadro é: {}'.format(choice(alunos)))