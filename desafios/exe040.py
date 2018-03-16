# Projeto: VemPython/exe040
# Autor: rafael
# Data: 16/03/18 - 10:49
# Objetivo: TODO Leia um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# Media abaixo de 5: REPROVADO
# Media entre 5 e 6.9: RECUPERAÇÃO
# Media 7 ou superior: APROVADO

print('>>>> CLICHÊ MÉDIA ALUNO BURRO! <<<<\n')

nt0 = float(input('Informe a 1ª Nota: '))
nt1 = float(input('Informe a 2ª nota: '))

if (nt0+nt1)/2 < 5:
    print('LÁ VAI O TORTO! VAMOS ESTUDAR QUERIDÃO? >>> REPROVADO <<<')
elif (nt0+nt1)/2 >=5 and (nt0+nt1)/2 <= 6.9:
    print('QUAAAAASE FIÃO! SÓ DÁ MAIS UM GÁS QUE VC CONSEGUE! >>> RECUPERAÇÃO <<<')
else:
    print('SAPORRA É UM DEUS! PARABÉNS! >>> APROVADO <<<')
