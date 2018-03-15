#Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
#Entregar o menor número de notas;
#É possível sacar o valor solicitado com as notas disponíveis;
#Saldo do cliente infinito;
#Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
#Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
#Exemplos:
#Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
#Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
#http://dojopuzzles.com/problemas/exibe/caixa-eletronico/

print('Olá bem vindo a ATM\n\nNotas disponiveis:\nR$ 100,00\nR$ 50,00\nR$ 20,00\nR$ 10,00')

vlr = int(input('Informe o valor que deseja sacar: '))

u = vlr // 1 % 10

saque100 = 0
saque50 = 0
saque20 = 0
saque10 = 0

if u == 0 :
	if vlr >= 100:
		saque100 = vlr // 100
		vlr = vlr-(saque100*100)
	if vlr >= 50:
		saque50 = vlr // 50
		vlr = vlr-(saque50*50)
	if vlr >= 20:
		saque20 = vlr // 20
		vlr = vlr-(saque20*20)
	if vlr >= 10:
		saque10 = vlr // 10
		vlr = vlr-(saque10*10)
	print('Notas: {} de 100 - {} de 50 - {} de 20 - {} de 10'.format(saque100, saque50, saque20, saque10))
else:
	print('Sem notas disponiveis\nO valor solicitado é invalido')
