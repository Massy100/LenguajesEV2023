import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PantallaGenerarOE(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFD=parent.pantallaParent.automatasCargadosAFD
        self.geometry("640x480")
        self.title("Pantalla Generar Reporte OE")

        tk.Label(self, text="Nombre AFD a Optimizar").pack(expand=True)
        automatas = [automata[0] for automata in self.automataAFD]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()

        tk.Button(self, text="Aceptar", width=100, height=5).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()