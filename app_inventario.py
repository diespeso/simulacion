#!/usr/bin/python3.9
precision = 3

from generador import Generador

from distribuidor_tabla import DistribuidorDeTabla


class SimInventario:

	"""
	Representa la tabla de la simulación de un inventario
	en n meses
	"""
	def __init__(self, q, r, inicial, numeros):
		""" q: cantidad a pedir
			r: cantidad donde se pide
			incial: inventario de inicio
			numeros: arreglo de números pseudoaleatorios
		"""
		self.q = q
		self.r = r
		self.inicial = inicial
		self.numeros = numeros
		self.i_numero = 0
		self.i_mes = 1

	def simular(self):
		"""Simula un mes de inventario"""
		print(self.i_mes)
		print(self.inicial)
		print(self.numeros[self.i_numero])
		print()

	def get_demanda_ajustada(self, pseudo):
		"""Toma una número pseudoaleatorio y devuelve la demanda
		ajustada que le corresponde a ese número
		"""



if __name__ == '__main__':
	probabilidades = """0.01 35
0.015 36
0.020 37
0.020 38
0.022 39
0.023 40
0.025 41
0.027 42
0.028 43
0.029 44
0.035 45
0.045 46
0.060 47
0.065 48
0.070 49
0.080 50
0.075 51
0.070 52
0.065 53
0.060 54
0.050 55
0.040 56
0.030 57
0.016 58
0.015 59
0.005 60"""
	td = DistribuidorDeTabla(probabilidades)
	gen = Generador(101, 221, 17001, 17)
	gen.ciclo(325)
	print(td.obtener_evento(gen.get_generacion()[0]))
	inv = SimInventario(200, 100, 150, gen.get_generacion())