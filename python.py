idade = int(input('digite a idade: '))

if idade > 18 and idade < 65:
	print('voto obrigatorio')
elif idade >= 16 and idade < 18:
	print('voto facultativo')
elif idade < 16 or idade > 65 :
	print('não vota')