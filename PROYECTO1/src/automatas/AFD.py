import tkinter as tk
import graphviz
from PIL import ImageTk, Image
import os

class AFD(tk.Toplevel):
    def __init__(self, automataAFD):
        super().__init__()
        self.geometry("640x480")
        self.title("Pantalla de Automata Finito No Determinista")
        #PantallaCrearAFN.get()
        f = graphviz.Graph()

        # Configuración de la fuente
        f.node_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        f.edge_attr['fontname'] = 'Helvetica, Arial, sans-serif'
        print(automataAFD[0])
        print(automataAFD[1])
        print(automataAFD[2])
        print(automataAFD[3])
        print(automataAFD[4])
        print(automataAFD[5])
        print(automataAFD[5][0])
        print(automataAFD[5][0][0])
        print(automataAFD[5][0][1])
        print(automataAFD[5][0][2]) 
    
        #Definición de los nodos del círculo (todo tipo de estado
        f.attr('node', shape = 'circle')
        for estado in automataAFD[1]:
            if estado not in automataAFD[4]:
                f.node(estado)
            else: #Definición de los nodos dobles circulares (estados de aceptacion)
                f.attr('node', shape ='doublecircle')
                f.node(estado)
                f.attr('node', shape='circle')


        # Definición de las aristas
        #para cada transicion ejecutar: f.edge(estadoInicial, estadoFinal, label = valorTransicion)
        #Lista de transiciones en formato (estado1, valor, estado2), (estado1, valor, estado2) ...
        for transicion in automataAFD[5]:
            automataAFD[5][0][0], automataAFD[5][0][1], automataAFD[5][0][2] = transicion
            f.edge(automataAFD[5][0][0], automataAFD[5][0][2], label=automataAFD[5][0][1])


        f.render(automataAFD[0], directory="output", format="png", cleanup=True)
        
        frame = tk.Frame(self, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Cargar la imagen
        imagen = Image.open(os.path.join(os.path.dirname(__file__), "../../../output/"+automataAFD[0]+".png"))

        # Redimensionar la imagen si es necesario
        imagen = imagen.resize((600, 400))

        # Convertir la imagen a un objeto PhotoImage
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Create a Label Widget to display the text or Image
        label = tk.Label(self, image = self.imagen_tk)
        label.pack()
