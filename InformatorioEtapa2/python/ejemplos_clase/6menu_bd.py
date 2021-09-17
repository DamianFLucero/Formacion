import pyodbc


def connect():
	servidor = 'DESKTOP-QBFQQ6B\SQLEXPRESS'
	nombre_bd = 'Personas'
	#nombre_usuario = ''
	#password = ''
	conexion = None

	try:
		conexion = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};"
								  "Server="+servidor+";"
								  "DATABASE="+nombre_bd+";"
								  "Trusted_Connection=yes;")
		# OK! conexión exitosa
		#print("Funciona")
	except Exception as e:
		# Atrapar error
		print("Ocurrió un error al conectar a SQL Server: ", e)
	return conexion

#-----------FUNCIONES---------
#Buscar persona / Mostrar todo
def select(conn,q,v=None):
	c = conn.cursor()
	if v:
		c.execute(q,v)
	else:	
		c.execute(q)
	for r in c:
		print(r)

#Cargar persona
def insert(conn,q,v):
	c = conn.cursor()
	c.execute(q,v)
	conn.commit()	

#Modificar persona
def update(conn,q,v):
	c = conn.cursor()
	c.execute(q,v)
	conn.commit()

#Borrar persona
def delete(conn,q):
	c = conn.cursor()
	c.execute(q)
	conn.commit()	

#-----------MENU---------

def menu():
	print("\nHola, seleccione:")	
	conn = connect()
	while True:
		print("\n1 Buscar persona\n2 Cargar persona\n3 Mostrar todo\n4 Borrar persona\n5 Modificar persona\n6 Salir\n")
		op = input()
		if op == "1":
			#Buscar persona
			dni = int(input("Ingrese el DNI de la persona que quiere buscar: "))
			consulta = "SELECT * FROM Persona WHERE dni = ?"
			valores = (dni)
			select(conn,consulta,valores)
		elif op == "2":
			#Cargar persona
			print("Ingrese los datos de la persona")
			dni = int(input("DNI: "))
			nombre = input("Nombre: ")
			apellido = input("Apellido: ")
			direccion = input("Dirección: ")
			edad = int(input("Edad: "))
			profesion = input("Profeesión: ")
			consulta = "INSERT INTO persona (dni,nombre,apellido,direccion,edad,profesion) VALUES (?,?,?,?,?,?)"
			valores = (dni,nombre,apellido,direccion,edad,profesion)
			insert(conn,consulta,valores)	
		elif op == "3":
			#Mostrar todo
			consulta = "SELECT * FROM Persona"
			select(conn,consulta)
		elif op == "4":
			#Borrar persona
			borrar = int(input("Ingrese DNI de la persona que desea borrar: "))
			consulta = f"DELETE FROM Persona WHERE persona.dni = {borrar}"
			delete(conn,consulta)
			consulta="SELECT * FROM Persona"
			select(conn,consulta)
		elif op == "5":
			#Modificar persona
			dni = int(input("Ingrese DNI de la persona que desea modificar: "))
			dato = input("Ingrese el dato (dni,nombre,apellido,direccion,edad,profesion) que desea modificar: ")
			nuevo = input("Ingrese nuevo dato: ")
			consulta = "UPDATE Persona SET " + dato + "= ? where dni = ?"
			valores = (nuevo,dni)
			update(conn,consulta,valores)
		else:
			#Salir
			print("Adios")
			break
	conn.close()

menu()