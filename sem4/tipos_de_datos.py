"""
Principales tipos de datos en Python3 (builtin datatypes).
Recordar que Python opera con tipado dinámico, esto significa que no obliga a especificar
el tipo de dato al momento de declarar una variable. No obstante, puede hacerse si se lo desea.
"""


# Numérico entero (int)
n1 = 10

# Numérico coma flotante (float)
n2 = 10.6

# Cadena de caracteres (str)
t1 = "Control"

# Booleano (bool), solo verdadero o falso, True / False
b1 = True

# Lista (list), es mutable
l1 = [10, 5, 8]

# Tupla (tuple), es inmutable
tp1 = (10, 5, 8)

# Rango (range)
r1 = range(5)
for ciclo in r1:
	print(ciclo)


# Obtener el tipo de dato de una variable
b2 = False
print(type(b2)) # devolverá <class 'bool'>


# Convertir de un tipo a otro, aplicando funciones predefinidas con el nombre de cada tipo de dato
n3 = float(n1)
print(n3) # imprimirá 10.0


# Las mismas funciones de conversión, pueden utilizarse para especificar el tipo de dato
# aunque recordemos, no es imprescindible hacerlo
n4 = int(23.5)
print(n4) # n4 será int, por lo tanto se imprimirá 23
