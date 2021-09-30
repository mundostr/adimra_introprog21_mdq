# Librerías y módulos internos
import requests
import na_config as cfg


# Declaraciones constantes y variables
CRITERIO = "tesla"
FECHA = "2021-08-29"
URL_API = f"https://newsapi.org/v2/everything?q={CRITERIO}&from={FECHA}&sortBy=publishedAt&apiKey={cfg.API_KEY}"


# Declaraciones Funciones
def recuperar_contenido(direccion):
	print(direccion)
	solicitud = requests.get(direccion)

	if (solicitud.status_code == 200):
		return solicitud.json()
	else:
		return False

def main():
	contenido = recuperar_contenido(URL_API)
	if (contenido == False):
		print("ERROR al recuperar contenidos desde newsapi")
	else:
		print(contenido)


# Flujo principal
if (__name__ == "__main__"):
	main()
