"""
Archivo de configuración para ejemplo NewsAPI
https://newsapi.org/
"""


from os import getenv
from dotenv import load_dotenv
load_dotenv()


API_KEY = getenv("NEWSAPI_ID")

# Declaraciones constantes y variables
PAIS = "ar"
CRITERIO = "tesla"
FECHA = "2021-08-30"
CATEGORIA = "sports"
# URL_API = f"https://newsapi.org/v2/everything?q={CRITERIO}&from={FECHA}&sortBy=publishedAt&apiKey={cfg.API_KEY}"
URL_API = f"https://newsapi.org/v2/top-headlines?country={PAIS}&category={CATEGORIA}&apiKey={API_KEY}"
