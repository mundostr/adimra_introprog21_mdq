"""
En este ejemplo simple, se ingresan de forma reiterada código, cantidad y precio de productos,
para calcular un totalGeneral.

Podemos observar la comodidad de while() cuando es necesario generar un ciclo indefinido, que
se mantendrá iterando hasta que se ingrese un 0 como código, allí mediante break se "romperá"
el ciclo y se imprimirá el total general calculado.
"""

print("1- Manzanas")
print("2- Peras")
print("3- Tomates")
print("4- Frutillas")
print("5- Kiwis")

totalGeneral = 0

# for i in range(100): # Ciclo finito
while(True): # Ciclo indefinido
	codigo = int(input("Ingresar código: "))
	if (codigo == 0): # código es igual a 0?
		break
	
	cantidad = int(input("Ingresar cantidad: "))
	precio = int(input("Ingresar precio: "))

	subtotal = cantidad * precio
	print(subtotal)
	print()

	# Acumulador para cálculo del total general
	totalGeneral = totalGeneral + subtotal

print(totalGeneral)
