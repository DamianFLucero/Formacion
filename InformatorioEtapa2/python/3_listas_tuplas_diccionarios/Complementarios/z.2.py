
'''
z.2 Leer una frase y luego invierta el orden de las palabras en la frase. 
Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.
'''
frase = str(input("\nIngrese frase: "))

r = frase.split(" ")
u = reversed(r)

print("\n#############################################\n\nFrase:")
print(r)
print("\nFrase invertida:")
print(list(u))