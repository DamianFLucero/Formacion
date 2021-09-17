from contactoControlador import *
from agendaVista import *
from agendaModelo import *
from os import system



class AgenCont:

	def __init__(self):
		self.__AgVista = AgenVis()
		self.decision()

	#Abre un menu u otro dependiendo si existe, o no, una agenda	
	def decision(self):
		x = AgenMod.consultar()
		r = x[0]
		if r[0] == 0:	
			self.menuAgendaNueva()
		else:
			self.menuAgendaCreada()

	#Menu para crear agenda nueva
	def menuAgendaNueva(self):
		system('cls')
		seleccion = self.__AgVista.menuCrear()
		if seleccion == 1:
			self.crearAg()
		elif seleccion == 2:
			self.salir()
		else:
			print("\tingrese valor correcto")
			input("\t")
			self.menuAgendaNueva()

	#Menu cuando ya se tiene una agenda creada
	def menuAgendaCreada(self):
		system('cls')
		seleccion = self.__AgVista.menuAbrir()
		if seleccion == 1:
			self.abrirAg()
		elif seleccion == 2:
			self.renombrarAg()
		elif seleccion == 3:
			self.eliminarAg()
		elif seleccion == 4:
			self.salir()		
		else:
			print("\tingrese valor correcto")
			input("\t")
			self.menuAgendaCreada()
	
	#Crea agenda
	def crearAg(self):
		dato = self.__AgVista.pedirDatos('\n\tPropietario: ')
		x = AgenMod(dato['\n\tPropietario: '])
		AgenMod.crearAgenda(x)
		self.menuAgendaCreada()

	#Abre el menu de contactos
	def abrirAg(self):
		contactoControlador()
		system('cls')
		self.menuAgendaCreada()
		
	#Modifica el nombre de la agenda	
	def renombrarAg(self):
		datos = self.__AgVista.pedirDatos('\n\tUsuario: ')
		x = AgenMod(datos['\n\tUsuario: '])
		AgenMod.modificar(x)
		self.decision()

	#Elimina completamente la agenda, incluyendo contactos
	def eliminarAg(self):
		system('cls')
		seleccion = self.__AgVista.eliminar()
		if seleccion == 1:
			AgenMod.eliminar()
			AgenMod.eliminarCont()
			AgenCont()
		elif seleccion == 2:
			AgenCont()
		else:
			print("\tingrese valor correcto")
			input("\t")
			AgenCont.eliminarAg()		

	#Cierra el programa		
	def salir(self):
		system('cls')
		print('\n\n\t¡ADIÓS!')
		input()
		pass

#Ejecuta el programa
AgenCont()


