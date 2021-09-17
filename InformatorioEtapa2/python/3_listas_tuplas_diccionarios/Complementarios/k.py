

#k. 	Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.

lista_1 = ['gato', 'perro', 'caballo', 'vaca', 'tortuga']
lista_2 = ['jabalí', 'vaca', 'gato', 'liebre', 'perro', 'lechuza']


lista_nueva = list(set(lista_1 + lista_2))

print(lista_nueva)
