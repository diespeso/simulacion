#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

from prueba_frecuencia import PruebaFrecuencia

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10

class GeneradorResultados:
	def __init__(self, master, row, prueba):
		self.contador = 0
		self.master = master
		self.column = 0
		self.row = row
		self.prueba_frecuencia = prueba
		self.labels = []
		self.entries = []

		self.entry_chi = None
		self.entry_tolerancia = None
		self.entry_conclusion = None
	
	def dibujar_intervalos(self):
		""" incluye en el master todos los intervalo
		y devuelve la fila donde se teŕminó la inserción
		"""
		for intervalo in self.prueba_frecuencia.intervalos:
			self.generar_intervalo(intervalo)

		return self.row	

	def __del__(self):
		for label in self.labels:
			label.destroy()
		for entry in self.entries:
			entry.destroy()

	def generar_intervalo(self, intervalo):
		bajo = ttk.Entry(self.master, width=10)
		self.entries.append(bajo)
		bajo.insert(0, str(intervalo.limite_inferior))
		bajo.grid(column = self.column, row = self.row, pady = p_y)
		#ttk.Label(self.master, text=" a ").grid(column = (self.column + 1),row = self.row, pady = p_y)

		alto = ttk.Entry(self.master, width=10)
		self.entries.append(alto)
		alto.insert(0, str(intervalo.limite_superior))
		alto.grid(column = self.column + 1, row = self.row, pady = p_y)

		frec = ttk.Label(self.master, text="Frecuencia observada:")
		self.labels.append(frec)
		frec.grid(
			column = self.column + 2, row = self.row, pady = p_y)


		frecuencia = ttk.Entry(self.master, width=10)
		self.entries.append(frecuencia)
		frecuencia.insert(0, str(intervalo.frecuencia))
		frecuencia.grid(column= self.column + 3, row = self.row, pady = p_y)

		self.row += 1

	def add_resultados(self, resultado):
		self.add_interfaz_resultados()

		self.entry_chi.insert(0, str(self.prueba_frecuencia.x_chi))
		#self.entry_chi.config(state="disabled")

		self.entry_tolerancia.insert(0, str(self.prueba_frecuencia.tolerancia))
		#self.entry_tolerancia.config(state="disabled")

		if resultado: #distribuidos uniformemente
			self.entry_conclusion.insert(0, str("Los números están distribuidos uniformemente"))
		else:
			self.entry_conclusion.insert(0, str("Los números no están distribuidos uniformemente"))


	def add_interfaz_resultados(self):
		lbl_chi = ttk.Label(self.master, text="Chi cuadrada")
		self.labels.append(lbl_chi)
		lbl_chi.grid(column=0, row = self.row, padx = p_x_l, pady = p_y)
		
		self.entry_chi = ttk.Entry(self.master, width=15)
		self.entries.append(self.entry_chi)
		self.entry_chi.grid(column = 1, row = self.row, padx = p_x_l, pady = p_y)

		lbl_tolerancia = ttk.Label(self.master, text="Tolerancia")
		self.labels.append(lbl_tolerancia)
		lbl_tolerancia.grid(column=0, row = self.row + 1, padx = p_x_l, pady = p_y)

		self.entry_tolerancia = ttk.Entry(self.master, width=15)
		self.entries.append(self.entry_tolerancia)
		self.entry_tolerancia.grid(column = 1, row = self.row + 1, padx = p_x_l, pady = p_y)

		lbl_conclusion = ttk.Label(self.master, text="Conclusión: ")
		self.labels.append(lbl_conclusion)
		lbl_conclusion.grid(column = 0, row = self.row + 2, padx = p_x_l, pady = p_y)

		self.entry_conclusion = ttk.Entry(self.master, width=45)
		self.entries.append(self.entry_conclusion)
		self.entry_conclusion.grid(
			column = 1, row= self.row + 2, padx = p_x_l, pady = p_y,
			columnspan = 3)

