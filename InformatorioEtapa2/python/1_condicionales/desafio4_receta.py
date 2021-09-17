
print("\n\n Bienvenido!\n\n Receta ecológica 1:\n -Lenteja\n -Apio\n\n Receta ecológica 2:\n -Morrón\n -Cebolla")
seleccion = int(input("\n Elija 1 o 2 para una receta: "))
if seleccion == 1:
	print("\n ################################################################################")
	print("\n Ha seleccionado receta ecológica con lenteja y apio, ingrese 1 o 2 para agregar:\n 1 Verduras\n 2 Berenjena ")
	sel2 = int(input("\n Ingrese: "))
	print("\n ################################################################################")
	if sel2 == 1:
		print("\n Confirmación del pedido:\n Ensalada ecológica de lenteja, apio y verduras.")
	elif sel2 == 2:
		print("\n Confirmación del pedido:\n Ensalada ecológica de lenteja, apio y berenjena.")
	else:
		print("\n Vuelva a ingresar su pedido")
elif seleccion == 2:
	print("\n ################################################################################")
	print("\n Ha seleccionado receta ecológica con morrón y cebolla, ingrese 1 o 2 para agregar:\n 1 Verduras\n 2 Berenjena ")
	sel2 = int(input("\n Ingrese: "))
	print("\n ################################################################################")
	if sel2 == 1:
		print("\n Confirmación del pedido:\n Ensalada ecológica de morrón, cebolla y verduras.")
	elif sel2 == 2:
		print("\n Confirmación del pedido:\n Ensalada ecológica de morrón, cebolla y berenjena.")
	else:
		print("\n Vuelva a ingresar su pedido")
else:
	print("\n ################################################################################")
	print("\n Vuelva a ingresar su pedido")
