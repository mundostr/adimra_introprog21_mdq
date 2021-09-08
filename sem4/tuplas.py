# Una tupla se maneja de manera similar a una lista, accediendo sus items mediante índices
# Recordar que el índice SIEMPRE inicia en 0
tupla1 = ("Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom")

print("Cuarto item de la tupla:", tupla1[3]) # imprimirá Jue

# pero tiene una diferencia fundamental, es INMUTABLE
# esto significa que no podremos modificar, agregar o quitar items una vez definida.

# Esta instrucción generará un error
# tupla1.append("Otro día")

# Todo lo relacionado a iteracciones se mantiene
print()
for item in tupla1:
	print(item)

# Cuando iteramos una parte de una tupla, no necesitamos comenzar desde cero
# En este caso vamos del índice 4 al 7 (recordar el que último NO se incluye),
# por lo que se listarán los índices 4, 5 y 6 = Vie, Sab y Dom
print()
for item in tupla1[4:7]:
	print(item)
