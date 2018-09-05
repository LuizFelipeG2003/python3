n1 = int(input('digite um numero:'))
sucessor = n1 + 1
antecessor  = n1 - 1 
print('O antecessor do seu numero é {} e o sucessor é {}'.format(antecessor,sucessor))

================================================================================================

nota1 = int(input('digite a primeira nota:'))
nota2 = int(input('digite a segunda nota:'))
nota3 = int(input('digite a terceira nota:'))
soma = (nota1+nota2+nota3)/3
if soma >=6:
	print('Voce passou, Parabens!!Sua nota final foi {:.1f}'.format(soma)) 
else:  
	print('Você não passou, vai estudar! Sua nota final foi {:.1f}'.format(soma))

================================================================================================

km = float(input('Diga a quantidade de km rodados:'))
dias = int(input('Diga a quantidade de dias que o carros ficou alugado:'))
fixo = (dias * 60) + (km * 0.15)
print('O valor total a se pagar pelo carros alugado é {}'.format(fixo))

================================================================================================

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

==================================================================================================	

reais = float(input("digite a quantidade de dinheiro, para ser convertido em dolar: "))
conversao = reais / 4.18
print("Você tem {:.2f} dolares!".format(conversao))

===================================================================================================

n1 = int(input("Digite um numero: "))
v1 = n1 * 1
v2 = n1 * 2
v3 = n1 * 3
v4 = n1 * 4
v5 = n1 * 5
v6 = n1 * 6
v7 = n1 * 7
v8 = n1 * 8
v9 = n1 * 9
v10 = n1 * 10
print('Tabuada: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10))

===================================================================================================

peça1 = int(input("Digite o codigo da peça: "))
quantidade = int(input("Quantas peças vai querer?"))
valorunitario1 = 55.00
peça2 = int(input("Digite o codigo da segunda peça: "))
quantidade2 = int(input("Quantas vai querer? "))
valorunitario2 = 34.50
valortotal = (quantidade * 55.00) + (quantidade2 * 34.50)
print("O valor total a se pagar pelas peças é {:.2f}".format(valortotal))

peça1 = int(input("Digite o codigo da peça: "))
quantidade = int(input("Quantas peças vai querer?"))
valor1 = int(input("qual valor da peça"))
peça2 = int(input("Digite o codigo da segunda peça: "))
quantidade2 = int(input("Quantas vai querer? "))
valor2 = int(input("qual valor da segunda peça?"))
valortotal = (quantidade * valor1) + (quantidade2 * valor2)
print("O valor total a se pagar pelas peças é {:.2f}".format(valortotal))

====================================================================================================
