usuario_c = "admin"
ctrs = 1234

usuario = input("\n\nIngrese su usuario: ")
while usuario != usuario_c:
	print("\nUsuario inexistente vuelva a intentarlo")
	break
else:
	print("\nBienvenido", usuario_c)
	ing_cts = int(input("\nIngrese su contraseña: "))
	if ing_cts == ctrs:
		print("\n\n###################\nContraseña correcta\n###################")
	elif ing_cts != ctrs:
		while ing_cts != ctrs:
			print("\nContraseña incorrecta")
			ing_cts = int(input("Ingrese su contraseña: "))
		print("\n###################\nContraseña correcta\n###################")