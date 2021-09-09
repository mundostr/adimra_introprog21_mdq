LIMITE = 15


lecturas = [23, 22, 21, 22, 23, 24, 25, 24 ]


def controlLimite(lectura):
	return True if (lectura > LIMITE) else False


# Filter permite aplicar una función a todos los items de una colección.
# En este ejemplo aplicamos controlLimite(), que devuelve True o False para cada item
# según supere o no LIMITE. Convertimos el resultado a una lista con list()

lecturasFiltradas = list(filter(controlLimite, lecturas))

print(lecturas)
print("Valores fuera de rango:", len(lecturasFiltradas))
