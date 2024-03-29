import tkinter as tk
from tkinter import ttk
from vistas.vistaECAFN import PantallaECAFN

class PantallaSeleccionarAFN(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent):
        super().__init__()
        self.pantallaParent=parent
        self.automataAFN=parent.pantallaParent.automatasCargadosAFN
        self.geometry("640x480")
        self.title("Pantalla Seleccionar AFN")

        automatas = [automata[0] for automata in self.automataAFN]
        self.combobox = ttk.Combobox(self, values=automatas)
        self.combobox.pack()
        tk.Button(self, text="Aceptar", width=100, height=5, command=self.abrir_ventanaECAFN).pack(expand=True)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).pack(expand=True)

    def cerrar_ventana(self):
        self.destroy()
        
    def abrir_ventanaECAFN(self):
        automataSeleccionado=self.combobox.get()
        for automataAFN in self.pantallaParent.pantallaParent.automatasCargadosAFN:
            if automataAFN[0] == automataSeleccionado:
                ventanaECAFN= PantallaECAFN(self, automataAFN)
                ventanaECAFN.grab_set()
            