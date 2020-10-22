#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

import sys

import generador as gen
from interfaz.ventana import Ventana


def main():

	datos = None
	if len(sys.argv) > 1:
		datos = {}
		datos["semilla"] = int(sys.argv[1])
		datos["constante"] = int(sys.argv[2])
		datos["multiplicador"] = int(sys.argv[3])
		datos["modulo"] = int(sys.argv[4])
		datos["tamano"] = int(sys.argv[5])

	root = Tk()
	root.geometry("868x600")
	app = Ventana(root, args=datos)
	root.mainloop()

if __name__ == '__main__':
	main()
