n1 = int(input('digite um numero:'))
sucessor = n1 + 1
antecessor  = n1 - 1 
print('O antecessor do seu numero é {} e o sucessor é {}'.format(antecessor,sucessor))

nota1 = int(input('digite a primeira nota:'))
nota2 = int(input('digite a segunda nota:'))
nota3 = int(input('digite a terceira nota:'))
soma = (nota1+nota2+nota3)/3
if soma >=6:
	print('Voce passou, Parabens!!Sua nota final foi {:.1f}'.format(soma)) 
else:  
	print('Você não passou, vai estudar! Sua nota final foi {:.1f}'.format(soma))

quantidade de km
qts dias foi alugado
diaria 60reais
00,15 por km rodado

km = float(input('Diga a quantidade de km rodados:'))
dias = int(input('Diga a quantidade de dias que o carros ficou alugado:'))
fixo = (dias * 60) + (km * 0.15)
print('O valor total a se pagar pelo carros alugado é {}'.format(fixo))

print('1 corintians')
print('2 flamengo')
print('3 vasco')
resposta = int(input('diga o numero do seu time: '))
if resposta == 1:
	print('Corintians')
elif resposta == 2:
	print('flamengo')
elif resposta == 3:
	print('vasco')
else:
	print('você não e ninguem!')