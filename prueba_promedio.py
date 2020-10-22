#!/usr/bin/python3

import math

from normal import Normal
from generador import Generador
from comun import precision

class PruebaPromedio:
	""" la prueba del promedio toma un valor alfa que se divide
	entre dos, que es la tolerancia de error, se busca el valor
	de distribución inversa de la densidad = (1 - alfa / 2)
	"""
	def __init__(self, numeros):
		self.numeros = numeros
		self.n = len(numeros)
		self.normal = None
		self.z0 = None
		self.sigma = None
		self.z_alfa_mitad = None
		self.tolerancia = None
		self.ejecutar()

	def ejecutar(self):
		self.mu = self.obtener_promedio()
		self.sigma = self.obtener_desviacion_estandar(self.mu)
		self.z0 = abs(self.obtener_z0())
		self.generar_normal()

	def generar_normal(self):
		self.normal = Normal(self.mu, self.sigma)

	def obtener_promedio(self):
		sumatoria = 0
		for numero in self.numeros:
			sumatoria += numero
		return round(sumatoria / len(self.numeros), precision)

	def obtener_desviacion_estandar(self, promedio):
		sumatoria_cuadrados = 0
		for numero in self.numeros:
			sumatoria_cuadrados += (numero - promedio) ** 2
		varianza = sumatoria_cuadrados / len(self.numeros)
		return round(math.sqrt(varianza), precision)

	def probar(self, alfa, mostrar=False):
		self.tolerancia = self.normal.densidad_estandar_acumulada_inversa( 1 - alfa / 2)
		self.z_alfa_mitad = self.tolerancia

		if mostrar:
			print("promedio: {}".format(self.mu))
			print("desviacion e: {}".format(self.sigma))
			print("z0: {}".format(self.z0))
			print("tolerancia: {}".format(self.tolerancia))


		if punto_z0 < self.tolerancia:
			return True
		else:
			return False

	def obtener_z0(self):
		resultado = (self.mu - 0.5) * math.sqrt(len(self.numeros))
		return round(resultado / math.sqrt(1 / 12), precision)
		

if __name__ == '__main__':
	generador = Generador(101, 221, 17001, 17)
	generador.ciclo(200)

	generador.mostrar_historico()

	prueba = PruebaPromedio(generador.get_generacion())
	print(prueba.probar(0.05, mostrar=True))

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

	


