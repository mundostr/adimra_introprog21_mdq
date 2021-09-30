# Librerías
# Nuevamente aprovechamos el import para incluir un archivo de configuración.
# De esta manera, organizamos todos los parámetros iniciales por separado.
import config


# Constantes y variables
RUTA = f"https://api.openweathermap.org/data/2.5/weather?q={config.CIUDAD}&appid={config.APPID}"


# Funciones
def mostrarMensaje(msj):
	print(msj)


# Flujo principal
# Recordar que esta condición, permite evaluar si el script está siendo ejecutado de forma directa o no.
# De ser así, se indica por dónde debe comenzar la ejecución.
if(__name__ == "__main__"):
	mostrarMensaje(RUTA)
