

#h. 	Construya un algoritmo que sume todos los elementos en posición par de una lista

L = [1,2,3,4,5,6,7,8,9,10]
contador = 0



for i in range(len(L)):
	if i % 2 == 0:
		contador += L[i]
	

print(contador)
		
