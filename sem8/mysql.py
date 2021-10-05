# pip install pymysql
# pip install sqlalchemy

# Librerías
from sqlalchemy import create_engine


# Definiciones
SERVIDOR = "pad19.com"
USUARIO = "adimra"
CLAVE = "adm2021"
BBDD = "adimra_introprog21"
RUTA_SERVIDOR = f"mysql+pymysql://{USUARIO}:{CLAVE}@{SERVIDOR}/{BBDD}"


# Funciones
def conectarMysql():
	motorMysql = create_engine(RUTA_SERVIDOR, pool_recycle=3600)
	conn = motorMysql.connect()

	if (conn):
		return conn
	else:
		return False

def solicitarRegistros(conn, sql):
	resultado = conn.execute(sql)
	return resultado

def main():
	enlaceBd = conectarMysql()
	if (enlaceBd == False):
		print("Problemas al conectar con la bbdd")
	else:
		resultado = solicitarRegistros(enlaceBd, "SELECT piloto, puntos FROM clasificacion_f1 ORDER BY puntos DESC LIMIT 0, 3")
		for item in resultado:
			print(item)


# Main
if (__name__ == "__main__"):
	main()
