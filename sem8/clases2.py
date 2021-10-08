"""
Introducción a POO (Programación Orientada a Objetos)
Ejemplo de declaración de clases que HEREDAN características de otras,
Perro y Gato en este caso, de Mascota.
Recordar que una clase es esencialmente un molde que define las características de un objeto.
"""


class Mascota:
	def __init__(self, nombre, raza):
		self.nombre = nombre
		self.raza = raza
	
	def mostrarNombre(self):
		print(f"La mascota se llama {self.nombre}")


class Perro(Mascota):
	def ladrar(self):
		print(f"{self.nombre} ladra")


class Gato(Mascota):
	def maullar(self):
		print(f"{self.nombre} maulla")


def main():
	# Instanciamos 2 objetos, un Perro y un Gato, pasando nombre y raza para inicialización
	# Ambos podrán mostrar su nombre, aunque este método no se declara ni en Perro ni en Gato,
	# pero se hereda de Mascota, pudiendo usarse con cualquier objeto de tipo Perro o Gato.
	
	# El perro podrá ladrar (cuenta con un método ladrar declarado)
	# pero no podrá maullar.
	perro = Perro("Batuque", "Galgo")
	perro.mostrarNombre()
	perro.ladrar()

	# Inversamente, el gato podrá maullar (cuenta con un método maullar declarado)
	# pero no podrá ladrar.
	gato = Gato("Travieso", "Siames")
	gato.mostrarNombre()
	gato.maullar()


if __name__ == '__main__':
	main()
