'''
A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.

	VEHÍCULO
	 color
     ruedas
	   ^
	   ^
	 COCHE
 velocidad(km/h)
 cilindrada(cc)
'''


class Vehiculo:
	def __init__(self,color,ruedas):
		self.__color=color
		self.__ruedas=ruedas

	def setColor(self,color):
		self.__color=color
	def getColor(self):
		return self.__color

	def setRuedas(self,ruedas):
		self.__ruedas=ruedas
	def getRuedas(self):
		return self.__ruedas

	color=property(getColor,setColor)
	ruedas=property(getRuedas,setRuedas)	


class Coche(Vehiculo):
	def __init__(self,color,ruedas,velocidad,cilindrada):
		super().__init__(color, ruedas)
		self.__velocidad=velocidad
		self.__cilindrada=cilindrada

	def setVelocidad(self,velocidad):
		self.__velocidad=velocidad
	def getVelocidad(self):
		return self.__velocidad

	def setCilindrada(self,cilindrada):
		self.__cilindrada=cilindrada
	def getCilindrada(self):
		return self.__cilindrada

	velocidad=property(getVelocidad,setVelocidad)
	cilindrada=property(getCilindrada,setCilindrada)		


def mostrarVehiculo(self):
		print("######################################################")
		print(f"Color del coche es {self.color}")
		print(f"El coche tiene {self.ruedas} ruedas")
		print("######################################################")


def mostrarCoche(self):
		print("######################################################")
		print(f"Color del coche es {self.color}")
		print(f"El coche tiene {self.ruedas} ruedas")
		print(f"La velocidad final del coche es: {self.velocidad}km/h")
		print(f"La cilindrada del coche es: {self.cilindrada}cc")
		print("######################################################")



vairo = Vehiculo("rojo", 2)
mostrarVehiculo(vairo)

maseratiGT = Coche('negro',4,299,4.691)
mostrarCoche(maseratiGT)
