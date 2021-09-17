


#17) Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades 
#si este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:

#Tiempo								Utilidad

#Menos de 1 año						5% del salario
#Más de 1 año y hasta 2 años		7% del salario
#Más de 2 años y hasta 5 años 		10% del salario
#Más de 10 años						20% del salario


print("\n\nReparto anual de utilidades:")

ant = int(input("Ingrese antigüedad del trabajador: "))
sal = float(input("Ingrese salario mensual: "))

if ant <= 1:
	x = sal*5/100
	print("\n#Utilidad mensual: ", x)
	print("#Suma de utilidades anual: ", x*12)
elif ant <= 2:
	x = sal*7/100
	print("\n#Utilidad mensual: ", x)
	print("Suma de utilidades anual: ", x*12)
elif ant <= 5:
	x = sal*10/100
	print("\n#Utilidad mensual: ", x)
	print("Suma de utilidades anual: ", x*12)
else:
	x = sal*20/100
	print("\n#Utilidad mensual: ", x)
	print("Suma de utilidades anual: ", x*12)





