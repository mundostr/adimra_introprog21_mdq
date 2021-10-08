"""
Ejemplo base de alcance (scope) de variables, que permite observar el comportamiento
de variables globales y locales.
"""


# Las variables declaradas a nivel raíz, serán GLOBALES
v1Global = 0


def fn1():
	# Las variables declaradas a nivel de función, serán LOCALES, solo estarán disponibles
	# dentro del ambito de esa función.
	ident = 1

	# En Python, indicaremos explícitamente con global, las variables globales que
	# deseamos utilizar en la función
	global v1Global

	for c in range(3):
		print(f"fn1 {ident}")
		ident += 1
		v1Global += 1


def fn2():
	# Las variables declaradas a nivel de función, serán LOCALES, solo estarán disponibles
	# dentro del ambito de esa función.
	ident = 2

	# En Python, indicaremos explícitamente con global, las variables globales que
	# deseamos utilizar en la función
	global v1Global

	print(f"fn2 {ident}")
	v1Global += 1


def main():
	# Simplemente realizamos algunas llamadas a las funciones declaradas,
	# para observar el comportamiento de las variables
	print("v1Global: ", v1Global)
	fn1()
	print("v1Global: ", v1Global)
	fn2()
	print("v1Global: ", v1Global)
	fn1()
	print("v1Global: ", v1Global)


if(__name__ == "__main__"):
	main()
