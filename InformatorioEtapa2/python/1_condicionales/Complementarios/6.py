

sueldo = float(input("\nPara determinar premio, ingrese monto del sueldo: "))

if sueldo <= 6000:
	total = sueldo*15/100 + sueldo
	print("\nSueldo actual: ", sueldo,"\nAumento: 15%\nTotal con premio: ", total)
elif sueldo <= 7900:
	total = sueldo*10/100 + sueldo
	print("\nSueldo actual: ", sueldo,"\nAumento: 10%\nTotal con premio: ", total)	
elif sueldo < 12000:
	total = sueldo*6/100 + sueldo
	print("\nSueldo actual: ", sueldo,"\nAumento: 6%\nTotal con premio: ", total)
else:
	print("\nSin bonificación\nTotal: ", sueldo)	