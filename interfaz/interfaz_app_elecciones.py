from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

from app_elecciones import Votacion

from parser_tablas import leer_archivo
from distribuidor_tabla import DistribuidorDeTabla

p_x = 3
p_y = 3
p_x_l = 10
p_y_l = 10
w = 10

votantes = 100

class InterfazAppElecciones(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.txt_sector_uno = None
		self.txt_sector_dos = None
		self.txt_sector_tres = None
		self.txt_sector_cuatro = None
		self.txt_sector_cinco = None

		self.btn_simular = None

		self.votacion = None

		self.numeros = None

		self.init_interfaz()

	def init_interfaz(self):
		self.add_labels()

		self.btn_simular = ttk.Button(self, text="Simular", command=self.simular)
		self.btn_simular.grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y)

		self.txt_sector_uno = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_uno.grid(
			column = 0, row = 4, padx = p_x_l, pady = p_y)

		self.txt_sector_dos = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_dos.grid(
			column = 1, row = 4, padx = p_x_l, pady = p_y)

		self.txt_sector_tres = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_tres.grid(
			column = 2, row = 4, padx = p_x_l, pady = p_y)

		self.txt_sector_cuatro = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_cuatro.grid(
			column = 3, row = 4, padx = p_x_l, pady = p_y)

		self.txt_sector_cinco = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_cinco.grid(
			column = 4, row = 4, padx = p_x_l, pady = p_y)

	def simular(self):
		try: 
			probabilidades = DistribuidorDeTabla(
				leer_archivo("votos")
			)
		except Exception as e:
			messagebox.showwarning(message=e.__str__())
		if self.numeros:
			self.votacion = Votacion(votantes, probabilidades, self.numeros)
		else:
			messagebox.showwarning(message="No hay números en el generador")
			return
		self.votacion.simular()
		self.limpiar()
		self.txt_sector_uno.insert(INSERT,
			self.votacion.get_votos_str(1))
		self.txt_sector_dos.insert(INSERT,
			self.votacion.get_votos_str(2))
		self.txt_sector_tres.insert(INSERT,
			self.votacion.get_votos_str(3))
		self.txt_sector_cuatro.insert(INSERT,
			self.votacion.get_votos_str(4))
		self.txt_sector_cinco.insert(INSERT,
			self.votacion.get_votos_str(5))

	def set_numeros(self, numeros):
		self.numeros = numeros

	def limpiar(self):
		self.txt_sector_uno.delete("1.0", END)
		self.txt_sector_dos.delete("1.0", END)
		self.txt_sector_tres.delete("1.0", END)
		self.txt_sector_cuatro.delete("1.0", END)
		self.txt_sector_cinco.delete("1.0", END)

	def add_labels(self):
		ttk.Label(self, text="Clave").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="1: Creación y protección del empleo.  2. Atención a la seguridad.  3. Impulso al comercio y al turismo.  4. Prestación de servicios.\n" + 
			"5. Honestidad de los servidores.  6. Atención a la educación").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y,
			columnspan = 8)

		ttk.Label(self, text="Sector 1").grid(
			column = 0, row = 3, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 2").grid(
			column = 1, row = 3, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 3").grid(
			column = 2, row = 3, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 4").grid(
			column = 3, row = 3, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 5").grid(
			column = 4, row = 3, padx = p_x_l, pady = p_y)
