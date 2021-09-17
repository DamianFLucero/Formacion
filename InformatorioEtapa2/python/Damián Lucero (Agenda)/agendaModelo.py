from acDB import DB 



class AgenMod:
	__DB = DB(name = 'ContactosDB')
	__tableName = 'Agenda'

	def __init__(self,Usuario,id = None):
		self.Usuario = Usuario
		self.id = id

	@classmethod	
	def consultar(self):
		query = "SELECT COUNT(*) FROM Agenda"
		return AgenMod.__DB.run(query)

	def crearAgenda(self):
		query = "INSERT INTO "+AgenMod.__tableName+" (Usuario,id) VALUES (?,1)"
		values = (self.Usuario)
		AgenMod.__DB.run(query,values)

	@classmethod
	def nombreAgenda(self):
		query = "SELECT Usuario FROM Agenda"
		return AgenMod.__DB.run(query)

	def modificar(self):
		query = "UPDATE "+AgenMod.__tableName+" SET Usuario = ? WHERE id = 1"
		values = (self.Usuario)
		AgenMod.__DB.run(query, values)

	@classmethod	
	def eliminar(self):
		query = "DELETE FROM "+AgenMod.__tableName
		return AgenMod.__DB.run(query)

	@classmethod	
	def eliminarCont(self):
		query = "DELETE FROM Contactos"
		return AgenMod.__DB.run(query)

		
			