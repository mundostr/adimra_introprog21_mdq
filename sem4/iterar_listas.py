# Declaración de una matriz tipo lista, conteniendo números enteros
listaEnteros = [10, 20, 50, 15, 12, 80, 33]

# Accedemos a los items de una lista mediante un índice que SIEMPRE inicia en 0
print("Primer item:", listaEnteros[0]) # imprimirá 10
print("Tercer item:", listaEnteros[2]) # imprimirá 50

# De similar manera, el último item de una lista SIEMPRE se identifica con el índice -1
print("Ultimo item:", listaEnteros[-1]) # imprimirá 33


# Podemos iterar (recorrer) fácilmente la lista, utilizando la sintaxis del for
print()
for item in listaEnteros:
	print(item)

# También podemos iterar solo una parte de la lista, especificando en el for
# el índice de inicio y fin [0:3]. El de fin NO es incluído, por lo cual 0:3
# significa que se tomarán los items 0, 1 y 2.
sumatoria = 0
for item in listaEnteros[0:3]:
	sumatoria = sumatoria + item
print()
print("Sumatoria de los 3 primeros items:", sumatoria)

# Con el comando copy() podemos copiar de forma total o parcial una lista en otra
listaEnteros2 = listaEnteros.copy()
print()
print("listaEnteros2:", listaEnteros2) # listaEnteros2 será igual a listaEnteros

listaEnteros3 = listaEnteros[0:4].copy()
print()
print("listaEnteros3:", listaEnteros3) # listaEnteros3 contendrá solo los 4 primeros items de listaEnteros
