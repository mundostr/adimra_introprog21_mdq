"""
El uso de librerías es una práctica muy standard en todos los lenguajes de programación actuales.
En el caso de Python, la cláusula import permite insertar la librería que se desee,
para comenzar a utilizar sus métodos.
"""

# Se importa la librería random, incluída en la instalación predeterminada de Python3
# En este caso, se importa de forma completa, es decir, todos sus métodos estarán disponibles.
import random

# Se realiza el llamado a uno de los métodos (randint), que permite generar un número entero al azar.
# También se podrían utilizar otros declarados en la librería, como randrange o randbytes por ejemplo.
nro = random.randint(0, 100)

print("Entero generado al azar:", nro)
