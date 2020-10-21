#! /usr/bin/python3

### modulo de generación de números pseudo-aleatorios
### usando método congruencial mixto

import sys

from comun import precision

"""
TODO: el generador debe poder tomar valores para cada variable
ya no es fase de pruebas
"""
class Generador:
	def __init__(self, multiplicador, constante, modulo, semilla):
		#inician valores para el ejemplo
		"""self.multiplicador = 101
		self.constante = 221
		self.semilla = semilla
		self.actual = self.semilla
		self.modulo = 17001
		"""
		self.multiplicador = multiplicador
		self.constante = constante
		self.modulo = modulo
		self.semilla = semilla
		self.actual = self.semilla
		#terminan valores para el ejemplo
		self.contador = 0
		self.historico = []

	def actualizar_historico(self):
		self.historico.append([self.contador, self.actual, round(self.actual / self.modulo, precision)])

	def mostrar_historico(self):
		print("histórico, semilla: {}".format(self.semilla))
		for registro in self.historico:
			''' for campo in registro:
				print('{:.5f}'.format(campo), end='\t')
			'''
			for i in range(0, len(registro)):
				if i == 2:
					print('{:.5f}'.format(registro[i]), end='\t')
				else:
					print(registro[i], end='\t')
			print("")

	def str_historico(self):
		cadena = ""
		for registro in self.historico:
			cadena += "{}\t{}\n".format(registro[0], registro[2])
		return cadena

	def next(self):
		self.contador += 1
		siguiente = (self.multiplicador * self.actual + self.constante) % self.modulo
		self.actual = siguiente
		self.actualizar_historico()
		return siguiente

	def ciclo(self, n, mostrar=False):
		""" genera n números pseudoaleatorios en su historial
			se pueden visualizar o no mientras se generan
		"""
		for i  in range(0, n):
			if mostrar:
				print(self.next())
			else:
				self.next()

	def get_generacion(self):
		""" devuelve un arreglo de los números pseudoaleatorios
		generados
		"""

		if len(self.historico) == 0:
			raise Exception("generador vacío")
		generacion = []
		for i in range(0, len(self.historico)):
			generacion.append(self.historico[i][2])

		return generacion

	def detectar_ciclo(self):
		pass #muestra donde se presenta el ciclo.

	def is_vacio(self):
		return len(self.historico) == 0

	def reiniciar(self):
		self.historico = []
		self.contador = 0


if __name__ == '__main__':
	gen = None
	#si se llama este script con un argumento, se usa ese como semilla
	try:
		sys.argv[1]
	except IndexError:
		#semilla default = 17
		gen = Generador(17)
	else:
		gen = Generador(int(sys.argv[1]))
	gen.ciclo(325)
	gen.mostrar_historico()


	
