# Primer versión ejercicio ronda personas
"""
Primer versión ejercicio ronda personas, con defectos de código pero cumpliendo con las funcionalidades solicitadas.
El objetivo es que una ronda de 10 personas cuente hasta 100, uno a uno.
1) Inicia en sentido horario
2) Si la cuenta es perfectamente divisible por 8, la ronda debe cambiar de sentido.
3) Si la cuenta es perfectamente divisible por 11, se debe mantener el sentido pero saltar la siguiente persona.
"""

LIMITE_CUENTA = 100
LIMITE_PERSONAS = 10


cuenta = 0
persona = 0
sentido = "horario"


for ciclo in range(LIMITE_CUENTA):
	## Control de cuenta, persona
	# Incrementamos la cuenta general
	cuenta = cuenta + 1 # contador

	# De acuerdo al sentido de giro actual, incrementamos o decrementamos el indicador de persona,
	# y además verificamos que este indicador nunca se exceda de los límites de la ronda.
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
	# Si es perfectamente divisible por ocho, simplemente invertimos el sentido de giro
	if (cuenta % 8 == 0):
		if (sentido == "horario"):
			sentido = "antihorario"
		else:
			sentido = "horario"
	

	# Control de perfectamente divisible por 11
	# Si es perfectamente divisible por 11, volvemos a controlar el sentido de giro
	# para incrementar o decrementar otra vez el indicador de persona, y así saltar una.
	if (cuenta % 11 == 0):
		if (sentido == "horario"):
			persona = persona + 1
			if (persona > LIMITE_PERSONAS):
				persona = 1
		else:
			persona = persona - 1
			if (persona < 1):
				persona = LIMITE_PERSONAS
	