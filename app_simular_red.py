#!/usr/bin/python3.9

from math import sqrt

from generador import Generador


mb_archivo = 500
mb_paquete = 5
paquetes = int(mb_archivo / mb_paquete)

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

		self.mb_paquete = mb_paquete
		self.mb_archivo = mb_archivo
		self.paquetes_por_linea = self.mb_archivo / self.mb_paquete

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

	def simular_estatico(pseudo):
		if self.nodo_actual == 'a':
			if self.contador_paquetes < self.f_nodo_a * self.paquetes_por_linea:
				#si aun quedan paquetes por mandar
				vel = self.nodo_a.enviar(pseudo)
				self.contador_paquetes += 1


def calcular_triangular(pseudo, bajo, promedio, alto):
	x = (promedio - bajo) / (alto - bajo)
	if pseudo <= x:
		return bajo + sqrt((promedio - bajo) * (alto - bajo) * pseudo)
	else:
		return alto - sqrt((alto - promedio) * (alto - bajo) * (1 - pseudo))

class Nodo:
	def __init__(self, str_tipo):
		self.mb_min = 0.3
		self.mb_max = 1.7

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
		velocidad = self.calcular_velocidad(pseudo)
		print('velocidad', velocidad)
		return round(tamano_paquete / velocidad)

if __name__ == '__main__':
	alfa = Nodo('alfa')
	beta = Nodo('beta')
	gamma = Nodo('gamma')

	gen = Generador(17, 14, 50, 3)
	gen.ciclo(5)
	numeros = gen.get_generacion()

	red = Red()
	for i in range(0,len(numeros)):
		print('alfa')
		alfa.enviar(numeros[i], mb_paquete)
		print('beta')
		beta.enviar(numeros[i], mb_paquete)
		print('gamma')
		gamma.enviar(numeros[i], mb_paquete)