# Projeto: VemPython/exe043
# Autor: rafael
# Data: 16/03/18 - 10:57
# Objetivo: TODO Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# Calcule e mostre seu IMC e mostre seu status, de acordo com a tabela abaixo:
# <18.5: Abaixo peso
# <>18.5 e 25: Peso ideal
# <>25 e 30: sobrepeso
# <>30 e 40: Obesidade
# > 40: Obesidade morbida

print('>>> VEM MOSNTRO <<<< \n')

peso = float(input('Monstro fala seu peso ai [Kg]: '))
altu = float(input('DEMORO!\nAgora fala sua altuta [m]: '))

imc = peso/(altu**2)

if imc > 0 and imc < 18.5:
    print('FRANGOLINO! TA FRACO PORRA! TU TEM {:.2f} DE IMC!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('AEW CARALHO, É HORA DO SHOW PORRA, VAMO TRABALHAR ESSE CORPINHO SAUDAVEL! {:.2f} DE IMC!'.format(imc))
elif imc >= 25 and imc < 30:
    print('VAMO COLOCAR UNS FRANGO NESSA DIETA, PQ O MALUCO É QUASE O SR BOLOTA, OU DONA PORPETA! TANTO FAZ! {:.2f} DE IMC'.format(imc))
elif imc >= 30 and imc < 40:
    print('CARALHO MULEQUE COMO VC CONSEGUE? O ROLHA DE NAVIO! VAMO CORRE! FICA GOSTOSO(A) DE VERDADE! {:.2f} DE IMC'.format(imc))
elif imc >= 40:
    print('SE SEGURA QUE ELE TA CHEGANDO! AJUDA O GORDO QUE ELE TÁ DOENTE! {:.2f} DE IMC'.format(imc))
else:
    print('TEM QUE SER UM ANIMAL PRA DIGITAR ESSA MERDA ERRADA!')