'''
Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

Realiza una función llamada catalogar() 
que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.

Modifica la función catalogar() para que reciba un argumento optativo ruedas, 
haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. 
Ponla a prueba con 0, 2 y 4 ruedas como valor.


		    VEHICULO
		     color
		     ruedas
	^					  ^
	^					  ^
  COCHE               BICICLETA
velocidad(km/h)     tipo(urbana/deportiva)
cilindrada(cc)
    ^                     ^
    ^                     ^
 CAMIONETA           MOTOCICLETA
 carga(kg)           velocidad(km/h)
                     cilindrada(cc)
'''


class Vehiculo:
	def __init__(self,color,ruedas):
		self.color=color
		self.ruedas=ruedas

	def __str__(self):	
		return f"\nColor: {self.color}\nRuedas: {self.ruedas}"

class Coche(Vehiculo):
	def __init__(self,color,ruedas,velocidad,cilindrada):
		super().__init__(color,ruedas)
		self.velocidad=velocidad
		self.cilindrada=cilindrada

	def __str__(self):	
		return f"\nColor: {self.color}\nRuedas: {self.ruedas}\nVelocidad final: {self.velocidad}km/h\nCilindrada: {self.cilindrada}cc"


class Camioneta(Coche):
	def __init__(self,color,ruedas,velocidad,cilindrada,carga):
		super().__init__(color,ruedas,velocidad,cilindrada)
		self.carga=carga

	def __str__(self):	
		return f"\nColor: {self.color}\nRuedas: {self.ruedas}\nVelocidad final: {self.velocidad}km/h\nCilindrada: {self.cilindrada}cc\nCarga: {self.carga}kg"

	
class Bicicleta(Vehiculo):
	def __init__(self,color,ruedas,tipo):
		super().__init__(color,ruedas)
		self.tipo=tipo

	def __str__(self):	
		return f"\nColor: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}"


class Motocicleta(Bicicleta):
	def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
		super().__init__(color,ruedas,tipo)
		self.velocidad=velocidad
		self.cilindrada=cilindrada

	def __str__(self):	
		return f"\nColor: {self.color}\nRuedas: {self.ruedas}\nTipo: {self.tipo}\nVelocidad final: {self.velocidad}km/h\nCilindrada {self.cilindrada}cc"


def catalogar(x):
	for i in x:
		print("\n###############################\n",i.__class__.__name__,"\n",i,"\n###############################\n")	


def verRuedas(lista,rued=None):
	if rued == None:
		for i in lista:
			print("\n###############################\n",i.__class__.__name__,"\n",i,"\n###############################\n")
	else:	
		contador=0
		for i in lista:
			if rued == i.ruedas:
				contador+=1
				print("\n",i.__class__.__name__,i,"\n")
		print(f"\n# Se han encontrado {contador} vehículos con {rued} ruedas #")


olmo = Bicicleta('verde',2,'deportiva')
ns200 = Motocicleta('amarillo',2,'urbana',136,199)
peugeot306 = Coche('negro',4,192,1761)
ram = Camioneta('azul',4,175,6690,554)
catalogo = [olmo,ns200,peugeot306,ram]


#catalogar(catalogo)
verRuedas(catalogo,4)	

