print("\nIngrese:\n'1' para barrio céntrico\n'2' para barrio no céntrico")
barrio = int(input("\n\nOpción: "))
print("\n####################")
if barrio == 1:
	nombre = str(input("\nIngrese el nombre del barrio: "))
	if nombre[0] <= ('l'):
		print("\n####################")
		print("\nSección A")
	elif nombre[0] > ('l'):
		print("\n####################")
		print("\nSección B")
elif barrio == 2:
	nombre = str(input("\nIngrese el nombre del barrio: "))
	if nombre[0] > ('m'):
		print("\n####################")
		print("\nSección A")
	elif nombre[0] <= ('m'):
		print("\n####################")
		print("\nSección B")