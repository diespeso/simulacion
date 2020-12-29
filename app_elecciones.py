#!/usr/bin/python3.9
"""
Aplicación para elegir 5 acciones para un candidato de campaña
simulando a 10,000 votantes, donde cada uno elige 3 acciones ordenadas
en orden de importancia
"""

from generador import Generador
from distribuidor_tabla import DistribuidorDeTabla
from parser_tablas import leer_archivo
import copy
import statistics

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
		return "atención a la educación"
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
			#print(self.contador_votos, self.max_votos)
			self.votos.append(
				self.distro.obtener_evento(pseudo)
			)
			c = self.contador_votos
			self.contador_votos += 1

			#redistribuir tabla eliminando lo que se acaba de votar para evitar repetir
			self.distro = redistribuir_tabla(self.votos[c], self.distro)	
			
			return self.votos[c]
		self.reiniciar() # ya se votó N veces
		"""Si solo reinicio, entonces se pierde siempre el número
		que triggereó el reiniciado, entonces también voto
		luego de reinicar para no desperdiciar números,
		es una función recursiva
		"""
		self.votar(pseudo, distribucion) 

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
		prob = round(copia.relaciones[evento][1] - copia.relaciones[evento][0], 5)
		#borrar el seleccionado
		del copia.eventos[evento]
		del copia.relaciones[evento] # -1 por ser indexado desde 0

		tam = len(copia.eventos)
		aumento = round(prob / tam, 5)

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

class Votacion:
	"""Toma una cantidad de votantes, y simula las votaciones
	para 5 sectores:
	sector 1: 16%
	sector 2: 24%
	sector 3: 20%
	sector 4: 5%
	sector 5: 15%

	Considerar que los votantes deben de ser el 5% de 200,000
	"""

	def __init__(self, c_votantes, distro, numeros):
		"""c_votantes = cantidad de votantes
		distro = tabla de distribución de probabilidad
		numeros = arreglo de números pseudoaleatorios
		"""
		self.c_votantes = c_votantes
		self.votante = Votante()
		self.distro = distro
		self.numeros = numeros

		self.votos_sector = {}
		self.votos_sector[1] = int(round(c_votantes * 0.16, 0)) #sector 1
		self.votos_sector[2] = int(round(c_votantes * 0.24, 0)) #s2
		self.votos_sector[3] = int(round(c_votantes * 0.20, 0))
		self.votos_sector[4] = int(round(c_votantes * 0.05, 0))
		self.votos_sector[5] = int(round(c_votantes * 0.15, 0))

		self.votos = {
		1: [],
		2: [],
		3: [],
		4: [],
		5: []
		} # registro de [n, n, n], [n, n, n]
	def simular(self):
		"""
		lleva a cabo la simulación total
		del número de votantes dados
		"""
		c_pseudo = 0
		for sector in self.votos_sector.items():
			#print("sector {}: {} votantes".format(sector[0], sector[1]))
			for i in range(0, sector[1]): #por cada votante en el sector
				for j in range(0, 3): # 3 votos
					voto = self.votante.votar(self.numeros[c_pseudo], self.distro)
					c_pseudo += 1
					if j == 2:
						self.registrar_voto(sector[0], self.votante.votos)
						#print(self.votante.votos)
		#debe ser por cada sector
		#print("sector 5: ", self.analizar_sector(5))
		for i in range(1, 7):
			#print("votos para {}: ".format(i), self.contar_votos_sector(5, i))
			pass

	def registrar_voto(self, n_sector,  voto):
		"""Registra el voto segun el n_sector al que pertence
		"""
		if len(voto) == 3:
			self.votos[n_sector].append(voto)

	def get_votos_str(self, n_sector):
		str_resultado = ""
		for voto in self.votos[n_sector]:
			for opcion in voto:
				str_resultado += str(opcion) + " "
			str_resultado[:-1] # eliminar el espacio que sobra
			str_resultado += "\n"
		return str_resultado[:-1] #eliminar newline que sobra


	def analizar_sector(self, n_sector):
		"""Regresa las 5 opciones mas votadas y su cantidad
		de votos, el algoritmo comienza de forma vertical por
		orden de importancia (la primera columna es mas importante),
		y luego hace un conteo global
		"""
		prohibidos = [] #numeros eliminados
		votos = self.votos[n_sector]
		col_uno = []
		for i in range(0, len(votos)): # columna uno
			col_uno.append(votos[i][0])
		col_dos = []
		for i in range(0, len(votos)):
			col_dos.append(votos[i][1]) #columna dos
		col_tres = []
		for i in range(0, len(votos)):
			col_tres.append(votos[i][2]) # columna 3
		#print(col_uno, col_dos, col_tres)

		uno = statistics.mode(col_uno)
		prohibidos.append(uno)
		#print(col_uno)
		#print("uno: ", uno)
		for numero in prohibidos:
			borrar_numero(col_dos, numero)
		#print(col_dos)
		dos = statistics.mode(col_dos)
		prohibidos.append(dos)
		#print("dos: ", dos)
		#print(col_tres)
		for numero in prohibidos:
			borrar_numero(col_tres, numero)
		#print(col_tres)
		tres = statistics.mode(col_tres)
		prohibidos.append(tres)
		#print("tres: ", tres)

		vector = [] #todos los votos
		for voto in votos:
			for opcion in voto:
				vector.append(opcion)

		#print("vector ", vector)
		borrar_numero(vector, uno)
		borrar_numero(vector, dos)
		borrar_numero(vector, tres)
		#print("vector ", vector)

		cuatro = statistics.mode(vector)
		#print("cuatro", cuatro)
		borrar_numero(vector, cuatro)
		cinco = statistics.mode(vector)
		#print("cinco", cinco)
		borrar_numero(vector,cinco)
		#print(vector)

		return [uno, dos, tres, cuatro, cinco]

#nota: si quiero implementar mi moda, entonces 
#lo mejor es acomodarlos de abajo hacia arriba

	def contar_votos_sector(self, n_sector, opcion):
		"""cuenta cuantos votos hubo para la opcion
		dada en el sector dado.

		No es realmente útil, pero está por si se
		quiere saber"""
		vector = self.vector_votos(n_sector)
		contador = 0
		for voto in vector:
			if voto == opcion:
				contador += 1

		return contador

	def vector_votos(self, n_sector):
		votos = self.votos[n_sector]
		vector = [] #todos los votos
		for voto in votos:
			for opcion in voto:
				vector.append(opcion)
		return vector


def borrar_numero(arreglo, numero):
	if numero in arreglo:
		for i in arreglo:
			if i == numero:
				arreglo.remove(numero)
	if numero in arreglo: #debe ser luego del ciclo
		arreglo.remove(numero) #siempre uno residual

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
	for i in range(0, 100):
		pseudo = gen.next()
		print("pseudo", pseudo)
		voto = votante.votar(pseudo, distro)
		if votante.contador_votos == N_VOTOS:
			print(votante.votos)
	votacion = Votacion(100, distro, gen.get_generacion())
	votacion.simular()
		

if __name__ == '__main__':
	
	main()