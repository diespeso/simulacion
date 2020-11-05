#!/usr/bin/python3

from scipy import stats

from generador import Generador
from comun import precision

class Intervalo:

	def __init__(self, limite_inferior, tamano):
		self.limite_inferior = round(limite_inferior, precision)
		self.limite_superior = round(self.limite_inferior + tamano, precision)
		self.frecuencia = 0

	def __repr__(self):
		return "({}, {}) fo = {}".format(
			self.limite_inferior, self.limite_superior,
			self.frecuencia)

class PruebaFrecuencia:
	"""
	debe ser posible elegir el número de intervalos
	"""
	def __init__(self, numeros):
		""" 
		numeros: arreglo de números a probar
		"""
		self.n_intervalos = None
		self.intervalos = None
		self.numeros = numeros
		self.n = len(numeros)
		self.frecuencia_esperada = None
		self.tam_intervalo = None

		self.x_chi = None
		self.alfa = None
		self.tolerancia = None

	def generar_intervalos(self):
		intervalos = []
		acumulador = 0.0
		i = 0
		while i < self.n_intervalos:
			intervalo = Intervalo(acumulador, round(1 / self.n_intervalos, precision))
			intervalos.append(intervalo)
			acumulador = round(intervalo.limite_superior, precision)
			i += 1

		return intervalos

	def generar_frecuencia_observada(self):
		""" por cada número en el arreglo, y por cada intervalo
		revisar si el numero entra en el intervalo,
		y si entra aumentar la frecuencia de dicho intervalo
		"""
		for i in range(0, self.n):
			for intervalo in self.intervalos:
				if self.numeros[i] > intervalo.limite_inferior and self.numeros[i] < intervalo.limite_superior:
					
					intervalo.frecuencia += 1
	def mostrar_frecuencia_observada(self):
		for intervalo in self.intervalos:
			print(intervalo)

	#probar con alfa e intervalos 
	def probar(self, alfa, n_intervalos, mostrar=False):
		self.n_intervalos = n_intervalos
		self.frecuencia_esperada = round(self.n / self.n_intervalos, precision)
		self.intervalos = self.generar_intervalos()
		self.tam_intervalo = round(1 / self.n_intervalos, precision)
		self.generar_frecuencia_observada()
		self.alfa = alfa
		# se debe de tomar desde la izquierda, por lo que es el complemento de alfa
		# y no tiene 2 colas, por lo que no es necesario dividir entre 2
		self.tolerancia = round(stats.chi2.ppf(1 - alfa, self.n_intervalos - 1), precision)
		self.calcular_chi()

		if mostrar:
			self.mostrar_frecuencia_observada()
			print("x_chi2: {}".format(self.x_chi))
			print("tolerancia: {}".format(self.tolerancia))

		if self.x_chi < self.tolerancia:
			return True
		else:
			return False

	def calcular_chi(self):
		acumulador = 0.0
		# formula para obtener chi cuadrada x para la prueba
		for intervalo in self.intervalos:
			acumulador += (intervalo.frecuencia - self.frecuencia_esperada) ** 2
		self.x_chi = round(acumulador / self.frecuencia_esperada, precision)

if __name__ == '__main__':
	gen = Generador(101, 221, 17001, 17)
	gen.ciclo(65)

	prueba = PruebaFrecuencia(gen.get_generacion())
	print(prueba.probar(0.05, 4, mostrar=True))
	