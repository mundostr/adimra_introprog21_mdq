"""
En este ejemplo, aprovechamos las definiciones cargadas en codigo_incluido.py.
Importamos el archivo completo con el alias fn, y utilizando la notación de puntos,
accedemos a las distintas funcionalidades declaradas (calcularPerimetroRect por ejemplo).
"""


#Librerías
import codigo_incluido as fn
# from codigo_incluido import calcularPerimetroRect


# Declaraciones ctes y variables


# Declaraciones Funciones
def main():
	# print(calcularSuperficie(3))
	print(fn.calcularPerimetroRect(2, 3))


# Flujo ppal
# Recordar que esta condición, permite evaluar si el script está siendo ejecutado de forma directa o no.
# De ser así, se indica por dónde debe comenzar la ejecución.
if (__name__ == "__main__"):
	main()
