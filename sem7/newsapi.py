# Librerías y módulos internos
import requests
import na_config as cfg


# Declaraciones Funciones
def recuperar_contenido(direccion):
	try:
		solicitud = requests.get(direccion)
		
		if (solicitud.status_code == 200):
			return solicitud.json()
		else:
			print(solicitud.status_code)
			return False
	except requests.exceptions.RequestException as error:
		print(error)
		return False


# Flujo principal
def main():
	contenido = recuperar_contenido(cfg.URL_API)
	if (contenido == False):
		print("ERROR general")
	else:
		print(contenido)

if (__name__ == "__main__"):
	main()
