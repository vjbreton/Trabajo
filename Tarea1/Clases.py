class Jugador:
	id_jugador = 1

	def __init__(self, nombre, contraseña):
		self._id = Jugador.id_jugador
		self.nombre = nombre
		self.contraseña = contraseña
		self.dinero = 1000
		self.medallas = []
		self.prograbolas = 10



class Entrenador:

	def __init__(self, nombre, equipo):
		self.nombre = nombre



class Progradex:

	def __init__(self):
		self.vistos = []
		self.capturados = []


