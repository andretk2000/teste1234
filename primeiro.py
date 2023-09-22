def soma(val1, val2):
	return val1 + val2

def Subtrair(val1, val2):
	return val1 - val2	


a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

print('-' * 20)

operacao = int(input('1 - Somar; 2 - Subtrair.:  '))

print('-' * 20)

if operacao == 1:
	print('o resultado da soma é.:',soma(a,b))
elif operacao == 2:	 
	print('o resultado da subtração é.:',Subtrair(a,b))



