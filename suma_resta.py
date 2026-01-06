print("Bienvenido \n")
try:
	a = float(input('Ingrese el primer número: '))
	b = float(input('Ingrese el segundo número: '))

except ValueError:
	print('Entrada inválida: por favor ingrese números.')

else:
	suma = a + b
	resta = a - b
	print('\nSuma:', suma)
	print('\nResta:', resta)

print("\nGracias por usar el programa")