
#z.1. Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.


lista_A = []
lista_B = []
salir = True

print("\nPara determinar si una palabra es palíndromo:\nIngrese una palabra letra por letra, y escriba 'salir' para ver el resultado.")

while salir:
	ing = input("Ingreso: ")
	if ing.lower() == 'salir':
		salir == False
		break
	else:
		lista_A.append(ing)
		lista_B.append(ing)

a = "".join(lista_A)
b = reversed(lista_B)
c = "".join(b)

if a == c:
	print("\n#La palabra es palíndromo:\n", a, "\n", c)
else:
	print("\n#La palabra no es palíndromo:\n", a,"\n", c)

