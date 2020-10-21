#!/usr/bin/python3

from tkinter import *

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10

class InterfazPromedio(Frame):
	"""
		Una interfaz promedio se inicializa con toda la interfaz
		posible, pero al momento de aplicarla, es cuando se pasa
		el arreglo de los números. Entonces una interfaz promedio
		existe independientemente de una interfaz de generador
		pero no hace nada hasta que el generador ha generado
		los números.
	"""
	def __init__(self, master, generador):
		Frame.__init__(self, master)

		self.init_interfaz()
		self.entrada_promedio = None
		self.entrada_des_estandar = None
		self.entrada_z0 = None
		self.entrada_alfa = None

	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

	def add_labels(self):
		ttk.Label(self, text="Promedio").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Desv. Estándar").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="z0").grid(
			column = 4, row = 0, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="nivel significancia").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

	def add_entradas(self):
		self.entrada_promedio = ttk.Entry(self, width=15)
		self.entrada_promedio.grid(
			column = 1, row = 0, padx = 0, pady = 0)
		self.entrada_promedio.config(state="disabled") #al final

		self.entrada_des_estandar = ttk.Entry(self, width=15)
		self.entrada_des_estandar.grid(
			column = 3, row = 0, padx = 0, pady = 0)
		self.entrada_des_estandar.config(state="disabled")

		self.entrada_z0 = ttk.Entry(self, width=15)
		self.entrada_z0.grid(
			column = 5, row = 0, padx = 0, pady = 0)
		self.entrada_z0.config(state="disabled")

		self.entrada_alfa = ttk.Entry(self, width=15)
		self.entrada_alfa.grid(
			column = 1, row = 1, padx = 0, pady = 0)