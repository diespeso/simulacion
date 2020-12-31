#!/usr/bin/python3.9

from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox

from interfaz.ventana import *

from app_red import Red
from app_red import Nodo

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10
w = 10

class InterfazAppRed(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.numeros = None

		self.red = None

		self.factores = None
		self.set_factores({'a': 0.7,
			'b': 1,
			'c': 1,
			'd': 0.8,
			'e': 0.9})

		self.mb_paquete = None
		self.mb_archivo = None

		self.entry_mb_paquete = None
		self.entry_mb_archivo = None

		self.btn_simular = None

		self.txt_registros = None
		self.btn_registrar = None

		self.interfaz_nodos = None # diccionario de interfaz de nodos

		self.init_interfaz()

	def rellenar(self, numeros):
		self.numeros = numeros

	def set_factores(self, factores):
		self.factores = factores

	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

		self.add_interfaz_nodos()

		self.btn_registrar = ttk.Button(self, text="Registrar", command=self.registrar_actual)
		self.btn_registrar.grid(column = 0, row = 7, padx = p_x_l, pady = p_y, columnspan = 2)

		self.btn_simular = ttk.Button(self, text="Simular",command=self.simular)
		self.btn_simular.grid(column = 3, row = 8, padx = p_x_l, pady = p_y )
	
	def add_labels(self):
		ttk.Label(self, text="mb/paquete").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="mb archivo").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Registros").grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y, columnspan = 2)
		ttk.Label(self, text="Nodo").grid(
			column = 2, row = 2, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Tipo").grid(
			column = 3, row = 2, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Estabilidad de conexión").grid(
			column = 4, row = 2, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="$ paquetes pérdidos").grid(
			column = 5, row = 2, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Nodo A").grid(
			column = 2, row = 3, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Nodo B").grid(
			column = 2, row = 4, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Nodo C").grid(
			column = 2, row = 5, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Nodo D").grid(
			column = 2, row = 6, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Nodo E").grid(
			column = 2, row = 7, padx = p_x_l, pady = p_y)

	def add_entradas(self):
		self.entry_mb_paquete = ttk.Entry(self, width=w)
		self.entry_mb_paquete.grid(column = 1, row = 1, padx = p_x_l, pady = p_y)

		self.txt_registros = scrolledtext.ScrolledText(self,
			width=25, height=10)
		self.txt_registros.grid(column = 0, row = 3, padx = p_x_l, pady = p_y, rowspan=4, columnspan=2)

		self.entry_mb_archivo = ttk.Entry(self, width=w)
		self.entry_mb_archivo.grid(column = 1, row = 0, padx = p_x_l, pady = p_y)

	def add_interfaz_nodos(self):
		self.interfaz_nodos = {}
		for letra in ["a", "b", "c", "d", "e"]:
			self.interfaz_nodos[letra] = {}
			self.interfaz_nodos[letra]["tipo"] = ttk.Combobox(self, width=6, values=["Alfa", "Beta", "Gamma"])
			if self.factores:
				self.interfaz_nodos[letra]["factor"] = ttk.Label(self, text=str(round(float(self.factores[letra] * 100), 1)) + "%")
		col = 3
		r = 3
		r_factor = 3
		for letra_nodo in self.interfaz_nodos.items():
			letra = letra_nodo[0]
			nodo = letra_nodo[1]
			
			if letra == "a":
				nodo["tipo"].grid(column=col, row=r, padx=p_x_l, pady=p_y)
				nodo["factor"].grid(column=col+1, row=r, padx=p_x_l, pady=p_y)
			elif letra == "b":
				nodo["tipo"].grid(column=col, row=r+1, padx=p_x_l, pady=p_y)
				nodo["factor"].grid(column=col+1, row=r+1,padx=p_x_l, pady=p_y)
			elif letra == "c":
				nodo["tipo"].grid(column=col, row=r+2, padx=p_x_l, pady=p_y)
				nodo["factor"].grid(column=col+1, row=r+2, padx=p_x_l, pady=p_y)
			elif letra == "d":
				nodo["tipo"].grid(column=col, row=r+3, padx=p_x_l, pady=p_y)
				nodo["factor"].grid(column=col+1, row=r+3, padx=p_x_l, pady=p_y)
			elif letra == "e":
				nodo["tipo"].grid(column=col, row=r+4, padx=p_x_l, pady=p_y)
				nodo["factor"].grid(column=col+1, row=r+4, padx=p_x_l, pady=p_y)
		"""
		print(self.interfaz_nodos.keys())
		for nodo in self.interfaz_nodos.values():
			nodo["tipo"].grid(column=col, row = r, padx = p_x_l, pady = p_y)
			r += 1
			nodo["factor"].grid(column=col + 1, row = r_factor, padx = p_x_l, pady = p_y)
			r_factor += 1
		"""
	
	def registrar_actual(self):
		print("todo: registrar")
		#self.master.master.root.geometry("920x920")

	def simular(self):
		self.nodos = {}
		try:
			"""
			self.mb_paquete = int(self.entry_mb_paquete.get())
			self.mb_archivo = int(self.entry_mb_archivo.get())

			print(self.interfaz_nodos["a"]["tipo"].get())
			print(self.nodos)
			"""
			self.mb_paquete = int(self.entry_mb_paquete.get())
			self.mb_archivo = int(self.entry_mb_archivo.get())

			if self.mb_archivo < self.mb_paquete:
				messagebox.showwarning(message="El tamaño de archivo\ndebe ser mayor al\ntamaño de paquete")
				return
			if self.mb_paquete > 5:
				messagebox.showwarning(message="El tamaño de paquete máximo es 5mb")
				return
			if self.mb_archivo <= 1:
				messagebox.showwarning(message="Tamaño de archivo demasiado pequeño")
				return
			if self.mb_paquete < 1:
				messagebox.showwarning(message="Tamaño de paquete demasiado pequeño")
				return
			
			for letra in ["a", "b", "c", "d", "e"]:
				self.nodos[letra] = self.interfaz_nodos[letra]["tipo"].get()
				if self.nodos[letra] == "": #si falla el parse
					messagebox.showwarning(message="Introduce todos los tipos de nodo.")
					return
		except Exception as e:
			messagebox.showwarning(message="datos incorrectos.")
		
		self.red = Red(self.mb_archivo, self.mb_paquete)
		self.red.set_nodos(
			Nodo(self.nodos["a"]),
			Nodo(self.nodos["b"]),
			Nodo(self.nodos["c"]),
			Nodo(self.nodos["d"]),
			Nodo(self.nodos["e"])
			)

		self.red.simular(self.numeros)
		self.add_lbl_paquetes()

	def add_lbl_paquetes(self):
		col = 5
		r = 3
		for letra in ["a", "b", "c", "d", "e"]:
			perdidos = self.red.get_paquetes_perdidos(letra)
			costo = self.red.nodos[letra].costo_perdida
			total = perdidos * costo

			self.interfaz_nodos[letra]["paquetes"] = ttk.Label(
				self, text="{}px${:.3f}=${:.3f}".format(
					perdidos, costo, total)
				).grid(column = col, row = r, padx = p_x_l, pady = p_y
				)
			r += 1