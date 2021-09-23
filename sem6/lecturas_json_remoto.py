"""
Prueba de lectura de archivo remoto en formato JSON
"""


# Librerías
# La librería requests es una de las habitualmente utilizadas en Python para obtener contenidos remotos
import requests


# Constantes y variables globales
# En este caso la ruta ya no será un archivo en la propia máquina (o en la red local),
# sino la URL de un contenido remoto
RUTA = "https://ergast.com/api/f1/current/driverStandings.json"


# Funciones
# Organizamos las tareas en funciones
def recuperar_contenido(direccion):
	# requests.get() nos permite fácilmente obtener un contenido remoto
	solicitud = requests.get(direccion)

	# Si la solicitud fue exitosa, status_code() retornará 200
	if (solicitud.status_code == 200):
		# Simplemente devolvemos el contenido recibido, convertido a JSON.
		return solicitud.json()
	else:
		return False

def extraer_podio(lista_posiciones):
	# Del contenido, obtenemos una parte, que se trata de una lista
	posiciones = lista_posiciones["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
	# y retornamos solo los 3 primeros items (el podio en este ejemplo)
	return posiciones[0:3]

def mostrar_podio(podio):
	# Intramos la lista
	for registro in podio:
		# Aprovechamos la macro f para armar fácilmente una cadena a mostrar
		# piloto = registro["Driver"]["givenName"] + " " + registro["Driver"]["familyName"]
		piloto = f'{registro["Driver"]["familyName"]}, {registro["Driver"]["givenName"]}'
		puntos = registro["points"]
		print(f"Piloto: {piloto} -> puntaje: {puntos}")


# Flujo principal
contenido = recuperar_contenido(RUTA)
if (contenido == False):
	print("La solicitud no se pudo procesar, por favor chequear la URL")
else:
	podio = extraer_podio(contenido)
	mostrar_podio(podio)
