
print("\nIngrese 3 numeros:")
n1 = int(input("Ingrese su primer número: "))
n2 = int(input("Ingrese su segundo número: "))
n3 = int(input("Ingrese su tercer número: "))

mayor = max(n1, n2, n3)
menor = min(n1, n2, n3)
medio = (n1 + n2 + n3) - mayor - menor

print("\nNúmero mayor: ",mayor,"\nNúmero medio: ",medio,"\nNúmero menor: ",menor)