class InterfazFrecuencia(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		self.entrada_tamano = None
		self.entrada_n_intervalos = None
		self.entrada_tam_intervalo = None
		self.entrada_f_esperada = None
		self.entrada_alfa = None
		self.btn_probar = None


		self.generador_resultados = None

		self.fila_resultados = None

		self.prueba_frecuencia = None
		self.init_interfaz()


	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

		self.btn_probar = ttk.Button(self, text="Probar", command=self.capturar)
		self.btn_probar.grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y)

	def add_labels(self):
		ttk.Label(self, text="Tamaño").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Intervalos").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="F. Esperada").grid(
			column = 2, row = 1, padx = p_x_l, pady = p_y + 10)

		ttk.Label(self, text="Tamaño de intervalo").grid(
			column = 4, row = 0, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="nivel de significancia").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Intervalos:").grid(
			column = 0, row = 3, padx = p_x_l, pady = p_y + 10)



	def add_entradas(self):
		self.entrada_tamano = ttk.Entry(self, width=15)
		self.entrada_tamano.grid(
			column = 1, row = 0, padx = p_x_l, pady = p_y)

		self.entrada_n_intervalos = ttk.Entry(self, width=15)
		self.entrada_n_intervalos.grid(
			column = 3, row = 0, padx = p_x_l, pady = p_y)

		self.entrada_tam_intervalo = ttk.Entry(self, width=15)
		self.entrada_tam_intervalo.grid(
			column = 5, row = 0, padx = p_x_l, pady = p_y)

		self.entrada_alfa = ttk.Entry(self, width=15)
		self.entrada_alfa.grid(
			column = 1, row = 1, padx = p_x_l, pady = p_y)

		self.entrada_f_esperada = ttk.Entry(self, width=15)
		self.entrada_f_esperada.grid(
			column = 3, row = 1, padx = p_x_l, pady = p_y)

	def abrir_entradas(self):
		self.entrada_tamano.config(state="enabled")
		self.entrada_tam_intervalo.config(state="enabled")
		self.entrada_f_esperada.config(state="enabled")

	def cerrar_entradas(self):
		self.entrada_tamano.config(state="disabled")
		self.entrada_tam_intervalo.config(state="disabled")
		self.entrada_f_esperada.config(state="disabled")

	def reiniciar(self):
		self.abrir_entradas()
		self.entrada_tamano.delete(0, END)
		self.entrada_tam_intervalo.delete(0, END)
		self.entrada_f_esperada.delete(0, END)
		self.cerrar_entradas()

	def reiniciar_temporales(self):
		self.abrir_entradas()
		self.entrada_tam_intervalo.delete(0, END)
		self.entrada_f_esperada.delete(0, END)
		self.cerrar_entradas()

	def borrar_conclusiones(self):
		if self.generador_resultados:
			self.generador_resultados.__del__()
			self.generador_resultados = None


	def rellenar(self, numeros):
		self.reiniciar()
		self.borrar_conclusiones()
		self.abrir_entradas()
		self.prueba_frecuencia = PruebaFrecuencia(numeros)
		self.entrada_tamano.insert(0, str(len(numeros)))	
		self.cerrar_entradas()

	def capturar(self):
		self.reiniciar_temporales()
		self.abrir_entradas()
		n_intervalos = int(self.entrada_n_intervalos.get())
		alfa = float(self.entrada_alfa.get())

		resultado = self.prueba_frecuencia.probar(alfa, n_intervalos)
		self.entrada_tam_intervalo.insert(0, str(self.prueba_frecuencia.tam_intervalo))
		self.entrada_f_esperada.insert(0, str(self.prueba_frecuencia.frecuencia_esperada))

		self.generador_resultados = GeneradorResultados(
			self, 5, self.prueba_frecuencia)
		self.fila_resultados = self.generador_resultados.dibujar_intervalos()
		self.generador_resultados.add_resultados(resultado)

		self.cerrar_entradas()