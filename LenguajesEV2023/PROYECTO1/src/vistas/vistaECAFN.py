import tkinter as tk
import tkinter.messagebox as mbox

class PantallaECAFN(tk.Toplevel):
    pantallaParent = None
    def __init__(self, parent, automataAFN):
        super().__init__()
        self.pantallaParent=parent
        #self.automataAFN=parent.pantallaParent.pantallaParent.pantallaParent.automatasCargadosAFN
        self.automata=automataAFN
        self.geometry("640x480")
        self.title("Pantalla de Evaluar Cadena AFN")
        self.cadena=tk.Entry(self)
        self.cadena.pack(expand=True)
        tk.Button(self, text="Solo Validar", width=100,height=5, command=self.validar).pack(expand=True)
        tk.Button(self, text="Ruta", width=100,height=5, command=self.ruta).pack(expand=True)

    def crear_entry(self):
<<<<<<< HEAD
        texto = list(self.cadena.get())
        estado_actual = self.automata[3] #el estado actual comienza con el estado inicial
        estado_anterior=[]
        accept=False #acceptar cadena
        print(".......START.........")
        for simbolo in texto:
            if estado_actual not in self.automata[1]:
                return False #El estado actual no se encuentra en los estados posibles
            
            if simbolo not in self.automata[2]: #luego verifica si esta dentro del alfabeto
                return False #La cadena se encuentra fuera del alfabeto establecido
                
            end=True #finalizar
            for transicion in self.automata[5]:
                if transicion[0] == estado_actual and transicion[1] == simbolo:
                    if estado_anterior == transicion and transicion [0] != transicion[2]:
                        return False # Repitio la instruccion sin que haya repitencia
                    else:
                        print("Me movi de: "+estado_actual+" con: "+simbolo+" hacia : "+transicion[2])
                        
                        estado_anterior=transicion
                        estado_actual = transicion[2]
                        end=False #decimos que aun no ha terminado
                        break;             
            
            if end: #Si no se encontro la transicion finaliza
                return False
            
            if estado_actual in self.automata[4]: #Verificamos si se encuentra en algun estado de aceptacion
                accept = True
            else:
                accept = False

        print("Estado final: "+estado_actual)
        
        return accept  # Retorna estado de aceptación si no hay errores
=======
        texto = self.cadena.get()
        estado_actual = self.automata[3] #el estado actual comienza con el estado inicial

        for simbolo in texto:
            if simbolo not in self.automata[2]: #luego verifica si esta dentro del alfabeto
                print("alfabeto")
                return False
            #crear un variable que sea correcto=False
            #hacer un for que recorra self.automata[5]
            #for transicion_actual in self.automata[5]
            #estado_actual in transicion_actual
            #si cumple hacer simbolo in transicion_actual
            #si cumple hacer estado_actual = transicion_actual[3]
            #hacer correcto=True
            #luego hacer un break
            #if correcto=False retorna False

            if estado_actual in self.automata[5] and simbolo in self.automata[5][estado_actual]: #luego revisa las transiciones
                estado_actual = self.automata[5][estado_actual][simbolo] 
            else:
                print("estado")
                return False

        return estado_actual in self.automata[4] #retorna estado de aceptacion
>>>>>>> 51def8de68bb63400f0fb3c0cd5743c178789658

    def validar(self):
        
        # Realizar las validaciones necesarias
        if self.crear_entry():
<<<<<<< HEAD
            mbox.showinfo("Cadena correcta", "Cadena valida")
=======
            mbox.showerror("Cadena correcta", "Cadena valida")
>>>>>>> 51def8de68bb63400f0fb3c0cd5743c178789658
        else:
            mbox.showerror("Cadena incorrecta", "Cadena invalida")

    def mostrarRuta(self):
<<<<<<< HEAD
        texto = list(self.cadena.get())
        estado_actual = self.automata[3] #el estado actual comienza con el estado inicial
        estado_anterior=[]
        accept=False #acceptar cadena


        for simbolo in texto:
            if estado_actual not in self.automata[1]:
                return False #El estado actual no se encuentra en los estados posibles
            
            if simbolo not in self.automata[2]: #luego verifica si esta dentro del alfabeto
                return False #La cadena se encuentra fuera del alfabeto establecido
                
            end=True #finalizar
            for transicion in self.automata[5]:
                if transicion[0] == estado_actual and transicion[1] == simbolo:
                    if estado_anterior == transicion and transicion [0] != transicion[2]:
                        return False # Repitio la instruccion sin que haya repitencia
                    else:
                        
                        tk.Label(self, text="Me movi de: "+estado_actual+" con: "+simbolo+" hacia : "+transicion[2]).pack(expand=True)
                        estado_anterior=transicion
                        estado_actual = transicion[2]
                        end=False #decimos que aun no ha terminado
                        break;             
            
            if end: #Si no se encontro la transicion finaliza
                return False
            
            if estado_actual in self.automata[4]: #Verificamos si se encuentra en algun estado de aceptacion
                accept = True
            else:
                accept = False


        tk.Label(self, text="Estado final: "+estado_actual).pack(expand=True)
        return accept  # Retorna estado de aceptación si no hay errores

    
    def ruta(self):
        # Realizar las validaciones necesarias
        if self.mostrarRuta():
            tk.Label(self, text="Cadena valida").pack(expand=True)
        else:
            tk.Label(self, text="Cadena invalida").pack(expand=True)
=======
        rutaEstados=[]
        texto = self.cadena.get()
        estado_actual = self.automata[3] #el estado actual comienza con el estado inicial
        rutaEstados.append(estado_actual)

        for simbolo in texto:
            if simbolo not in self.automata[2]: #lluego verifica si esta dentro del alfabeto
                rutaEstados.append("Error, la cadena no es valida")
                return [False, rutaEstados] #retorna si fue existoso o no y la ruta

            if estado_actual in self.automata[5] and simbolo in self.automata[5][estado_actual]: #luego revisa las transiciones
                estado_actual = self.automata[5][estado_actual][simbolo] 
                rutaEstados.append(estado_actual)
            else:
                rutaEstados.append("Error, la cadena no es valida")
                return [False, rutaEstados]

        return [estado_actual in self.automata[4], rutaEstados] #retorna si el estado actua esta o no en los estados de aceptacion
 
    
    def ruta(self):
        variable=self.mostrarRuta() #devuelve un booleano y un array de strings
        print(variable)
        tk.Label(self, text=variable[1]).pack(expand=True) #para mostrar solo el array de strings
>>>>>>> 51def8de68bb63400f0fb3c0cd5743c178789658

