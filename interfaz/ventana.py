#!/usr/bin/pyhton3

from tkinter import ttk
from tkinter import *

from interfaz.interfaz_generador import InterfazGenerador
from interfaz.interfaz_promedio import InterfazPromedio
from interfaz.interfaz_frecuencia import InterfazFrecuencia

class Ventana(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
		self.tab_control = None
		self.tab_generador = None
		self.tab_promedio = None
		self.tab_frecuencia = None

	def init_window(self):
		self.master.title("Generador Pseudoaleatorios")
		self.crear_tabs()

		self.grid(column = 0, row = 0)
		#self.pack(fill=BOTH, expand=1)

	def crear_tabs(self):
		self.tab_control = ttk.Notebook(self)

		generador = None

		self.tab_generador = InterfazGenerador(self.tab_control, generador)
		self.tab_promedio = InterfazPromedio(self.tab_control, generador)
		self.tab_frecuencia = InterfazFrecuencia(self.tab_control, generador)

		self.tab_control.add(self.tab_generador, text="Generador")
		self.tab_control.add(self.tab_promedio, text="Prueba Promedio")
		self.tab_control.add(self.tab_frecuencia, text="Prueba Frecuencia")
		self.tab_control.grid(column= 1, row = 1)
		#self.tab_control.pack(expand=1, fill=BOTH)

