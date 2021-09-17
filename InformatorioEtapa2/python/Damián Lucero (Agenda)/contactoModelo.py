from acDB import DB 



class Persona:
	__DB = DB(name = 'ContactosDB')
	__tableName = 'Contactos'

	def __init__(self,Telefono,Nombre,Email = None):
		self.__Telefono = Telefono
		self.__Nombre = Nombre
		self.__Email = Email

	@classmethod
	def mostrar(cls):
		query = "SELECT * FROM "+Persona.__tableName
		return Persona.__DB.run(query)

	@classmethod
	def buscar(cls, Telefono):
		query = "SELECT * FROM "+Persona.__tableName+" WHERE Telefono = ?"
		values = (Telefono)
		return Persona.__DB.run(query, values)

	def agregar(self):
		query = "INSERT INTO "+Persona.__tableName+" (Telefono,Nombre,Email) VALUES (?,?,?)"
		values = (self.__Telefono,self.__Nombre,self.__Email)
		Persona.__DB.run(query,values)
	
	def modificar(Nombre, Email, Telefono):
		query = "UPDATE "+Persona.__tableName+" SET Nombre = ?, Email = ? WHERE Telefono = ?"
		values = (Nombre, Email, Telefono)
		Persona.__DB.run(query, values)

	def eliminar(Telefono):
		query = "DELETE FROM "+Persona.__tableName+" WHERE Telefono = ?"
		values = (Telefono)
		Persona.__DB.run(query, values)
	

