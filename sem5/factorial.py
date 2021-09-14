"""
Ejercicio simple repaso llamada a funciones con argumentos y cálculo de
factorial mediante 2 alternativas, recursividad (llamada de una función a si misma)
y ciclo reverso
"""

def solicitarNro():
	while(True):
		nro = int(input("Ingresar nro positivo o cero: "))
		if (nro >= 0):
			break
	return nro

def calcularFactorial(n):
	if (n <= 1):
		return 1
	else:
		return n * calcularFactorial(n - 1)


# Flujo principal de código
nroIngresado = solicitarNro()

factorial = calcularFactorial(nroIngresado)
print(factorial)

factorial = 1
for item in range(nroIngresado, 0, -1):
	factorial = factorial * item

print(factorial)
