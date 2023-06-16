import tkinter as tk
from PIL import ImageTk, Image
import os

class PantallaAyudaOE(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()

        self.geometry("6400x4800")
        self.title("Que es una Optimizacion de Estados?")

        tk.Label(self, text="Nombre:").grid(row = 0, column = 0)
        tk.Label(self, text="AFD2").grid(row = 0, column = 1)

        tk.Label(self, text="Estados:").grid(row = 1, column = 0)
        tk.Label(self, text="q0, q1").grid(row = 1, column = 1)

        tk.Label(self, text="Alfabeto:").grid(row = 2, column = 0)
        tk.Label(self, text="0, 1").grid(row = 2, column = 1)

        tk.Label(self, text="Estado Inicial:").grid(row = 3, column = 0)
        tk.Label(self, text="q0").grid(row = 3, column = 1)

        tk.Label(self, text="Estados de Aceptacion:").grid(row = 4, column = 0)
        tk.Label(self, text="q0").grid(row = 4, column = 1)

        tk.Label(self, text="Transiciones:").grid(row = 5, column = 0)
        tk.Label(self, text="q0,0;q0").grid(row = 5, column = 1)
        tk.Label(self, text="q0,1;q1").grid(row = 5, column = 2)
        tk.Label(self, text="q1,0;q0").grid(row = 6, column = 1)
        tk.Label(self, text="q1,1;q1").grid(row = 6, column = 2)

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__), "../imagenes/ayudaOE.PNG"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((600, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.grid(row = 7, column = 1)
        #tk.Label(self, text="Un AFD minimizado es la versión simplificada de lo que fue un AFD con estados redundantes entre sí. Utilizando algoritmos es posible encontrar estados equivalentes para formar un AFD mínimo.").grid(row = 8, column = 0)
        tk.Button(self, text="Regresar", width=100, height=5, command=self.cerrar_ventana).grid(row = 9, column = 1)

    def cerrar_ventana(self):
        PantallaAyudaOE.destroy(self)

        