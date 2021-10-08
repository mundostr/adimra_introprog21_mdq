"""
En este ejemplo, vemos como podemos acceder cómodamente una base de datos SQL (Mysql)
mediante las librerías pymysql y sqlalchemy, para efectuar las operaciones CRUD
(Create, Read, Update, Delete), es decir, las 4 operaciones básicas en el almacenamiento persistente
"""


# Librerías
# pip install pymysql
# pip install sqlalchemy
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()


# Definiciones
SERVIDOR = getenv("SERVIDOR")
USUARIO = getenv("USUARIO")
CLAVE = getenv("CLAVE")
BBDD = getenv("BBDD")
RUTA_SERVIDOR = f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}/{BBDD}"


# Funciones
def conectarMysql():
	motorMysql = create_engine(RUTA_SERVIDOR, pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def consultar(conn, sql):
	try:
		resultado = conn.execute(sql)
		return resultado
	except:
		return False

def main():
	enlaceBd = conectarMysql()
	if (enlaceBd == False):
		print("Problemas al conectar con la bbdd")
	else:
		# Leer registros
		sql = """
		SELECT clasificacion_f1.piloto, escuderias_f1.nombre, clasificacion_f1.puntos
		FROM clasificacion_f1, escuderias_f1
		WHERE clasificacion_f1.id_escuderia = escuderias_f1.id
		ORDER BY puntos DESC"""
		resultado = consultar(enlaceBd, sql)
		
		if not (resultado):
			print("Error al realizar la consulta")
		else:
			for item in resultado:
				print(item)
		
		# # Cargar registro
		# sql = "INSERT into escuderias_f1 (nombre) VALUES('Aston')"
		# resultado = consultar(enlaceBd, sql)

		# # Actualizar registro
		# sql = "UPDATE escuderias_f1 SET nombre = 'Aston Martin' WHERE nombre = 'Aston'"
		# resultado = consultar(enlaceBd, sql)

		# # Borrar registro
		# sql = "DELETE FROM escuderias_f1 WHERE id = 7"
		# resultado = consultar(enlaceBd, sql)


# Main
if (__name__ == "__main__"):
	main()
