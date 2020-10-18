#!/usr/bin/python3

from tkinter import *;
import generador as gen;

def uwu():
	print("uwu, bye")

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Pseudoaleatorio")
		self.pack(fill=BOTH, expand=1)
		quitButton = Button(self, text="Quit", command=uwu)

		quitButton.place(x=0, y=0)

		text = Text()
		text.insert(INSERT, "esto es un texto")
		text.place(x=32, y=32)

def main():
	root = Tk()
	root.geometry("400x300")
	app = Window(root)
	root.mainloop()

if __name__ == '__main__':
	main()
