"""
Exceptions usadas en el programa
"""
class BadAlfaException(Exception):
	""" Alfa debe de ser un número flotante
	siempre menor a 1.0, si no es así,
	se envia esta exception
	"""
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value

	def __str__(self):
		return "Alfa debe ser un valor menor a 1.0, alfa es {}".format(
			self.value)
