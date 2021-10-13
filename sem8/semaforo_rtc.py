"""
Ejercicio base de semáforo para comenzar a analizar el control de tiempos,
la ejecución síncrona / asíncrona y las alternativas de multitarea.

En este primer ejemplo solo se realiza el ciclo esencial típico de un semáforo.
"""


# Librerías
import datetime
from time import sleep


# Definiciones
LUCES = [
	{ "nombre": "________RJO________", "color": "\x1b[0;30;41m", "demora": 5 },
	{ "nombre": "________VDE________", "color": "\x1b[0;30;42m", "demora": 5 },
	{ "nombre": "________AMA________", "color": "\x1b[3;30;43m", "demora": 1 },
	{ "nombre": "________APA________", "color": "\x1b[0m", "demora": 1 }
]
MODO_DIURNO_INI = datetime.time(6, 0, 0)
MODO_DIURNO_FIN = datetime.time(23, 59, 0)


# Main
def main():
	luzActiva = 0
	modo = "INICIAL"

	while(True):
		# Control horario
		if (MODO_DIURNO_INI <= datetime.datetime.now().time() <= MODO_DIURNO_FIN):
			modo = "DIURNO"
		else:
			modo = "NOCTURNO"

		# Modo diurno
		if (modo == "DIURNO"):
			print(LUCES[luzActiva]["color"] + LUCES[luzActiva]["nombre"] + "\x1b[0m")
			sleep(LUCES[luzActiva]["demora"])

			luzActiva = luzActiva + 1
			if (luzActiva == len(LUCES) - 1):
				luzActiva = 0
				print()
		
		# Modo nocturno
		if (modo == "NOCTURNO"):
			print(LUCES[luzActiva]["color"] + LUCES[luzActiva]["nombre"] + "\x1b[0m")
			sleep(LUCES[luzActiva]["demora"])

			if (luzActiva == 2):
				luzActiva = 3
			else:
				luzActiva = 2


if (__name__ == "__main__"):
	main()
