#!/usr/bin/python3

import sys

from tkinter import ttk 
from tkinter import *
from tkinter import scrolledtext

from interfaz.ventana import *

from generador import Generador

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos


class InterfazGenerador(Frame):
	def __init__(self, ventana):
		Frame.__init__(self, ventana)
		self.master = ventana

		self.entrada_semilla = None
		self.entrada_multiplicador = None
		self.entrada_constante = None
		self.entrada_modulo = None
		self.entrada_ciclo = None
		self.btn_generar = None
		self.txt_generacion = None
		self.init_interfaz()

	def init_interfaz(self):
		ttk.Label(self, text="Semilla").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		self.entrada_semilla = ttk.Entry(self, width=15)
		self.entrada_semilla.grid(
			column = 1, row = 0, padx = 0, pady = 0)

		ttk.Label(self, text="Constante").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		self.entrada_constante = ttk.Entry(self, width=15)
		self.entrada_constante.grid(
			column= 3, row = 0, padx = 0, pady = 0)

		ttk.Label(self, text="Multiplicador").grid(
			column = 4, row = 0, padx = p_x_l, pady = p_y)
		self.entrada_multiplicador = ttk.Entry(self, width=15)
		self.entrada_multiplicador.grid(
			column = 5, row = 0, padx = 0, pady = 0)

		ttk.Label(self, text="Módulo").grid(
			column = 6, row = 0, padx = p_x_l, pady = p_y)
		self.entrada_modulo = ttk.Entry(self, width=15)
		self.entrada_modulo.grid(
			column = 7, row = 0, padx = 0, pady = 0)

		self.btn_generar = ttk.Button(self, text="Generar", command=self.capturar)
		self.btn_generar.grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Tamaño").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)
		self.entrada_ciclo = ttk.Entry(self, width=15)
		self.entrada_ciclo.grid(
			column = 1, row = 1, padx = 0, pady = 0)

		self.txt_generacion = scrolledtext.ScrolledText(self.master, width=120, height=35)
		self.txt_generacion.grid(
			column = 0, row = 0, padx = 10, pady= 100)
		

		#self.pack(expand=1, fill=BOTH)


	def capturar(self):
		generador = None
		ciclo = None
		try:
			generador = Generador(
				int(self.entrada_multiplicador.get()),
				int(self.entrada_constante.get()),
				int(self.entrada_modulo.get()),
				int(self.entrada_semilla.get())
			)

			ciclo = int(self.entrada_ciclo.get())

		except:
			print("No se pudo crear el generador, datos incorrectos")
			e = sys.exc_info()[0]
			print(e.__str__())
		finally:
			generador.ciclo(ciclo)
			self.txt_generacion.insert(INSERT, generador.str_historico())

		def limpiar(self):
			pass

		def reiniciar(self):
			pass