from os import system



class Contacto:

	def menu(self):
		print('\n\t          MENU')         
		print('\n\t1 - Mostrar contactos')
		print('\t2 - Buscar contacto')
		print('\t3 - Agregar contacto')
		print('\t4 - Editar contacto')
		print('\t5 - Eliminar contacto')
		print('\t6 - Volver a menu de agenda')
		return int(input('\n\tOpción: '))

	def pedirDatos(self, *args):
		system('cls')
		print('\n\n\t-----------------------------')
		print('\n\tIngrese los siguientes datos:')
		salida = dict()
		for r in args:
			salida[r] = input(r+ " ")
		system('cls')   
		return salida

	def resultados(self,resultados):
		print('\n\n\tContacto/s: \n')
		for r in resultados:
			print("\t", r)


