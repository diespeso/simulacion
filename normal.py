#!/usr/bin/python3

import math
from scipy import stats

from generador import Generador

class Normal:
	def __init__(self, mu, sigma):
		self.mu = mu
		self.sigma = sigma
		self.x = None
		self.z = None

	def densidad_puntual(self, x):
		self.x = x
		raiz = math.sqrt(2 * math.pi * self.sigma)
		exponente_2 = (self.x - self.mu) ** 2
		exponente_2 /= -2 * self.sigma ** 2
		return (math.e ** exponente_2) / raiz

	def densidad_estandar_acumulada(self, x):
		""" estandariza los valores a zeta, para luego obtener
		la densidad acumulada desde la izquierda
		"""
		self.x = x
		self.z = (self.x - self.mu) / self.sigma
		return stats.norm.cdf(self.z)

	def densidad_estandar_acumulada_inversa(self, densidad):
		""" regresa el valor en x desde izquierda de donde se obtiene
		el valor de densidad acumulada dado
		"""
		return stats.norm.ppf(densidad)


#nuevo módulo
class PruebaPromedio:
	""" la prueba del promedio toma un valor alfa que se divide
	entre dos, que es la tolerancia de error, se busca el valor
	de distribución inversa de la densidad = (1 - alfa / 2)
	"""
	def __init__(self, numeros):
		self.numeros = numeros
		self.n = len(numeros)
		self.normal = None
		self.ejecutar()
		self.z0 = None
		self.z_alfa_mitad = None

	def ejecutar(self):
		self.generar_normal()

	def generar_normal(self):
		self.mu = self.obtener_promedio()
		self.sigma = self.obtener_desviacion_estandar(self.mu)
		self.normal = Normal(self.mu, self.sigma)

	def obtener_promedio(self):
		sumatoria = 0
		for numero in self.numeros:
			sumatoria += numero
		return sumatoria / len(self.numeros)

	def obtener_desviacion_estandar(self, promedio):
		sumatoria_cuadrados = 0
		for numero in self.numeros:
			sumatoria_cuadrados += (numero - promedio) ** 2
		varianza = sumatoria_cuadrados / len(self.numeros)
		return math.sqrt(varianza)

	def probar(self, alfa):
		tolerancia = self.normal.densidad_estandar_acumulada_inversa( 1 - alfa / 2)
		self.z_alfa_mitad = tolerancia
		punto_z0 = abs( self.obtener_z0() )
		self.z0 = punto_z0

		if punto_z0 < tolerancia:
			return True
		else:
			return False

	def obtener_z0(self):
		resultado = (self.mu - 0.5) * math.sqrt(len(self.numeros))
		return resultado / math.sqrt(1 / 12)
		


if __name__ == '__main__':
	generador = Generador(3)
	generador.ciclo(200)

	prueba = PruebaPromedio(generador.get_generacion())
	print(prueba.probar(0.05))
	print(prueba.z0)
	print(prueba.z_alfa_mitad)

	gen = None
	i = 0
	prueba = None
	seguir = True
"""
	while seguir:
		gen = Generador(i)
		gen.ciclo(300)
		prueba = PruebaPromedio(gen.get_generacion())
		seguir = prueba.probar(0.05)
		if seguir == False:
			print(i)
		i += 1
"""

	


