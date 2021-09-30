"""
También podemos organizar todos los parámetros de inicialización en un archivo por separado.
En este caso aprovechamos las librerías os y dotenv para recuperar datos desde un archivo
de entorno (.env). Esta es una práctica cómoda y más eficiente al momento de guardar datos sensibles,
evitando que se deban listar manualmente en el código fuente principal.
"""

from os import getenv
from dotenv import load_dotenv
load_dotenv()


# Constantes y Variables
CIUDAD = "Rafaela"
APPID = getenv("OPEN_WEATHER_APPID")
