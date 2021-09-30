"""
Este es un ejemplo de código organizado en archivo por separado,
para ser incluído y utilizado en otro
"""

import math


def main():
	print("Módulo de cálculo de superficies")


def calcularSuperficie(radio, k2 = 1):
	return math.pi * radio * radio * k2

def calcularPerimetroRect(l1, l2):
	return (l1 * 2) + (l2 * 2)


# Recordar que esta condición, permite evaluar si el script está siendo ejecutado de forma directa o no.
# De ser así, se indica por dónde debe comenzar la ejecución.
if (__name__ == "__main__"):
	main()
