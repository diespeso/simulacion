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
	def __init__(self, numeros, n_intervalos):
		""" 
		numeros: arreglo de números a probar
		intervalos: define en cuantos intervalos se va a 
		separar la prueba
		"""
		self.n_intervalos = n_intervalos
		self.numeros = numeros
		self.n = len(numeros)
		self.frecuencia_esperada = round(self.n / self.n_intervalos, precision)

		self.intervalos = self.generar_intervalos()
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

	def probar(self, alfa, mostrar=False):
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
	gen = Generador(3)
	gen.ciclo(200)

	prueba = PruebaFrecuencia(gen.get_generacion(), 4)
	print(prueba.probar(0.05, mostrar=True))
	