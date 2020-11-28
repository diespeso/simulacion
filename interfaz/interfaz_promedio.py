#!/usr/bin/python3.9

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from prueba_promedio import PruebaPromedio

from exceptions import BadAlfaException
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
	def __init__(self, master):
		Frame.__init__(self, master)
		self.entrada_promedio = None
		self.entrada_des_estandar = None
		self.entrada_z0 = None
		self.entrada_alfa = None
		self.btn_probar = None

		self.prueba_promedio = None

		self.init_interfaz()


	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

		self.btn_probar = ttk.Button(self, text="Probar", command=self.capturar)
		self.btn_probar.grid(
			column=0, row = 2, padx = p_x_l, pady = p_y)

		self.txt_conclusion = Text(self, height=1)
		self.txt_conclusion.grid(
			column=1, columnspan = 4,
			row=3, padx = p_x_l, pady = p_y + 10)

	def add_labels(self):
		ttk.Label(self, text="Promedio").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Desv. Estándar").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Z0").grid(
			column = 4, row = 0, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="nivel significancia").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Zalfa/2").grid(
			column = 1, row = 2, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Conclusión:").grid(
			column = 0, row = 3, padx = p_x_l, pady = p_y + 10)

	def add_entradas(self):
		self.entrada_promedio = ttk.Entry(self, width=15)
		self.entrada_promedio.grid(
			column = 1, row = 0, padx = 0, pady = 0)

		self.entrada_des_estandar = ttk.Entry(self, width=15)
		self.entrada_des_estandar.grid(
			column = 3, row = 0, padx = 0, pady = 0)

		self.entrada_z0 = ttk.Entry(self, width=15)
		self.entrada_z0.grid(
			column = 5, row = 0, padx = 0, pady = 0)

		self.entrada_alfa = ttk.Entry(self, width=15)
		self.entrada_alfa.grid(
			column = 1, row = 1, padx = 0, pady = 0)

		self.entrada_z_alfa = ttk.Entry(self, width=15)
		self.entrada_z_alfa.grid(
			column = 2, row = 2, padx= 0, pady = 0)

	def capturar(self):
		self.reiniciar_temporales()
		self.abrir_entradas()
		captura = self.validar_entradas()
		if captura:
			z_alfa = float(self.entrada_alfa.get())
			resultado = self.prueba_promedio.probar(z_alfa)
			if resultado:
				self.txt_conclusion.insert("0.0", "Los números están distribuidos uniformemente.")
			else:
				self.txt_conclusion.insert("0.0", "Los números no están distribuidos uniformemente.")
			self.entrada_z_alfa.insert(0, str(self.prueba_promedio.z_alfa_mitad))
			self.cerrar_entradas()


	def validar_entradas(self):
		captura = {}
		try:
			captura["z_alfa"] = float(self.entrada_alfa.get())
			if captura["z_alfa"] >= 1.0:
				raise BadAlfaException(capturar["z_alfa"])
		except Exception as e:
			messagebox.showwarning(message="Entrada inválida", title="Error de entrada")
			return None
		except BadAlfaException as e:
			messagebox.showwarning(message=e.__str__(), title="Alfa incorrecto")
		return captura

	def abrir_entradas(self):
		self.entrada_promedio.config(state="enabled")
		self.entrada_des_estandar.config(state="enabled")
		self.entrada_z0.config(state="enabled")
		self.entrada_z_alfa.config(state="enabled")

	def cerrar_entradas(self):
		self.entrada_promedio.config(state="disabled")
		self.entrada_des_estandar.config(state="disabled")
		self.entrada_z0.config(state="disabled")
		self.entrada_z_alfa.config(state="disabled")

	def reiniciar(self):
		""" borra los datos de todos los campos autogenerados
		"""
		self.abrir_entradas()
		self.entrada_promedio.delete(0, END);
		self.entrada_des_estandar.delete(0, END);
		self.entrada_z0.delete(0, END);
		self.entrada_z_alfa.delete(0, END);
		self.txt_conclusion.delete("0.0", END);
		self.cerrar_entradas()

	def reiniciar_temporales(self):
		self.abrir_entradas()
		self.entrada_z_alfa.delete(0, END)
		self.txt_conclusion.delete("0.0", END)
		self.cerrar_entradas()

	def rellenar(self, numeros):
		""" toma una generación de números y crear una prueba
		de promedio, pero no la corre, solo rellena la interfaz
		con los datos
		"""
		self.reiniciar()
		self.abrir_entradas()
		self.prueba_promedio = PruebaPromedio(numeros)
		self.entrada_promedio.insert(0, str(self.prueba_promedio.mu))

		self.entrada_des_estandar.insert(0, str(self.prueba_promedio.sigma))

		self.entrada_z0.insert(0, str(self.prueba_promedio.z0))
		self.cerrar_entradas()
