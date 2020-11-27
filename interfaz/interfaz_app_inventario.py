#!/usr/bin/python3.9

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

from interfaz.ventana import *

from app_inventario import SimInventario
from distribuidor_tabla import DistribuidorDeTabla

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10
w = 10

class InterfazAppInventario(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master

		self.q = None
		self.w = None

		self.init_interfaz()

	def init_interfaz(self):
		self.add_labels()
		self.add_entradas()

	def add_labels(self):
		ttk.Label(self, text="Q:").grid(
			column = 0, row = 0, padx = p_x_l, pady = p_y)
		ttk.Label(self, text="R:").grid(
			column = 0, row = 1, padx = p_x_l, pady = p_y)

	def add_entradas(self):
		self.q = ttk.Entry(self, width=w)
		self.q.grid(
			column = 1, row = 0, padx = 0, pady = 0)
		self.r = ttk.Entry(self, width=w)
		self.r.grid(
			column = 1, row = 1, padx = 0, pady = 0)