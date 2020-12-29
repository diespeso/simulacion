#!/usr/bin/python3.9

from math import sqrt

from generador import Generador


mb_archivo = 500
mb_paquete = 5
paquetes = int(mb_archivo / mb_paquete)

precision = 3

class Red:
	def __init__(self, mb_archivo, mb_paquete):
		self.nodo_a = None
		self.nodo_b = None
		self.nodo_c = None
		self.nodo_d = None
		self.nodo_e = None

		self.set_nodos(Nodo('alfa'), Nodo('alfa'), Nodo('alfa'),
			Nodo('alfa'), Nodo('alfa'))

		self.set_factores_envio({'a': 0.7,
			'b': 1,
			'c': 1,
			'd': 0.8,
			'e': 0.9})

		self.nodo_actual = 'a'
		self.contador_paquetes = 0
		self.contador_global_paquetes = 0
		self.paquetes = None
		self.paquetes_exitosos = 0

		self.mb_paquete = mb_paquete
		self.mb_archivo = mb_archivo
		print("tam archivo: ", self.mb_archivo)
		print("tam paquete: ", self.mb_paquete)
		self.paquetes = int(self.mb_archivo / self.mb_paquete)
		print("paquetes: ", self.paquetes)
		self.paquetes_por_linea = int(self.paquetes / 5) # 5 líneas
		print("paquetes por línea: ", self.paquetes_por_linea)

		self.set_paquetes_exitosos() #depende de factores y nodos

	def set_nodos(self, nodo_a, nodo_b, nodo_c, nodo_d, nodo_e):
		self.nodo_a = nodo_a
		self.nodo_b = nodo_b
		self.nodo_c = nodo_c
		self.nodo_d = nodo_d
		self.nodo_e = nodo_e

	def set_factores_envio(self, factores):
		self.f_nodo_a = factores['a']
		self.f_nodo_b = factores['b']
		self.f_nodo_c = factores['c']
		self.f_nodo_d = factores['d']
		self.f_nodo_e = factores['e']

	def simular(self, numeros):
		"""Simula de forma automática la red siempre y cuando haya
		números suficientes.

		Toma una arreglo de n números aleatorios

		Si hay números suficientes regresa el resultado booleano
		de la simulación (simular_estatico), sino, regresará False.
		"""
		if len(numeros) < self.paquetes_exitosos:
			print("números insuficientes")
			return False #no se pude simular con esos números, no son suficientes
		else:
			for i in range(0, self.paquetes_exitosos):
				if not self.simular_estatico(numeros[i]):
					print("fin de la simulación")
					#todo bien(?)
					return True

	def simular_estatico(self, pseudo):
		"""
		Simula el envío de paquetes empezando con los paquetes exitosos
		del nodo a, luego el nodo b y así.

		Si el paquete se envió regresa True,
		Si ya se acabaron los paquetes regresa False y no hace nada
		"""
		print("global: ", self.contador_global_paquetes + 1)
		print("limite: ", self.paquetes_exitosos)
		if self.contador_global_paquetes + 1  == self.paquetes_exitosos:
			return False
		print("nodo actual: ", self.nodo_actual)
		print("contador paquetes: ", self.contador_paquetes)
		print("paquetes enviados: ", self.contador_global_paquetes)
		if self.nodo_actual == 'a':
			print("tipo: ", self.nodo_a.tipo, "\t estabilidad: ", self.f_nodo_a)
			if self.contador_paquetes < self.f_nodo_a * self.paquetes_por_linea:
				#si aun quedan paquetes por mandar
				vel = self.nodo_a.enviar(pseudo, self.mb_paquete)
				print("velocidad: ", vel, " mb/s")
				self.contador_paquetes += 1
				self.contador_global_paquetes += 1
			else:
				self.nodo_actual = 'b' # siguiente nodo
				self.contador_paquetes = 0
		if self.nodo_actual == 'b':
			print("tipo: ", self.nodo_b.tipo, "\t estabilidad: ", self.f_nodo_b)
			if self.contador_paquetes < self.f_nodo_b * self.paquetes_por_linea:
				vel = self.nodo_b.enviar(pseudo, self.mb_paquete)
				print("velocidad: ", vel, " mb/s")
				self.contador_paquetes += 1
				self.contador_global_paquetes += 1
			else:
				self.nodo_actual = 'c'
				self.contador_paquetes = 0
		if self.nodo_actual == 'c':
			print("tipo: ", self.nodo_c.tipo, "\t estabilidad: ", self.f_nodo_c)
			if self.contador_paquetes < self.f_nodo_c * self.paquetes_por_linea:
				vel = self.nodo_c.enviar(pseudo, self.mb_paquete)
				print("velocidad: ", vel, " mb/s")
				self.contador_paquetes += 1
				self.contador_global_paquetes += 1
			else:
				self.nodo_actual = 'd'
				self.contador_paquetes = 0
		if self.nodo_actual == 'd':
			print("tipo: ", self.nodo_d.tipo, "\t estabilidad: ", self.f_nodo_d)
			if self.contador_paquetes < self.f_nodo_d * self.paquetes_por_linea:
				vel = self.nodo_d.enviar(pseudo, self.mb_paquete)
				print("velocidad: ", vel, " mb/s")
				self.contador_paquetes += 1
				self.contador_global_paquetes += 1
			else:
				self.nodo_actual = 'e'
				self.contador_paquetes = 0
		if self.nodo_actual == 'e':
			print("tipo: ", self.nodo_e.tipo, "\t estabilidad: ", self.f_nodo_e)
			if self.contador_paquetes < self.f_nodo_e * self.paquetes_por_linea:
				vel = self.nodo_e.enviar(pseudo, self.mb_paquete)
				print("velocidad: ", vel, " mb/s")
				self.contador_paquetes += 1
				self.contador_global_paquetes += 1
			else:
				self.contador_paquetes = 0
				self.nodo_actual = None
		return True

	def set_paquetes_exitosos(self):
		self.paquetes_exitosos = self.calcular_paquetes_exitosos()

	def calcular_paquetes_exitosos(self):
		return round( self.f_nodo_a * self.paquetes_por_linea
			+ self.f_nodo_b * self.paquetes_por_linea
			+ self.f_nodo_c * self.paquetes_por_linea
			+ self.f_nodo_d * self.paquetes_por_linea
			+ self.f_nodo_e * self.paquetes_por_linea
		)


