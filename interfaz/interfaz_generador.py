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
	""" Tab gráfica donde se generan números pseudoaleatorios"""
	
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
		""" Pone todos los elementos gráficos en su lugar"""
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

	def add_labels(self):
		"""Añade labels a la interfaz gráfica"""
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
		"""Se activa al presionar el botón de generar
			Provoca que se llene el apartado de números generados
		"""
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
			resultado_analisis = self.analizar_periodo()
			analisis_periodo =None
			if resultado_analisis[0]: #si hay periodo, notificar al usuario
				messagebox.showwarning("Advertencia de periodo", resultado_analisis[1])
				analisis_periodo = resultado_analisis[2]
			self.insertar_generacion(self.generador, datos_periodo=analisis_periodo)
			

	def auto_run(self, datos):
		"""Sólo util cuando se corre el programa standalone,
		genera números sin tener que llenar campos manualmente
		"""
		self.is_auto_run = True
		self.is_generador_usado = True
		self.generador = Generador(
			datos["multiplicador"],
			datos["constante"],
			datos["modulo"],
			datos["semilla"])
		self.generador.ciclo(datos["tamano"])
		self.insertar_generacion(self.generador)

	def insertar_generacion(self, generador, datos_periodo=None):
		"""Inserta todos los datos de la generación de un generador
		en el campo de números generados

		Si hay datos_periodo, entonces colorear los números del periodo.
		"""
		contador_periodo = 0
		registros = generador.get_historico()
		for i in range(len(generador.get_historico())):
			registro = registros[i]
			if datos_periodo:
				if contador_periodo < datos_periodo[0]:
					self.txt_generacion.insert(INSERT,
						"{}\t{:5.5f}\n".format(registro[0], registro[2]),
						"periodo"
					)
					contador_periodo += 1;
					continue
			self.txt_generacion.insert(INSERT,
				"{}\t{:5.5f}\n".format(registro[0], registro[2])
			)
		self.txt_generacion.tag_config("periodo", foreground="red")




		"""for registro in generador.get_historico():
			self.txt_generacion.insert(
				INSERT, "{}\t{:5.5f}\n".format(registro[0], registro[2])
			)"""

			#self.txt_generacion.insert(INSERT, generador.str_historico())

	def limpiar(self):
		"""Limpia el campo de números generados"""
		self.txt_generacion.delete("1.0", END)

	def analizar_periodo(self):
		"""
			Usa una analizadorGenerador para encontrar
			el periodo

			Returns: (bool, str, [int, int]): flag de si encontró periodo,
				Una cadena de texto con un mensaje sobre el resultado del analisis
		"""
		analizador = AnalizadorGenerador()
		analisis = analizador.analizar(self.generador)
		str_analisis = "La longituddel periodo de los números a generar es de {}\nSi aún así deseas continuar, ignora este mensaje.".format(
			analisis[0])
		flag = False
		#si es -1, no hay periodo
		if analisis[0] == -1:
			flag = False
		else:
			flag = True
		return (flag, str_analisis, analisis)

	def get_is_generador_usado(self):
		return self.is_generador_usado

	def get_is_auto_run(self):
		return self.is_auto_run

	def reiniciar(self):
		pass
