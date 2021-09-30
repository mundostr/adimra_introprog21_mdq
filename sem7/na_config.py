"""
Archivo de configuración para ejemplo NewsAPI
https://newsapi.org/
"""


from os import getenv
from dotenv import load_dotenv
load_dotenv()


API_KEY = getenv("NEWSAPI_ID")
