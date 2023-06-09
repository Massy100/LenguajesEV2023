import tkinter as tk
from tkinter import ttk
from vistas.vistaAFN import PantallaAFN
from vistas.vistaAFD import PantallaAFD
from vistas.vistaOE import PantallaOE
from vistas.vistaCA import PantallaCA
from datos import Datos


class App(tk.Tk):
    def __init__(self, valor_obtenido):
        super().__init__()

        self.geometry("640x480")
        self.title("Pantalla de Inicio")

        # en label el primer espacio es donde se va a agregar y el segundo es el texto
        tk.Label(self, text="PROYECTO 1", bg="#B0DBD2").pack(expand=True)

        tk.Label(self, text=f"Datos Personales: {valor_obtenido}").pack(expand=True)

        tk.Button(
            self,
            text="Automata Finito No Determinista",
            width=100,
            height=5,
            command=self.abrir_ventanaAFN,
        ).pack(expand=True)

        tk.Button(
            self,
            text="Automata Finito Determinista",
            width=100,
            height=5,
            command=self.abrir_ventanaAFD,
        ).pack(expand=True)
        tk.Button(
            self,
            text="Optimizacion de Estados",
            width=100,
            height=5,
            command=self.abrir_ventanaOE,
        ).pack(expand=True)
        tk.Button(
            self,
            text="Cargar Archivos",
            width=100,
            height=5,
            command=self.abrir_ventanaCA,
        ).pack(expand=True)
        tk.Button(
            self, text="Salir", width=100, height=5, command=exit
        ).pack(expand=True)

    def abrir_ventanaAFN(self):
        ventanaAFN = PantallaAFN(self)
        ventanaAFN.grab_set()

    def abrir_ventanaAFD(self):
        ventanaAFD = PantallaAFD(self)
        ventanaAFD.grab_set()

    def abrir_ventanaOE(self):
        ventanaOE = PantallaOE(self)
        ventanaOE.grab_set()

    def abrir_ventanaCA(self):
        ventanaCA = PantallaCA(self)
        ventanaCA.grab_set()

if __name__ == "__main__":
    # aqui van los labels con la info personal
    objeto = Datos(
        "Ana Massielle", "Coti Rodas", "Lenguajes formales", "'P'", 202031873, 3348842920901
    )
    app = App(str(objeto))
    app.mainloop()
