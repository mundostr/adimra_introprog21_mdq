"""
Lectura de datos JSON desde el servicio OpenWeather
Este ejemplo es similar a lecturas_json_remoto, pero agrega el uso de un token (credencial)
que debe enviarse en este caso como parámetro en la misma URL, mediante appid
"""

import requests


# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
CIUDAD = "Balcarce"
APPID = "b07cceb706b36724ddaa2614cdb76af4"
# Una vez más, aprovechando la macro f, armamos fácilmente la ruta completa del contenido que queremos recuperar
RUTA = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&appid={APPID}"


# Misma función utilizada en el ejemplo anterior
def recuperar_contenido(direccion):
	solicitud = requests.get(direccion)

	if (solicitud.status_code == 200):
		return solicitud.json()
	else:
		return False

	
# Flujo principal
contenido = recuperar_contenido(RUTA)
if (contenido == False):
	print("La solicitud no se pudo procesar, por favor chequear la URL")
else:
	print(contenido)
