#!/usr/bin/python3

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
			column = 0, row = 1, padx = p_x_l, pady = p_y)

		self.txt_generacion = scrolledtext.ScrolledText(self.master, width=120, height=50)
		self.txt_generacion.grid(
			column = 0, row = 0, padx = 10, pady= 80)
		

		#self.pack(expand=1, fill=BOTH)


	def capturar(self):
		
		pass

"""
	def init_window(self):
		self.master.title("Generador Pseudoaleatorio")
		self.crear_tabs()

		self.interfaz_generador()

		self.pack(fill=BOTH, expand=1)

	def crear_tabs(self):
		self.tab_control = ttk.Notebook(self.master)

		self.tab_generador = ttk.Frame(self.tab_control)
		self.tab_promedio = ttk.Frame(self.tab_control)
		self.tab_frecuencia = ttk.Frame(self.tab_control)

		self.tab_control.add(self.tab_generador, text="Generador")
		self.tab_control.add(self.tab_promedio, text="Promedio")
		self.tab_control.add(self.tab_frecuencia, text="Frecuencia")

		self.tab_control.pack(fill=BOTH, expand=1)

	def interfaz_generador(self):
		ttk.Label(self.tab_generador, text="Semilla: ").grid(
			column = 0, row = 0, padx = 10, pady = 10)
"""