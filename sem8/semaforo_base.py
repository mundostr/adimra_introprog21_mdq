"""
Ejercicio base de semáforo para comenzar a analizar el control de tiempos,
la ejecución síncrona / asíncrona y las alternativas de multitarea.

En este primer ejemplo solo se realiza el ciclo esencial típico de un semáforo.
"""


# Librerías
import time


# Definiciones
LUCES = [
	{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 5 },
	{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 1 },
	{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 5 }
]


# Main
def main():
	luzActiva = 0

	while(True):
		print(LUCES[luzActiva]["color"] + LUCES[luzActiva]["nombre"] + "\x1b[0m")
		time.sleep(LUCES[luzActiva]["demora"])

		luzActiva = luzActiva + 1
		if (luzActiva == len(LUCES)):
			luzActiva = 0
			print()



if (__name__ == "__main__"):
	main()
