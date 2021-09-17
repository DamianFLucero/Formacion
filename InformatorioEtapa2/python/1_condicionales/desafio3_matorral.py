

matorral = str(input("\nIngrese si/no, si posee, o no vegetación de tipo 'matorral': "))


if matorral == "si":
	print("\nDebe eliminar la vegetación de tipo 'matorral' para utilizar el fertilizante")
elif matorral == "no":
	producto = int(input("\nIngrese porcentaje de producto sobre hectarea: "))
	print("\n", producto,"%")
	if producto >= 10:
		print("\nPuede utilizar el producto")
	else:
		print("\nNo puede utilizar el producto") 
else:
	print("\nVuelva a intentarlo")
