#! /usr/bin/python3

### modulo de generación de números pseudo-aleatorios
### usando método congruencial mixto

import sys

class Generador:
	def __init__(self, semilla):
		#inician valores para el ejemplo
		self.multiplicador = 101
		self.constante = 221
		self.semilla = semilla
		self.actual = self.semilla
		self.modulo = 17001
		#terminan valores para el ejemplo
		self.contador = 0
		self.historico = []

	def actualizar_historico(self):
		self.historico.append([self.contador, self.actual, self.actual / self.modulo])

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
	def next(self):
		self.contador += 1
		siguiente = (self.multiplicador * self.actual + self.constante) % self.modulo
		self.actual = siguiente
		self.actualizar_historico()
		return siguiente


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
	for i in range(0, 65):
		print(gen.next())
	gen.mostrar_historico()


	
