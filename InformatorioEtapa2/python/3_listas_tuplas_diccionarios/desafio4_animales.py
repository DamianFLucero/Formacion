

especies = []
salida = True

while salida == True:
	ingreso = str(input("Ingrese nombre de la especie: "))
	print("\n¡Hola! soy", ingreso,", cuidame.")
	especies.append(ingreso)
	pregunta = int(input("\n\nPresione 1 para cargar otra especie o 0 para salir: "))
	if pregunta > 0:
		salida = True
	else:
		salida = False
else:
	tupla = tuple(especies)
	print(tupla) 

print("\n######################################\n\nPara enviar un mensaje a cada especie:")
p = int(input("Ingrese un número a partir de la especie por la cual quiere empezar: "))
n = int(input("Ingrese cuantas especies a partir de la selección anterior quiere imprimir: "))

for i in range(p-1 , n+p-1):
	print("\n¡Hola! soy", tupla[i],", cuidame.")
	print("")