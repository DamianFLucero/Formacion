'''

150 años es el tiempo que tarda una bolsa de plástico común en degradarse y 
una botella de PET puede tardar 1.000 años en desaparecer. 

Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

Un trozo de chicle tarda 5 años en degradarse. 

Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: 
Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.
'''

def degradable(a):
	if a == 1:
		print("\n#Bolsa de plástico\nTarda 150 años en degradarse")
	elif a == 2:
		print("\n#Botella PET\nTarda 1.000 años en degradarse")
	elif a == 3:
		print("\n#Envase tetrabrik\nTarda 30 años en degradarse")
	else:
		print("\n#Chicle\nTarda 5 años en degradarse")


preg = int(input("\nPara saber cuanto tarda en degradarse un elemento seleccione:\n1- Bolsa de plástico\n2- Botella PET\n3- Envase tetrabrik\n4- Chicle\n\nOpción: "))
degradable(preg)


