# Script sin refactorizar: pide dos números, los suma y los resta
try:
	a = float(input('Ingrese el primer número: '))
	b = float(input('Ingrese el segundo número: '))
except ValueError:
	print('Entrada inválida: por favor ingrese números.')
else:
	suma = a + b
	resta = a - b
	print('Suma:', suma)
	print('Resta:', resta)
