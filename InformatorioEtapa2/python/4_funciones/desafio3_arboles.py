'''
Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles - 
plantados en diferentes ciudades de Argentina durante la cuarentena. 
Luego la función debe devolver dos listas ordenadas. 
La primera con las cantidades que superen los 100 y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.

'''

def separar(r):
	mas = list()
	menos = list()


	for i in r:
		if i[0]>100:
			mas.append(i)
		else:
			menos.append(i)
	mas.sort()			
	print("\nMás de 100:")
	print(mas)
	menos.sort()
	print("\nMenos de 100")
	print(menos)



lista = [[1524,'Cordoba'],[57,'Ushuaia'],[217,'Paraná'],[125,'Salta'],[43,'Formosa'],[75,'Viedma'],[836,'La Rioja']]
print("\nArboles plantados por ciudad durante la cuarentena: ")
separar(lista)
