

#i. Elabore un programa que dada una lista de 15 elementos, copie en otra lista los elementos pares multiplicados por 2.


lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pares = []

for i in lista:
	if i % 2 == 0:
		r = i * 2
		pares.append(r)

print(pares)

