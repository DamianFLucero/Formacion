

tupla = ('*Plástico','*Desechos industriales','*Pesticidas agrícolas','*Vertido accidental de petróleo','*Sedimentación por deforestación')

salida = True



while salida == True:
	juego = int(input("\nPara conocer una forma de contaminación del agua apretá un número: "))
	if (juego-1) >= 0 and (juego-1) < len(tupla):
		print(tupla[juego-1])
		pregunta = int(input("\n\n¿Continuar? si(1) no(0): "))
		if pregunta == 0:
			salida = False
		else:
			salida = True
	else:
		print("*Error")
else:
	print('\n###\nFIN\n###')