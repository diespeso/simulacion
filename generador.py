#! /usr/bin/python3

### modulo de generación de números pseudo-aleatorios
### usando método congruencial mixto

import sys

from comun import precision

class AnalizadorGenerador:
	def __init__(self):
		self.periodo = 0
		self.numero_periodo = 0.0

	def analizar(self, generador):
		"""Regresa un par (largo del periodo, numero donde se probó el periodo)
		"""
		numeros = generador.get_generacion() #lista de numeros
		primer_numero = numeros[0] 
		contador = 0
		for i in range(len(numeros)):
			if i == 0: #ignorar el primer numero porque es el mismo
				i = 1
			if numeros[i] == primer_numero: #cuando el primer numero se repita
				self.periodo = contador
				self.numero_periodo = primer_numero
				break
			contador += 1
		if self.periodo > 0:
			return (self.periodo, self.numero_periodo)
		else:
			return (-1, -1) #si no se detecta un periodo



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
			cadena += "{}\t{:5.5f}\n".format(registro[0], registro[2])
		return cadena

	def next(self):
		self.contador += 1
		siguiente = (self.multiplicador * self.actual + self.constante) % self.modulo
		self.actual = round(siguiente, 5)
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
		gen = Generador(17, 14, 50, 3)
	else:
		gen = Generador(int(sys.argv[1]))
	gen.ciclo(21)
	analizador = AnalizadorGenerador()
	print(analizador.analizar(gen))
	gen.mostrar_historico()


	
