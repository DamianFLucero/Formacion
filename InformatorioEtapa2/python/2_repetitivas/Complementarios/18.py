

#18) Diseña un programa al que se proporcione como entradas dos enteros y un carácter. 
#El programa deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros dependiendo del código 
#indicado en el tercer parámetro, y devolver el resultado. Por ejemplo si el usuario ingresa la opción “S”, se deberán sumar los números.

n = int(input("\n\nIngrese un número entero: "))
x = int(input("Ingrese otro número entero: "))
o = str(input("Para sumar los dos numeros ingrese 'S', para restar 'R', para multiplicar 'M' o para dividir 'D': "))

if o.upper() == 'S':
	r = n+x
	print("\nEl resultado de la suma es: ", r)
elif o.upper() == 'R':
	r = n-x
	print("\nEl resultado de la resta es: ", r)
elif o.upper() == 'M':
	r = n*x
	print("\nEl resultado de la multiplicación es: ", r)
elif o.upper() == 'D':
	r = n/x
	print("\nEl resultado de la división es: ", r)		
else:
	print("\n# Código no válido. Vuelva a intentarlo.")