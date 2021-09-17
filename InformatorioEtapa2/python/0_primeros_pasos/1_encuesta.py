total_preguntas = int(input("Ingrese total de preguntas "))
respuestas_correctas = int(input("Ingrese total de respuestas correctas "))

resto = respuestas_correctas*100/ total_preguntas

if resto >= 90:
	print("EXELENTE")
elif resto >= 70:
	print("BUENO")
elif resto >= 60:
	print("APROBADO")
else:
	print("NO ALCANZÓ")