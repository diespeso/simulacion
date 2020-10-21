#!/usr/bin/python3

"""
	este sistema es independiente del sistema visual y se encarga
	de llevar a cabo las pruebas a partir de un gerador.

	Este sistema consume un generador, el cual se activa al ser
	consumido. Si el generador ya fue activado antes, habrá 
	problemas

	Este sistema será consumido por el sistema visual para llenar
	sus campos.

"""

from generador import Generador
from prueba_promedio import PruebaPromedio
from prueba_frecuencia import PruebaFrecuencia

class SistemaEstadistico:
	def __init__(self):
		self.generador = None
		self.prueba_promedio = None
		self.prueba_frecuencia = None

	def init_generador(self, generador, n):
		""" acepta un generador limpio y un valor de n para
		saber cuantos número generar
		"""
		self.generador = generador
		if not self.generador.is_vacio():
			self.generador.reiniciar()
		self.generador.ciclo(n)

		#si está vacio aun después del ciclo, error
		if self.generador.is_vacio():
			raise Exception("Generador vacío")
		self.init_prueba_promedio()
		self.init_prueba_frecuencia()

	def init_prueba_promedio(self):
		self.prueba_promedio = PruebaPromedio(self.generador.get_generacion())

	def init_prueba_frecuencia(self):
		self.prueba_frecencia = None #???

	def get_generacion(self):
		return self.generador.get_generacion()

	def generar_datos_promedio(self, alfa):
		""" genera una prueba de promedio con el alfa dado y
		regresa un dicionario con sus valores
		"""
		datos = {}
		self.prueba_promedio.probar(alfa)
		datos["promedio"] = self.prueba_promedio.mu
		datos["desv"] = self.prueba_promedio.sigma

		return datos

if __name__ == '__main__':
	gen = Generador(101, 221, 17001, 17)
	sistema = SistemaEstadistico()
	sistema.init_generador(gen, 325)
	sistema.prueba_promedio.probar(0.05, mostrar=True)