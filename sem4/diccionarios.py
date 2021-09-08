"""
Primer práctica de diccionarios.
Un diccionario de Python, a diferencia de listas y tuplas, no se gestiona mediante índices
sino mediante claves (keys), que identifican cada item que contiene.

Las claves se expresan siempre entre comillas, y un : las separa del valor, que puede ser de
cualquier tipo (str, int, float, bool, etc). Así el diccionario se va armando con diversos pares key:valor.

Como se verá más adelante, los diccionarios serán muy útiles para gestionar datos
en formato JSON (Javascript Object Notation), un formato muy standard actualmente para el intercambio de datos.
"""

datosPersonales = {
	"nombre": "Carlos",
	"nacionalidad": "argentino",
	"activo": False, # bool o booleano
	"saldo": 1000.50,
	"apellido": "Perren",
}


# Imprimirá el diccionario completo como objeto
print()
print("Diccionario completo:", datosPersonales)

print()
# Imprimirá solo el valor de los key apellido y saldo
print("Key apellido:", datosPersonales["apellido"])
print("Key saldo:", datosPersonales["saldo"])
