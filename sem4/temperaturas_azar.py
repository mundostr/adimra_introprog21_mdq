"""
Generar una colección de 50 lecturas al azar, en un rango de 0 a 100 grados, utilizando la librería random.
Completar una segunda lista con las lecturas de la colección anterior, que superen un determinado límite.
"""

import random


LECTURAS = 50
TEMP_MIN = 0
TEMP_MAX = 100
TEMP_LIMITE = 95

# Generamos un par de listas vacias
listaTemps = []
listaTempsFRango = []


# Habilitamos un ciclo finito para la cantidad de lecturas solicitada
for ciclo in range(LECTURAS):
	# Generamos número al azar
	lectura = random.randint(TEMP_MIN, TEMP_MAX)

	# Agregamos el número a la lista de temperaturas
	listaTemps.append(lectura)

	if (lectura > TEMP_LIMITE):
		# Agregamos el número a la lista fuera de rango, solo si supera el límite
		listaTempsFRango.append(lectura)


# Mostramos los resultados. len() nos permite conocer la cantidad de items en la lista
print(listaTemps)
print(len(listaTemps))
print()

listaTemps.sort()
print(listaTemps)
print()

print(listaTempsFRango)
print(len(listaTempsFRango))
