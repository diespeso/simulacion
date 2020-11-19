#!/usr/bin/python3

import sys

from tkinter import ttk 
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

from interfaz.ventana import *

from generador import Generador
from generador import AnalizadorGenerador

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos


class InterfazGenerador(Frame):
	#TODO: Ventana de pánico si falta algún dato,
	# hay un try catch para esto
	def __init__(self, ventana): #todo: generador?
		Frame.__init__(self, ventana)
		self.master = ventana

		self.entrada_semilla = None
		self.entrada_multiplicador = None
		self.entrada_constante = None
		self.entrada_modulo = None
		self.entrada_ciclo = None
		self.btn_generar = None
		self.txt_generacion = None
		self.generador = None
		self.is_auto_run = False		

		self.is_generador_usado = False
		self.init_interfaz()

	def init_interfaz(self):
		self.add_labels()

		# entradas
		self.entrada_semilla = ttk.Entry(self, width=15)
		self.entrada_semilla.grid(
			column = 1, row = 0, padx = 0, pady = 0)


		self.entrada_constante = ttk.Entry(self, width=15)
		self.entrada_constante.grid(
			column= 3, row = 0, padx = 0, pady = 0)

		self.entrada_multiplicador = ttk.Entry(self, width=15)
		self.entrada_multiplicador.grid(
			column = 5, row = 0, padx = 0, pady = 0)

		self.entrada_modulo = ttk.Entry(self, width=15)
		self.entrada_modulo.grid(
			column = 7, row = 0, padx = 0, pady = 0)

		self.btn_generar = ttk.Button(self, text="Generar", command=self.capturar)
		self.btn_generar.grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y)


		self.entrada_ciclo = ttk.Entry(self, width=15)
		self.entrada_ciclo.grid(
			column = 1, row = 1, padx = 0, pady = 0)

		self.txt_generacion = scrolledtext.ScrolledText(self.master, width=120, height=35)
		self.txt_generacion.grid(
			column = 0, row = 0, padx = 10, pady= 100)
		

		#self.pack(expand=1, fill=BOTH)

	def add_labels(self):
		ttk.Label(self, text="Semilla").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Constante").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Multiplicador").grid(
			column = 4, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Módulo").grid(
			column = 6, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Tamaño").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

	def capturar(self):
		#Se activa al presionar el botón de generar
		self.limpiar()
		ciclo = None
		try:
			self.generador = Generador(
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
			self.generador.ciclo(ciclo)
			self.is_generador_usado = True
			#analizar en busca del periodo
			analizador = AnalizadorGenerador()
			analisis = analizador.analizar(self.generador)
			str_analisis ="La longitud del periodo para estos datos es de {},\nsi aún así deseas continuar ignora este mensaje".format(
				analisis[0])
			messagebox.showwarning("Advertencia de periodo", str_analisis)


			print(analisis)

			self.insertar_generacion(self.generador)

	def auto_run(self, datos):
		self.is_auto_run = True
		self.is_generador_usado = True
		self.generador = Generador(
			datos["multiplicador"],
			datos["constante"],
			datos["modulo"],
			datos["semilla"])
		self.generador.ciclo(datos["tamano"])
		self.insertar_generacion(self.generador)

	def insertar_generacion(self, generador):
			self.txt_generacion.insert(INSERT, generador.str_historico())

	def limpiar(self):
		self.txt_generacion.delete("1.0", END)

	def get_is_generador_usado(self):
		return self.is_generador_usado

	def get_is_auto_run(self):
		return self.is_auto_run

	def reiniciar(self):
		pass
