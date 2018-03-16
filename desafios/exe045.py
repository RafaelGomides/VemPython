# Projeto: VemPython/exe045
# Autor: rafael
# Data: 16/03/18 - 11:01
# Objetivo: TODO Criar um programa que faça com que o comptador jogue JOKENPO com o usuário

from time import sleep
from random import randint

opc = 1
uv = 0
cv = 0

# Introdução
text = ['\033[1;3{}mJO\033[m'.format(randint(0, 7)),
        '\033[1;3{}mKEN\033[m'.format(randint(0, 7)),
        '\033[1;3{}mPÔ\033[m'.format(randint(0, 7))]

for i in range(0, 3):
    print(text[i], end="", flush=True)
    sleep(1)

escolhas = ['\033[1;30;4{}mPEDRA\033[m'.format(randint(1, 7)),
            '\033[1;30;4{}mPAPEL\033[m'.format(randint(1, 7)),
            '\033[1;30;4{}mTESOURA\033[m'.format(randint(1, 7))]

# Inicio do Jogo
while opc == 1:

    # Escolhas
    com = randint(0, 2)

    usr = int(input('\n\nFaça sua Escolha: \n'
                    '1 - {}\n2 - {}\n3 - {}\n'
                    'Opção: '.format(escolhas[0], escolhas[1], escolhas[2])))-1

    # Resultado
    print('\n\nEu escolhi {} e você {}!\n\n'.format(escolhas[com], escolhas[usr]))

    if com == usr:
        print('\033[7;33mEMPATE\033[m')
    elif (com == 0 and usr == 2) or (com == 1 and usr == 0) or (com == 2 and usr == 1):
        print('\033[7;31mVOCÊ PERDEU!\033[m')
        cv += 1
    else:
        print('\033[7;32mVOCÊ GANHOU\033[m')
        uv += 1

    # Placar
    print('O PLACAR ESTÁ:\n\033[34mUSUÁRIO\033[m \033[32m{}\033[m X \033[32m{}\033[m \033[36mCPU\033[m'.format(uv, cv))

    sleep(3)

    opc = int(input('\n\nDeseja Tentar Novamente?\n'
                    '\n\033[4;32m1 - Para sim'
                    '\n\033[4;31m2 - Para não\033[m'
                    '\nOpção: '))

