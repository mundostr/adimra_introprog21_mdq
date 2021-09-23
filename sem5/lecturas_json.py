"""
Prueba de lectura de archivo local en formato JSON
"""


# Aprovechamos la librería JSON, incluida por defecto en la instalación de Python
import json


# Revisar SIEMPRE la ruta correcta, tener en cuenta cuál es el directorio raíz abierto
RUTA = "sem5/posiciones_f1_2021.json"

# Aprovechar el utf-8 para obtener correctamente acentos y otros caracteres.
archivo = open(RUTA, "r", encoding="utf-8")
# contenido = archivo.read()
# Un simple json.load(), permite recibir el contenido como diccionario.
contenido = json.load(archivo)

# A partir de allí, utilizando los keys correspondientes, podemos filtrar cualquier parte que nos interese
# MRData StandingsTable StandingsLists [0] DriverStandings []
posiciones = contenido["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
podio = posiciones[0:3]

for registro in podio:
	piloto = registro["Driver"]["familyName"]
	puntos = registro["points"]
	print(piloto, puntos)
