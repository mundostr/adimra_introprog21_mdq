"""
Los condicionales comprenden otro de los elementos básicos de cualquier lenguaje, permiten evaluar una condición
y ejecutar selectivamente un código u otro de acuerdo a si esta condición es válida o no.
"""

valorInicial = 16
LIMITE = 30


# Esta es la expresión más simple de un condicional,
# si valorInicial es mayor a LIMITE, se imprimirá el mensaje, caso contrario no se hará nada
if (valorInicial > LIMITE):
	print("El valor es mayor al límite")


# Esta es la segunda expresión habitual de un condicional,
# si valorInicial es mayor a LIMITE, se imprimirá un mensaje, caso contrario se imprimirá otro
if (valorInicial > LIMITE):
	print("El valor es mayor al límite")
else: # sino
	print("El valor no es mayor al límite")


# También se pueden evaluar condiciones en cadena, solo cuando las previas son falsas
# En este caso, si valorInicial es mayor a LIMITE, se imprimirá el primer mensaje y no se seguirán
# evaluando las condiciones debajo.
if (valorInicial > LIMITE):
	print("El valor es mayor al límite")
elif (valorInicial < LIMITE): # sino si
	print("El valor es menor al límite")
else: #sino
	print("El valor es igual al límite")


# Los condicionales pueden aplicarse también sobre conjuntos de datos
listaPersonas = ["Adrián", "Gustavo", "María", "Alicia", "Carolina"]
personaBuscada = "Carolina"
personaBuscada2 = "Carlos"

if personaBuscada in listaPersonas:
	print(personaBuscada, "está en la lista")

if not personaBuscada2 in listaPersonas:
	print(personaBuscada2, "no está en la lista")
