#!/usr/bin/python3.9
precision = 3
from generador import Generador

class DistribuidorDeTabla:
	"""Representa una tabla de distribución de probabilidad
	empírica
	"""
	def __init__(self, distribucion):
		"""distribucion: cadena de texto que obedece el formato:
		probabilidad numero, ejemplo:
		0.010 35
		0.015 36
		"""
		self.conjuntos = None
		self.probabilidades = None
		self.eventos = None
		self.relaciones = None
		try:
			self.conjuntos = self.crear_conjuntos(distribucion)
			self.probabilidades, self.eventos = self.crear_tabla(self.conjuntos)
			self.relacion = self.crear_relacion()
		except Exception as e:
			print(e.__str__())
		

	def crear_conjuntos(self, distribucion):
		"""Toma una cadena de texto en formato:
		0.010 35
		0.015 36
		y la convierte en series de '0.01 35', '0.015 36'
		"""
		conjuntos = distribucion.split(sep='\n')
		for conjunto in conjuntos:
			if not ' ' in conjunto:
				raise Exception("Fallo al leer la distribución de probabilidad")
		return conjuntos

	def traducir_a_numeros(self, conjuntos):
		"""Toma una serie de '0.01 35', '0.015 36' y la 
		transforma en diccionario 35 -> 0.01
		"""
		pass #quizas no sea util

	def crear_tabla(self, conjuntos):
		"""Toma una serie de '0.01 35', '0.015 36' y la 
		transforma a una serie de probabilidades, hace que la
		serie comience en 0.0 de forma automática

		regresa (serie de probabilidades, serie de eventos)
		"""
		probs = []
		eventos = []
		probs.append(0.0)
		for conjunto in conjuntos:
			s = conjunto.split(sep=' ')
			probs.append(
				float(s[0])
			)
			eventos.append(
				int(s[1])
			)
		return (probs, eventos)

	def crear_relacion(self):
		"""Crea un arreglo de formato
		[
			[0.0, 0.01],
			[0.01, 0.025]
		]

		el índice i representa el número de evento
		que se traducirá el intervalo,ejemplo i = 0 -> self.probs[0] -> 35
		"""
		acumulador = 0.0
		relaciones = []
		for i in range(len(self.probabilidades) - 1):
			j = i + 1
			relacion = []
			relacion.append(acumulador)
			relacion.append(round(acumulador + self.probabilidades[j], precision))
			acumulador = round(acumulador + self.probabilidades[j],
				precision)
			relaciones.append(relacion)
		self.relaciones = relaciones
		self.revisar_relaciones()


	def revisar_relaciones(self):
		if self.relaciones[-1][1] != 1.0:
			raise Exception("La distribución de probabilidades no suma 1.0")


	def obtener_evento(self, pseudo):
		"""Toma un número pseudoaleatorio y lo transforma
		a una evento, osea: lo busca en la tabla de probabiliades
		y retorna el valor del evento que corresponde a ese espacio
		"""
		for evento in range(len(self.relaciones)):
			#buscar en que intervalode evento cae el pseudoaleatorio
			limites = self.relaciones[evento]
			if pseudo >= limites[0] and pseudo < limites[1]:
				return self.eventos[evento]
		raise Exception("No se pudo encontrar un evento en ninǵun rango")




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
	inv = SimInventario(200, 100, 150, gen.get_generacion())