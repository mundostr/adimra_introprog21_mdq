"""
Cálculo base de promedio simple (suma de items / cantidad)
"""

datos = [15, 15, 10, 20, 20]

# Opción 1: calcular total en el ciclo, y luego dividir por cantidad
total = 0
promedio = 0
for item in datos:
  total = total + item
promedio = total / len(datos)
print(promedio)

# Opción 2: acumular directamente promedio en el ciclo, sumando el valor del item ya dividido
promedio = 0
for item in datos:
  promedio = promedio + item / len(datos)
print(promedio)