def calcular_triangular(pseudo, bajo, promedio, alto):
	x = (promedio - bajo) / (alto - bajo)
	if pseudo <= x:
		return bajo + sqrt((promedio - bajo) * (alto - bajo) * pseudo)
	else:
		return alto - sqrt((alto - promedio) * (alto - bajo) * (1 - pseudo))

class Nodo:
	""" Representa a una computadora que recibe paquetes, los procesa
	y los envía a otro nodo, todo nodo tiene un tipo: alfa, beta o gamma
	
	alfa
		envío promedio: 1.3 mb/s
		costo:
	beta
		envío promedio: 0.8 mb/s
		costo:
	gamma
		envío promedio: 0.6 mb/s
		costo:

	"""
	def __init__(self, str_tipo):
		self.mb_min = 0.3
		self.mb_max = 1.7

		self.tipo = str_tipo

		if str_tipo == 'alfa': #modelo de alto rendimiento
			self.mb_prom = 1.3
			self.costo_electrico = 0.015 # pesos de consumo por minuto
		elif str_tipo == 'beta': #modelo de medio rendimiento
			self.mb_prom = 0.8
			self.costo_electrico = 0.0075
		elif str_tipo == 'gamma': #modelo de bajo rendimiento
			self.costo_electrico = 0.0050
			self.mb_prom = 0.6
		else:
			print("no existe ese tipo de nodo")

	def calcular_velocidad(self, pseudo):
		return round(calcular_triangular(pseudo, self.mb_min, self.mb_prom, self.mb_max),
			2)

	def enviar(self, pseudo, tamano_paquete):
		""" Enviar envía un paquete de n tamaño en megabytes
		a una velocidad que se calcula dentro del a función.

		Regresa el tiempo en segundos que tardó en enviar n megabytes
		a una velocidad en mb/s
		"""
		velocidad = self.calcular_velocidad(pseudo)
		return round(tamano_paquete / velocidad, precision)

if __name__ == '__main__':
	alfa = Nodo('alfa')
	beta = Nodo('beta')
	gamma = Nodo('gamma')

	gen = Generador(17, 14, 50, 3)
	gen.ciclo(100)
	numeros = gen.get_generacion()

	red = Red(mb_archivo, mb_paquete)
	red.set_nodos(
		Nodo('alfa'),
		Nodo('gamma'),
		Nodo('beta'),
		Nodo('alfa'),
		Nodo('beta')
	)
	print("paquetes reales a enviar: ", red.calcular_paquetes_exitosos())
	"""
	for i in range(0,len(numeros)):
		print('alfa')
		alfa.enviar(numeros[i], mb_paquete)
		print('beta')
		beta.enviar(numeros[i], mb_paquete)
		print('gamma')
		gamma.enviar(numeros[i], mb_paquete)
	"""
	"""
	for i in range(0, 100):
		red.simular_estatico(numeros[i])
	"""
	if red.simular(numeros):
		print("exito")
	else:
		print("no éxito")