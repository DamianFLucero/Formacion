usuario_c = "admin"
ctrs = 1234
a = 0
contador = 5

usuario = input("\n\nIngrese su usuario: ")
while usuario != usuario_c:
	print("\nUsuario inexistente vuelva a intentarlo")
	break
else:
	print("\nBienvenido", usuario_c)
	ing_cts = int(input("\nIngrese su contraseña: "))
	if usuario == usuario_c and ing_cts == ctrs:
		print("\n\n###################\nContraseña correcta\n###################")
	elif ing_cts != ctrs:
		while a < 4:
			a = a + 1
			contador = contador - 1
			print("\nContraseña Inválida, restan", contador, "intentos")
			ing_cts = int(input("Ingrese su contraseña: "))
		print("\n################\nCuenta Bloqueada\n################")