import tkinter as tk
from PIL import ImageTk, Image
import os

class PantallaAyudaAFD(tk.Toplevel):

    def __init__(self, parent):
        super().__init__()
        

        self.geometry("6400x4800")
        self.title("Que es un Automata Finito Determinista?")

        tk.Label(self, text="Nombre:").grid(row = 0, column = 0)
        tk.Label(self, text="AFD2").grid(row = 0, column = 1)

        tk.Label(self, text="Estados:").grid(row = 1, column = 0)
        tk.Label(self, text="A, B, C").grid(row = 1, column = 1)

        tk.Label(self, text="Alfabeto:").grid(row = 2, column = 0)
        tk.Label(self, text="0, 1").grid(row = 2, column = 1)

        tk.Label(self, text="Estado Inicial:").grid(row = 3, column = 0)
        tk.Label(self, text="A").grid(row = 3, column = 1)

        tk.Label(self, text="Estados de Aceptacion:").grid(row = 4, column = 0)
        tk.Label(self, text="A, C").grid(row = 4, column = 1)

        tk.Label(self, text="Transiciones:").grid(row = 5, column = 0)
        tk.Label(self, text="A,1;A").grid(row = 5, column = 1)
        tk.Label(self, text="A,0;B").grid(row = 5, column = 2)
        tk.Label(self, text="B,1;B").grid(row = 6, column = 1)
        tk.Label(self, text="C,1;C").grid(row = 6, column = 2)
        tk.Label(self, text="C,0;C").grid(row = 7, column = 1)
        tk.Label(self, text="B,0;C").grid(row = 7, column = 2)

        

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__), "../imagenes/ayudaAFD.PNG"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((800, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.grid(row = 8, column = 1)
        #tk.Label(self, text="Un Autómata Finito No Determinista (AFN) es un modelo teórico utilizado en la teoría de la computación y en la teoría de lenguajes formales. No acepta cadenas vacias.").grid(row = 9, column = 0)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).grid(row = 10, column = 1)

    def cerrar_ventana(self):
        PantallaAyudaAFD.destroy(self)
        