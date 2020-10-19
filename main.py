#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

import generador as gen
from interfaz.ventana import Ventana



def main():
	root = Tk()
	root.geometry("960x640")
	app = Ventana(root)
	root.mainloop()

if __name__ == '__main__':
	main()
