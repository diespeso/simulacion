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

		self.votos_sector_uno = None
		self.votos_sector_dos = None
		self.votos_sector_tres = None
		self.votos_sector_cuatro = None
		self.votos_sector_cinco = None

		self.c_uno = None
		self.c_dos = None
		self.c_tres = None
		self.c_cuatro = None
		self.c_cinco = None

		self.entrada_votantes = None
		self.entrada_muestra = None

		self.btn_simular = None

		self.votacion = None

		self.votantes = None


		self.numeros = None

		self.primera_corrida = True #es para limpiar votos por sector
		self.primera_conclusiones = True
		self.init_interfaz()

	def init_interfaz(self):
		self.add_labels()

		self.btn_simular = ttk.Button(self, text="Simular", command=self.simular)
		self.btn_simular.grid(
			column = 0, row = 3, padx = p_x_l, pady = p_y)

		self.txt_sector_uno = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_uno.grid(
			column = 0, row = 6, padx = p_x_l, pady = p_y)

		self.txt_sector_dos = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_dos.grid(
			column = 1, row = 6, padx = p_x_l, pady = p_y)

		self.txt_sector_tres = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_tres.grid(
			column = 2, row = 6, padx = p_x_l, pady = p_y)

		self.txt_sector_cuatro = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_cuatro.grid(
			column = 3, row = 6, padx = p_x_l, pady = p_y)

		self.txt_sector_cinco = scrolledtext.ScrolledText(self,
			width = 12, height = 20)
		self.txt_sector_cinco.grid(
			column = 4, row = 6, padx = p_x_l, pady = p_y)

		self.entrada_votantes = ttk.Entry(self, width=15)
		self.entrada_votantes.grid(
			column = 1, row = 0, padx = p_x_l, pady = p_y)

		self.entrada_muestra = ttk.Entry(self, width=15)
		self.entrada_muestra.grid(
			column = 3, row = 0, padx = p_x_l, pady = p_y)

	def simular(self):
		votantes = None
		muestra = None
		try: 
			probabilidades = DistribuidorDeTabla(
				leer_archivo("votos")
			)
			votantes = int(self.entrada_votantes.get())
			muestra = round(float(self.entrada_muestra.get()), 2) #solo dos decimales

		except Exception as e:
			messagebox.showwarning(message=e.__str__())
		if not votantes or not muestra: #si falló el parsing
			return
		else:
			votantes = int(votantes * muestra)
		if votantes * 3 > len(self.numeros):
			messagebox.showwarning(message="Los números generados no son suficientes, faltan: {}".format(
				votantes * 3 - len(self.numeros) ))
			return
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

		self.add_numero_votantes()
		self.add_conclusiones()

	def add_numero_votantes(self):
		if self.primera_corrida:
			self.primera_corrida = False
		else:
			self.limpiar_numero_votantes()
		votos = self.votacion.votos_sector

		self.votos_sector_uno = ttk.Label(self, text="votos: {}".format(votos[1]))
		self.votos_sector_uno.grid(column = 0, row = 7, padx= p_x_l, pady = p_y)
		
		self.votos_sector_dos = ttk.Label(self, text="votos: {}".format(votos[2]))
		self.votos_sector_dos.grid(column = 1, row = 7, padx = p_x_l, pady = p_y)

		self.votos_sector_tres = ttk.Label(self, text="votos: {}".format(votos[3]))
		self.votos_sector_tres.grid(column = 2, row = 7, padx = p_x_l, pady = p_y)

		self.votos_sector_cuatro = ttk.Label(self, text="votos: {}".format(votos[4]))
		self.votos_sector_cuatro.grid(column = 3, row = 7, padx = p_x_l, pady = p_y)

		self.votos_sector_cinco = ttk.Label(self, text="votos: {}".format(votos[5]))
		self.votos_sector_cinco.grid(column = 4, row = 7, padx = p_x_l, pady = p_y)

	def limpiar_numero_votantes(self):
		self.votos_sector_uno.destroy()
		self.votos_sector_dos.destroy()
		self.votos_sector_tres.destroy()
		self.votos_sector_cuatro.destroy()
		self.votos_sector_cinco.destroy()

	def set_numeros(self, numeros):
		self.numeros = numeros

	def limpiar(self):
		self.txt_sector_uno.delete("1.0", END)
		self.txt_sector_dos.delete("1.0", END)
		self.txt_sector_tres.delete("1.0", END)
		self.txt_sector_cuatro.delete("1.0", END)
		self.txt_sector_cinco.delete("1.0", END)

	def add_labels(self):
		ttk.Label(self, text="Votantes:").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="% muestra:").grid(
			column = 2, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Clave").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="1: Creación y protección del empleo.  2. Atención a la seguridad.  3. Impulso al comercio y al turismo.  4. Prestación de servicios.\n" + 
			"5. Honestidad de los servidores.  6. Atención a la educación").grid(
			column = 0, row = 2, padx = p_x_l, pady = p_y,
			columnspan = 8)

		ttk.Label(self, text="Sector 1").grid(
			column = 0, row = 5, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 2").grid(
			column = 1, row = 5, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 3").grid(
			column = 2, row = 5, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 4").grid(
			column = 3, row = 5, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="Sector 5").grid(
			column = 4, row = 5, padx = p_x_l, pady = p_y)

		ttk.Label(self, text="Conclusiones").grid(
			column = 0, row = 8, padx = p_x_l, pady = p_y)

	def add_conclusiones(self):
		if self.primera_conclusiones:
			self.primera_conclusiones = False
		else:
			self.limpiar_conclusiones()
		

		sector_uno = self.votacion.analizar_sector(1)
		self.c_uno = ttk.Label(self, text="Corto plazo:\n{}, {}, {}\nLargo plazo:\n{}, {}".format(
			sector_uno[0], sector_uno[1], sector_uno[2], sector_uno[3],
			sector_uno[4]))
		self.c_uno.grid(column = 0, row = 9, padx = p_x_l, pady = p_y)

		sector_dos = self.votacion.analizar_sector(2)
		self.c_dos = ttk.Label(self, text="Corto plazo:\n{}, {}, {}\nLargo plazo:\n{}, {}".format(
			sector_dos[0], sector_dos[1], sector_dos[2], sector_dos[3],
			sector_dos[4]))
		self.c_dos.grid(column = 1, row = 9, padx = p_x_l, pady = p_y)

		sector_tres = self.votacion.analizar_sector(3)
		self.c_tres = ttk.Label(self, text="Corto plazo:\n{}, {}, {}\nLargo plazo:\n{}, {}".format(
			sector_tres[0], sector_tres[1], sector_tres[2], sector_tres[3],
			sector_tres[4]))
		self.c_tres.grid(column = 2, row = 9, padx = p_x_l, pady = p_y)

		sector_cuatro = self.votacion.analizar_sector(4)
		self.c_cuatro = ttk.Label(self, text="Corto plazo:\n{}, {}, {}\nLargo plazo:\n{}, {}".format(
			sector_cuatro[0], sector_cuatro[1], sector_cuatro[2], sector_cuatro[3],
			sector_cuatro[4]))
		self.c_cuatro.grid(column = 3, row = 9, padx = p_x_l, pady = p_y)

		sector_cinco = self.votacion.analizar_sector(5)
		self.c_cinco = ttk.Label(self, text="Corto plazo:\n{}, {}, {}\nLargo plazo:\n{}, {}".format(
			sector_cinco[0], sector_cinco[1], sector_cinco[2], sector_cinco[3],
			sector_cinco[4]))
		self.c_cinco.grid(column = 4, row = 9, padx = p_x_l, pady = p_y)

	def limpiar_conclusiones(self):
		self.c_uno.destroy()
		self.c_dos.destroy()
		self.c_tres.destroy()
		self.c_cuatro.destroy()
		self.c_cinco.destroy()