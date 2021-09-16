"""
Muestra de lectura de CSV con headers (primer línea con nombres de campo)
Abrimos un archivo de ciudades del mundo.
En la apertura del archivo, se indica el tipo de encoding (UTF-8) para leer correctamente.
readlines() permite fácilmente leer el contenido línea a línea, pasándolo a una lista.
Iteramos la lista (contenido) en busca de una ciudad determinada, para mostrar solo esos datos.
"""


import csv


RUTA = "practicas/ciudades_del_mundo.csv"
CIUDAD = "Balcarce"


# archivo = open(RUTA, "r", encoding="UTF-8")
# contenido = archivo.readlines()

# for registro in contenido:
# 	# La cláusula in, nos permite buscar fácilmente un contenido dentro de un registro
# 	# pero CUIDADO, puede haber múltiples coincidencias.
# 	if (CIUDAD in registro):
# 		print(registro)
		
# archivo.close()

archivo = csv.reader(open(RUTA, "r", encoding="utf8"))

for registro in archivo:
	if (CIUDAD in registro):
		datos = registro

print("Ciudad:", CIUDAD)
print("Latitud:", datos[2])
print("Longitud:", datos[3])
