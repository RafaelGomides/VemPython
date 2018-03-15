# Projeto: VemPython/exe026
# Autor: rafael
# Data: 14/03/18 - 16:55
# Objetivo: TODO Faça um programa que leia uam frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela ultima vez

frase = str(input('Escreve uma parada ai: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A letra A aparece na {} posição'.format(1+frase.lower().find('a')))
print('A ultima letra A aparece na {} posição'.format(1+frase.lower().rfind('a')))
