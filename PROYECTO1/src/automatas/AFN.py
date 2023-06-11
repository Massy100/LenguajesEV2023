import tkinter as tk
import graphviz
from PIL import ImageTk, Image
import os
#from vistas.vistaCrearAFN import PantallaCrearAFN

class AFN(tk.Toplevel):
    def automataFN(self):
        #PantallaCrearAFN.get()
        f = graphviz.Graph()

        # Configuración de la fuente
        f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'
    
        # Definición de los nodos de doble círculo
        f.attr('node', shape='doublecircle')
        f.node("0")
        f.node("3")
        f.node("4")
        f.node("8")

        # Definición de los nodos circulares
        f.attr('node', shape='circle')
        f.node("1")
        f.node("2")
        f.node("5")
        f.node("6")
        f.node("7")

        # Definición de las aristas
        f.edge("0", "2", label='SS(B)')
        f.edge("0", "1", label='SS(S)')
        f.edge("1", "3", label='S($end)')
        f.edge("2", "6", label='SS(b)')
        f.edge("2", "5", label='SS(a)')
        f.edge("2", "4", label='S(A)')
        f.edge("5", "7", label='S(b)')
        f.edge("5", "5", label='S(a)')
        f.edge("6", "6", label='S(b)')
        f.edge("6", "5", label='S(a)')
        f.edge("7", "8", label='S(b)')
        f.edge("7", "5", label='S(a)')
        f.edge("8", "6", label='S(b)')
        f.edge("8", "5", label='S(a)')


        f.render('automata', directory="output", format="png", cleanup=True)
        
        frame = tk.Frame(self, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__), "../../../output/automata.png"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((600, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Create a Label Widget to display the text or Image
        label = tk.Label(self, image = self.imagen_tk)
        label.pack()


