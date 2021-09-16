"""
Manejo de archivos locales en modos normales:

r = read (solo lectura)
w = write (escritura, trunca el archivo)
a = append (escritura, agrega al archivo)
"""


import random


def mostrar_contenidos(ruta):
	archivo = open(ruta, "r")
	listaDatos = archivo.read().split(",")
	archivo.close()

	# Salida lista recuperada original
	print(listaDatos)

	# Iteración de la lista para convertir todos los items a enteros.
	# Veremos más adelante otras alternativas.
	# for indice, dato in enumerate(listaDatos):
	for i in range(len(listaDatos)):
		listaDatos[i] = int(listaDatos[i])

	listaDatos.sort(reverse=True)

	# Salida lista ordenada
	print(listaDatos)

def subir_contenidos(ruta, contenido, modo):
	archivo = open(ruta, modo)
	archivo.write(contenido)
	archivo.close()
	
	print("Datos registrados:", contenido)


# MAIN, CODIGO PRINCIPAL
RUTA = "sem5/datos.csv" # recordar ajustar esta ruta para localizar el archivo
# mostrar_contenidos(RUTA)

RUTA_ALTERNATIVA = "sem5/datos_carga.csv"
datos = []
# Generamos 15 lecturas al azar para armar una lista
for i in range(15):
	# Agregamos cada lectura como nuevo item de la lista, convirtiéndola a una cadena con str()
	datos.append(str(random.randint(0, 100)))

# join nos permite fácilmente unir todos los elementos de una lista o tupla en una única cadena,
# utilizando como separador el que indiquemos al inicio (la coma en este caso).
datosComoTexto = ",".join(datos)
print("Datos a registrar:", datosComoTexto)

# Si el archivo en RUTA_ALTERNATIVA no existe, lo creará y cargará los contenidos,
# caso contrario reemplazará los contenidos actuales por los nuevos.
subir_contenidos(RUTA_ALTERNATIVA, datosComoTexto, "w")
