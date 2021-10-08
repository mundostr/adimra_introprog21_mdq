"""
Introducción a POO (Programación Orientada a Objetos)
Ejemplo de declaración de clases.
Recordar que una clase es esencialmente un molde que define las características de un objeto.
"""


class Vehiculo():
	ctdVehiculosFlota = 0

	# Constructor
	# Las funciones dentro de clases son denominadas métodos.
	# En el caso de Python, el método __init__ es ejecutado automáticamente cada vez que
	# se crea un objeto de esa clase.
	def __init__(self, patente, marca, id):
		self.id = id
		self.marca = marca
		self.patente = patente
		Vehiculo.agregarVehiculo()
	
	# Método
	def agregarVehiculo(clase):
		clase.ctdVehiculosFlota += 1


def main():
	# Creamos 3 objetos de tipo Vehiculo, o dicho de otra forma,
	# instanciamos 3 vehículos.
	v1 = Vehiculo("ABC333AA", "Fiat", 16)
	v2 = Vehiculo("ABC333AB", "Volkswagen", 17)
	v3 = Vehiculo("ABC333AC", "Toyota", 15)


if (__name__ == "__main__"):
	main()
