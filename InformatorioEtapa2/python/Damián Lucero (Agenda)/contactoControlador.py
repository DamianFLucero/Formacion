from os import system
from contactoModelo import * 
from contactoVista import *



class contactoControlador:
	def __init__(self):
		self.__CnVista = Contacto()
		self.menu()

	#Menu de contactos
	def menu(self):
		system('cls')
		seleccion = self.__CnVista.menu()
		if seleccion == 1:
			self.mostrarContactos()
		elif seleccion == 2:
			self.buscarContacto()
		elif seleccion == 3:
			self.agregarContacto()
		elif seleccion == 4:
			self.editarContacto()
		elif seleccion == 5:
			self.eliminarContacto()			
		elif seleccion == 6:
			self.cerrarContacto()
		else:
			print("\tingrese valor correcto")
			input("\t")
			self.menu()	
	
	#Mostrar todos los contactos		
	def mostrarContactos(self):
		system('cls')
		x = Persona.mostrar()
		self.__CnVista.resultados(x)
		input("\t")
		system('cls')
		self.menu()

	#Buscar un contacto por PK (Teléfono)
	def buscarContacto(self):
		dato = self.__CnVista.pedirDatos('\n\tBuscar por numero de teléfono: ')
		x = Persona.buscar(dato['\n\tBuscar por numero de teléfono: '])
		self.__CnVista.resultados(x)
		input("\t")
		system('cls')
		self.menu()

	#Agregar un contacto
	def agregarContacto(self):
		datos = self.__CnVista.pedirDatos('\n\tTeléfono: ','\n\tNombre: ','\n\tEmail: ')
		x = Persona(datos['\n\tTeléfono: '], datos['\n\tNombre: '], datos['\n\tEmail: '])
		Persona.agregar(x)
		self.menu()

	#Editar un contacto por PK (Teléfono)	
	def editarContacto(self):
		datos = self.__CnVista.pedirDatos('\n\tNombre nuevo: ', '\n\tEmail nuevo: ', '\n\tTeléfono a modificar: ')
		Persona.modificar(datos['\n\tNombre nuevo: '], datos['\n\tEmail nuevo: '], datos['\n\tTeléfono a modificar: '])
		self.menu()

	#Eliminar un contacto por PK (Teléfono)
	def eliminarContacto(self):
		dato = self.__CnVista.pedirDatos('\n\tTeléfono del contacto que desea eliminar: ')
		Persona.eliminar(dato['\n\tTeléfono del contacto que desea eliminar: '])
		self.menu()		

	#Volver al menu de agenda
	def cerrarContacto(self):
		pass


