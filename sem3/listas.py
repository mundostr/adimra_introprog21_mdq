"""
Primer interpretación de colecciones de datos.
Creación de una lista vacío y agregado de items con método append() en base a ingreso desde consola.
A medida que se obtienen los items, se cotejan contra una referencia para detectar cuál es el mayor.
"""

CTD_NROS = 5

mayor = -9999
listaDatos = [] # Lista vacía

for ciclo in range(CTD_NROS):
	ingreso = int(input("Ingresar nro:"))
	listaDatos.append(ingreso)

	if (ingreso > mayor):
		mayor = ingreso

print(mayor)
print(listaDatos)
