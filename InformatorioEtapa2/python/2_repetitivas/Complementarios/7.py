

print("\n\nPara conocer la suma de los multiplos de 5 comprendidos entre A y B:")

a = int(input("Ingrese el valor de 'A': "))
b = int(input("Ingrese el valor de 'B': "))
x = 0
r = 0

if a < 0 or b < 0:
	print("\n\n# El programa no se ejecuta con números menores a 0.\nVuelva a intentarlo.")
elif a > b:
	r = b
	b = a
	a = r
	for i in range(a,b+1):
		i = i*5
		if i%5 == 0:
			x = i + x
	else:
		print("\n# La suma de los multiplos de 5 entre", a,"y", b,"es:", x)
else:
	for i in range(a,b+1):
		i = i*5
		if i%5 == 0:
			x = i + x
	else:
		print("\n# La suma de los multiplos de 5 entre", a,"y", b,"es:", x)