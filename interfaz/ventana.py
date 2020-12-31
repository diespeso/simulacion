#!/usr/bin/pyhton3

from tkinter import ttk
from tkinter import *

from interfaz.interfaz_generador import InterfazGenerador
from interfaz.interfaz_promedio import InterfazPromedio
from interfaz.interfaz_frecuencia import InterfazFrecuencia

from interfaz.interfaz_app_red import InterfazAppRed


class Ventana(Frame):
	def __init__(self, master=None, args=None):
		Frame.__init__(self, master)
		self.master = master
		self.tab_control = None
		self.tab_generador = None
		self.tab_promedio = None
		self.tab_frecuencia = None

		self.tab_app_red = None
		self.init_window()
		self.tab_control.bind("<<NotebookTabChanged>>", self.configure_tab_control)
		if args:
			self.tab_generador.auto_run(args)

	def set_root(self, root):
		self.root = root

	def init_window(self):
		self.master.title("Generador Pseudoaleatorios")
		self.crear_tabs()
	
		self.grid(column = 0, row = 0)
		#self.pack(fill=BOTH, expand=1)

	def configure_tab_control(self, event):
		if self.tab_generador.get_is_generador_usado():
			self.rellenar_tabs_de_prueba()
			self.rellenar_tabs_de_aplicacion()
		else:
			pass #do nothing
		print(self.tab_control.tab("current"))
		current_tab = self.tab_control.tab("current")
		if current_tab['text'] == "Simulación de Red": #si se entra a la app de red
			self.root.geometry("920x600+100+100")
		else:
			self.root.geometry("868x600+100+100")

	def rellenar_tabs_de_prueba(self):
		self.rellenar_tab_promedio()
		self.rellenar_tab_frecuencia()

	def rellenar_tab_promedio(self):
		#usar la generación del generador para rellenar la tab
		#del promedio
		self.tab_promedio.rellenar(self.tab_generador.generador.get_generacion())

	def rellenar_tab_frecuencia(self):
		self.tab_frecuencia.rellenar(self.tab_generador.generador.get_generacion())

	def rellenar_tabs_de_aplicacion(self):
		self.rellenar_tab_app_red()

	def rellenar_tab_app_red(self):
		self.tab_app_red.rellenar(self.tab_generador.generador.get_generacion())
	
	def crear_tabs(self):
		self.tab_control = ttk.Notebook(self)

		generador = None

		self.tab_generador = InterfazGenerador(self.tab_control)
		self.tab_promedio = InterfazPromedio(self.tab_control)
		self.tab_frecuencia = InterfazFrecuencia(self.tab_control)

		self.tab_app_red = InterfazAppRed(self.tab_control)

		self.tab_control.add(self.tab_generador, text="Generador")
		self.tab_control.add(self.tab_promedio, text="Prueba Promedio")
		self.tab_control.add(self.tab_frecuencia, text="Prueba Frecuencia")
		
		self.tab_control.add(self.tab_app_red, text="Simulación de Red")
		
		self.tab_control.grid(column= 1, row = 1)
		#self.tab_control.pack(expand=1, fill=BOTH)
		

