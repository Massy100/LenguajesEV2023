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

    def validar(self):
        
        # Realizar las validaciones necesarias
        if self.crear_entry():
            mbox.showinfo("Cadena correcta", "Cadena valida")
        else:
            mbox.showerror("Cadena incorrecta", "Cadena invalida")

    def mostrarRuta(self):
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

