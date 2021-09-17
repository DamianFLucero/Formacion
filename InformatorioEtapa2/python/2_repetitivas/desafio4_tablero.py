
import os
os.system('color')

x = int(input("Ingrese cantidad de filas: "))
y = int(input("Ingrese cantidad de columnas: "))

if y % 2 == 0:
	par = False
else:
	par = True


for x in range(x):
	for z in range(y//2):
		if x % 2 == 0:
			print("\033[93m[X]", end="")
			print("\033[1;32;40m[0]", end="")
		else:
			print("\033[1;32;40m[X]", end="")
			print("\033[93m[0]", end="")
	if par:
		if x % 2 == 0:
			print("\033[93m[X]", end="")
		else:
			print("\033[1;32;40m[0]", end="")
	print("")