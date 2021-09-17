
print("\nBienvenido a pizzeria Bella Napoli, seleccione:\n")

pizza = int(input("(1) Pizza vegetariana\n(2) Pizza no vegetariana\n\n"))
if pizza == 1:
	print("\nHa seleccionado pizza vegetariana, seleccione un ingrediente:\n")
	ingredientes_vegetariana = int(input("(1) Pimiento\n(2) Rúcula\n\n"))
	if ingredientes_vegetariana == 1:
		print("\nConfirmación de pedido:\n\nPizza vegetariana\nMozarella, tomate y pimiento.")
	elif ingredientes_vegetariana == 2:
		print("\nConfirmación de pedido:\n\nPizza vegetariana\nMozarella, tomate y rúcula.")
	else:
		print("\nVuelva a realizar su pedido")	
elif pizza == 2:
	print("\nHa seleccionado no pizza vegetariana, seleccione un ingrediente:\n")
	ingredientes_vegetariana = int(input("(1) Jamón\n(2) Panceta\n\n"))
	if ingredientes_vegetariana == 1:
		print("\nConfirmación de pedido:\n\nPizza vegetariana\nMozarella, tomate y Jamón.")
	elif ingredientes_vegetariana == 2:
		print("\nConfirmación de pedido:\n\nPizza vegetariana\nMozarella, tomate y Panceta.")
	else:
		print("\nVuelva a realizar su pedido")
else:
	print("\nVuelva a realizar su pedido")
