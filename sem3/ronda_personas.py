# Primer versión ejercicio ronda personas

LIMITE_CUENTA = 100
LIMITE_PERSONAS = 10


cuenta = 0
persona = 0
sentido = "horario"


for ciclo in range(LIMITE_CUENTA):
	## Control de cuenta, persona
	cuenta = cuenta + 1 # contador

	if (sentido == "horario"):
		persona = persona + 1
		if (persona > LIMITE_PERSONAS):
			persona = 1
	else:
		persona = persona - 1
		if (persona < 1):
			persona = LIMITE_PERSONAS

	print("En sentido", sentido, "la persona", persona, "dice", cuenta)


	# Control de perfectamente divisible por 8
	if (cuenta % 8 == 0):
		if (sentido == "horario"):
			sentido = "antihorario"
		else:
			sentido = "horario"
	

	# Control de perfectamente divisible por 11
	if (cuenta % 11 == 0):
		if (sentido == "horario"):
			persona = persona + 1
			if (persona > LIMITE_PERSONAS):
				persona = 1
		else:
			persona = persona - 1
			if (persona < 1):
				persona = LIMITE_PERSONAS
	