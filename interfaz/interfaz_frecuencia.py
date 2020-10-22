#!/usr/bin/python3

from tkinter import *

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10

class InterfazFrecuencia(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)


	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

	def add_labels(self):
		ttk.Label(self, text="Tamaño").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Intervalos").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

	def add_entradas(self):
		