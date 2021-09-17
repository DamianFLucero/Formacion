from os import system
from agendaModelo import *



class AgenVis:
	
	def menuCrear(self):
		print('\n\n\t        AGENDA')
		print('\n\t1 - Crear agenda')
		print('\t2 - Salir')
		return int(input('\n\tOpción: '))

	def menuAbrir(self):
		x = AgenMod.nombreAgenda()
		r = x[0]
		s = r[0]
		print(f'\n\n\tAGENDA DE {s.upper()}:')
		print('\n\t1 - Abrir agenda')
		print('\t2 - Renombrar agenda')
		print('\t3 - Eliminar agenda')
		print('\t4 - Salir')
		return int(input('\n\tOpción: '))

	def eliminar(self):
		print('\n\t      ###¡ATENCIÓN!###')
		print('\n\t¿Seguro desea eliminar agenda?')
		print('\tSe perderán todos los contactos')
		print('\t    1 - SI        2 - NO')
		return int(input('\n\tOpción: '))			

	def pedirDatos(self,*args):
		system('cls')
		print('\n\n\t----------------------')
		print('\n\tIngrese los siguientes datos:')
		salida = dict()
		for r in args:
			salida[r] = input(r+ " ")
		system('cls')   
		return salida	