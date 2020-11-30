#!/usr/bin/python3.9
"""
Aplicación para elegir 5 acciones para un candidato de campaña
simulando a 10,000 votantes, donde cada uno elige 3 acciones ordenadas
en orden de importancia
"""

from generador import Generador
from distribuidor_tabla import DistribuidorDeTabla
import copy

N_VOTOS = 3

def id_to_propuesta(id):
	"""Toma un identificador de propuesta
	y lo transforma en la forma textual de esa propuesta.
	Si no encuentra la propuesta envía una exception
	"""
	if id == 1:
		return "creación y protección de empleo"
	elif id == 2:
		return "atención a la seguridad"
	elif id == 3:
		return "impulso al comercio y al turismo"
	elif id == 4:
		return "prestación de servicios"
	elif id == 5:
		return "honestidad de los servidores"
	elif id == 6:
		return "atención al educación"
	else:
		raise Exception("Id de propuesta inexistente")

class Votante:
	"""Representa a un votante, pero esta planeada para ser
	reutilizada.

	tiene N_VOTOS antes de reiniciarse, para este caso es igual a 3.

	La función principal de esta clase es votar
	"""
	def __init__(self):
		self.votos = []
		self.contador_votos = 0
		self.max_votos = N_VOTOS
		self.distro = None

	def votar(self, pseudo, distribucion):
		"""
		Toma un número pseudo para generar el evento de un voto
		Toma una distribución de la cual obtener el evento.
		Si el contador de votos es igual a 0, entonces el votante
		es nuevo, por lo que se debe asignar la distribución dada

		Pero si no es nuevo, entonces se debe ignorar la distribución
		dada, así se usará la distribución calculada luego del voto
		anterior al voto actual.

		Cada vez que un votante vota, se registra por qué opción voto
		para así redistribuir la tabla de distribuciones interna
		del votante, esto se hace para evitar que se repita el mismo
		voto, lo cual no tendría sentido.
		"""
		if self.contador_votos == 0:
			self.distro = distribucion # solo aceptar la distro si es nuevo votante
		if self.contador_votos < self.max_votos:
			self.votos.append(
				self.distro.obtener_evento(pseudo)
			)
			c = self.contador_votos
			self.contador_votos += 1

			#redistribuir tabla eliminando lo que se acaba de votar para evitar repetir
			self.distro = redistribuir_tabla(self.votos[c], self.distro)
			print(self.votos)
			
			return self.votos[c]
		self.reiniciar() # ya se votó N veces

	def reiniciar(self):
		self.votos = []
		self.contador_votos = 0
		self.distro = None

	def print(self):
		for i in self.votos:
			print(i)
		
def redistribuir_tabla(ev, distro):
	"""Toma una tabla, le quita el evento señalado
	y redistribuye las probabilidades.

	Considerar que los eventos se refieren van de 1 a 6
	en la primera vez que se borra uno.

	"""
	copia = copy.deepcopy(distro)
	if ev in copia.eventos:
		evento = copia.eventos.index(ev)
		print("ev", ev, "evento", evento)
		prob = round(copia.relaciones[evento][1] - copia.relaciones[evento][0], 5)
		#borrar el seleccionado
		del copia.eventos[evento]
		del copia.relaciones[evento] # -1 por ser indexado desde 0

		tam = len(copia.eventos)
		aumento = round(prob / tam, 5)
		print("prob", prob, "tam", tam, "aumento", aumento)

		str_relaciones = copia.generar_str()
		str_deposito = ""
		for linea in str_relaciones.split(sep="\n"):
			#por cada renglon, osea relacion de probabilidad
			prob = round(float(linea.split(" ")[0]) + aumento, 5)
			e = linea.split(" ")[1] #evento
			str_deposito += str(prob) + " " + e + "\n"

		#-1 para eliminar la nueva linea al final
		return DistribuidorDeTabla(str_deposito[:-1])
	else:
		raise Exception("no se pudo redistribuir el evento dado") # ignorar y enviar denuevo


def main():
	print("elecciones!")
	str_dis = """0.17 1
0.23 2
0.10 3
0.17 4
0.19 5
0.14 6"""

	distro = DistribuidorDeTabla(str_dis)
	
	gen = Generador(101, 221, 17001, 17)
	gen.ciclo(300)
	
	votante = Votante()
	for i in range(0, 10):
		pseudo = gen.next()
		print("pseudo", pseudo)
		voto = votante.votar(pseudo, distro)
		if voto:
			print(votante.votos, votante.contador_votos)
		else:
			print("reinicio!")
		

if __name__ == '__main__':
	
	main()