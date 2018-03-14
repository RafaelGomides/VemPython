# Projeto: VemPython/collatz
# Autor: rafael
# Data: 13/03/18 - 20:36
# Objetivo: http://dojopuzzles.com/problemas/exibe/analisando-a-conjectura-de-collatz/#

import time
print('>>> Conjectura de Collatz <<<')
pas = int(input('Infome o numero de 1 a 1.000.000: '))
n = 0
cn = 0
rn = 0
rp = 0
jm = 0
ini = time.time()
for n in range(1, pas+1):
    cn = n
    if n != 0:
        jm = 1
        while n > 1:
            jm += 1
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        print('{:0>10}'.format(cn))
        if rp < jm:
            rp = jm
            rn = cn
    else:
        print('Você digitou um valor menor que 1 !!!\nSaindo...')
fim = time.time()
print('O maior número é: {} com {} passos\nProcesso realizado em {:.3f} segundos'.format(rn, rp, fim-ini))
