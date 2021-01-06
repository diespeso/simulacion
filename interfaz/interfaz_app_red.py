#!/usr/bin/python3.9

from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox

from interfaz.ventana import *

from app_red import Red
from app_red import Nodo
from app_red import to_min_sec

p_x = 3
p_y = 3
p_x_l = 10 #p_x largos
p_y_l = 10
w = 10

precision = 3

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

        self.registros = []

        self.mb_paquete = None
        self.mb_archivo = None

        self.entry_mb_paquete = None
        self.entry_mb_archivo = None
        self.entry_total = None

        self.lbl_total = None

        self.btn_simular = None
        
        self.txt_conclusion = None

        self.txt_registros = None
        self.btn_registrar = None

        self.costo_total = 0.0

        self.primera_vez = True
        
        self.optimo = None

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
        self.btn_simular.grid(column = 4, row = 8, padx = p_x_l, pady = p_y )
    
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
        ttk.Label(self, text="$ Paquetes Pérdidos").grid(
            column = 5, row = 2, padx = p_x_l, pady = p_y)
        ttk.Label(self, text="$ Tiempo").grid(
            column = 6, row = 2, padx = p_x_l, pady = p_y)

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

        ttk.Label(self, text="$ Total").grid(
            column = 3, row = 9, padx = p_x_l, pady = p_y)
            
        ttk.Label(self, text="Conclusión: ").grid(
            column = 0, row = 10, padx = p_x_l, pady = p_y)

    def add_entradas(self):
        self.entry_mb_paquete = ttk.Entry(self, width=w)
        self.entry_mb_paquete.grid(column = 1, row = 1, padx = p_x_l, pady = p_y)

        self.txt_registros = scrolledtext.ScrolledText(self,
            width=25, height=10)
        self.txt_registros.grid(column = 0, row = 3, padx = p_x_l, pady = p_y, rowspan=4, columnspan=2)

        self.entry_mb_archivo = ttk.Entry(self, width=w)
        self.entry_mb_archivo.grid(column = 1, row = 0, padx = p_x_l, pady = p_y)

        self.entry_total = ttk.Entry(self, width=w)
        self.entry_total.grid(column = 4, row = 9, padx = p_x_l, pady = p_y)
        
        self.txt_conclusion = scrolledtext.ScrolledText(self, width=w *7 + 5, height = 2)
        self.txt_conclusion.grid(column = 1, row = 10, padx = p_x_l, pady = p_y, columnspan = 7)

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
        #TODO: Lógica de registro
        #(alfa, alfa, alfa, alfa, alfa) = $0.467
        self.txt_registros.delete("1.0", END)
        nodos = self.nodos
        costo = self.costo_total
        nuevo ="(A: {}, B: {}, C: {}, D: {}, E: {}) = ${:.4f}".format(
            nodos["a"], nodos["b"], nodos["c"], nodos["d"], nodos["e"],
            costo)
        if not (nuevo in self.get_registros_str().split("\n")):
            #si no está registrado
            print(self.get_registros_str().split("\n"))
            self.add_registro(self.nodos, self.costo_total, self.red.get_tiempo_total())

        print(self.get_registros_str())
        
        if len(self.registros) == 1:
            self.txt_registros.insert(INSERT, self.get_registros_str())
            return

        min = self.registros[0]["costo"]
        reg = self.registros[0]

        #encontrar el mas optimo
        for i in range(0, len(self.registros)):
            if self.registros[i]["costo"] < min:
                min = self.registros[i]["costo"]
                reg = self.registros[i]

        for i in range(0, len(self.registros)):
            if self.registros[i] == reg:
                self.txt_registros.insert(INSERT, self.get_registro_str(i) + "\n", "optimo")
            else:
                self.txt_registros.insert(INSERT, self.get_registro_str(i) + "\n")
        self.txt_registros.tag_config("optimo", foreground="green")
        self.optimo = reg
        self.add_conclusion()
        #self.txt_registros.insert(INSERT, self.get_registros_str())

    def add_registro(self, nodos, costo, tiempo):
        self.registros.append({"nodos": nodos, "costo": costo, "tiempo": tiempo})

    def get_registros_str(self):
        r = ""
        for i in range(0, len(self.registros)):
            r += self.get_registro_str(i)
            r += "\n"
        return r

    def get_registro_str(self, index):
        nodos = self.registros[index]["nodos"]
        costo = self.registros[index]["costo"]

        return "(A: {}, B: {}, C: {}, D: {}, E: {}) = ${:.4f}".format(
            nodos["a"], nodos["b"], nodos["c"], nodos["d"], nodos["e"],
            costo)

    def get_registro(self, indice):
        return self.registros[indice]

    def generar_conclusion(self):
        pass

    def simular(self):
        #borrar datos visuales de la simulación anterior
        self.reiniciar()
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
        self.add_lbl_tiempo()
        self.add_lbl_total()

        if self.primera_vez:
            self.primera_vez = False

    def reiniciar(self):
        self.limpiar()
        self.costo_total = 0.0

    def limpiar(self):
        if not self.primera_vez:
            for letra in ["a", "b", "c", "d", "e"]:
                self.interfaz_nodos[letra]["paquetes"].destroy()
                self.interfaz_nodos[letra]["tiempo"].destroy()
            self.entry_total.delete(0, 'end')
            self.txt_conclusion.delete("1.0", END)
    def add_lbl_paquetes(self):
        col = 5
        r = 3
        for letra in ["a", "b", "c", "d", "e"]:
            perdidos = self.red.get_paquetes_perdidos(letra)
            costo = self.red.nodos[letra].costo_perdida
            total = perdidos * costo
            self.costo_total += total

            self.interfaz_nodos[letra]["paquetes"] = ttk.Label(
                self, text="{}px${:.3f}=${:.4f}".format(
                    perdidos, costo, total)
                )
            self.interfaz_nodos[letra]["paquetes"].grid(column = col, row = r, padx = p_x_l, pady = p_y
                )
            r += 1

    def add_lbl_tiempo(self):
        col = 6
        r = 3
        for letra in ["a", "b", "c", "d", "e"]:
            tiempo = to_min_sec(self.red.tiempos[letra])
            costo = self.red.nodos[letra].costo_electrico
            total = tiempo[0] * costo #minutos
            total += tiempo[1] * costo / 60 #segundos
            total = round(total, precision)
            self.costo_total += total

            self.interfaz_nodos[letra]["tiempo"] = ttk.Label(
                self, text="{}min{}sx${:.3f}=${:.4f}".format(
                    tiempo[0].__str__(), tiempo[1].__str__(), costo, total
                    )
            )
            self.interfaz_nodos[letra]["tiempo"].grid(column = col, row = r, padx = p_x_l, pady = p_y)
            r += 1

    def add_lbl_total(self):
        """Añade el label que muestra el costo total
        """
        self.entry_total.insert(0, "${:.4f}".format(round(self.costo_total, precision)))

    def add_conclusion(self):
        print("optimo: ", self.optimo)
        if self.optimo:
            tim = self.optimo["tiempo"]
            min = tim[0]
            sec = tim[1]

            nodos = self.optimo["nodos"]
            txt_nodos = "A: {}, B: {}, C: {}, D: {}, E: {}".format(
                nodos["a"], nodos["b"], nodos["c"], nodos["d"], nodos["e"])
            conclusion = "La mejor configuración es {}, con un costo de ${:.4f} y un tiempo de {}min {}s".format(txt_nodos, self.optimo["costo"], min, sec)
            self.txt_conclusion.insert(INSERT, conclusion)
        
