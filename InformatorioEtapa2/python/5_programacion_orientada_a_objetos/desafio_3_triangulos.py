

'''
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los
atributos, imprimir el valor del lado con un tamaño mayor y el
tipo de triángulo que es (equilátero, isósceles o escaleno).
'''


class Triangulo:
	def __init__(self,ladoA,ladoB,ladoC):
		self.ladoA=ladoA
		self.ladoB=ladoB
		self.ladoC=ladoC


	def printTriangulo(self):
		return print(f"\nLado A: {self.ladoA}\nLado B: {self.ladoB}\nLado C: {self.ladoC}")


	def ladoTriangulo(self):
		lista=[]
		lista.append(self.ladoA)
		lista.append(self.ladoB)
		lista.append(self.ladoC)
		lista.sort()			
		print(f"\nEl tamaño mayor del triángulo es: {lista[2]}")	


	def tipoTriangulo(self):
		if self.ladoA==self.ladoB and self.ladoB==self.ladoC:
			return print(f"Triángulo equilátero (sus tres lados son de igual tamaño)")
		elif self.ladoA==self.ladoB or self.ladoA==self.ladoC or self.ladoB==self.ladoC:
			return print(f"Triángulo isósceles (dos lados de igual tamaño)")
		else:
			return print(f"Triángulo escaleno (sus tres lados son de distintos tamaños)")




ejemplo=Triangulo(7,9,7)
ejemplo.printTriangulo()
ejemplo.ladoTriangulo()
ejemplo.tipoTriangulo()

