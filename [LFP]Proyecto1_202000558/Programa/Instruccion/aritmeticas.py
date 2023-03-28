from abst.abstract import Expresion 

class Aritmetica(Expresion): #hereda de la clase
    
    def __init__(self,L ,R , tipo, fila, columna):
        self.L = L
        self.R = R
        self.tipo = tipo
        self.valor = None
        super().__init__(fila, columna) #inicializa los atributos f y c en base al constructor expresion
        
        
    def operar(self, arbol):
        Lvalue = ''
        Rvalue = ''

        if self.L != None: #verifica si el operando izquierdo es diferente de nada
            Lvalue = self.L.operar(arbol) # si L no es none llama al metodo 
        if self.R != None:
            Rvalue = self.R.operar(arbol)

        if self.tipo.operar(arbol) == 'Suma': #verifica el tipo de operacion
            resultado = Lvalue + Rvalue # si es una + calcula el resultado
            self.valor = resultado #asignando el resultado a valor
            return resultado
        elif self.tipo.operar(arbol) == 'Resta':
            resultado = Lvalue - Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Multiplicacion':
            resultado = Lvalue * Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Division':
            resultado =  Lvalue / Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Modulo':
            resultado =  Lvalue % Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Potencia':
            resultado =  Lvalue ** Rvalue
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Raiz':
            resultado =  Lvalue ** (1/Rvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Inverso':
            resultado =  1/Lvalue
            self.valor = resultado
            return resultado
        else:
            return 0
        
    def getFila(self):
        return super().getFila() #devuelve la f de la expresion
    
    def getColumna(self):
        return super().getColumna() #devuelve la c de la expresion
    
    def __str__(self):
        return f"{self.tipo.operar(None)}\n {self.valor}" #devuelve una cadena que repre. la operacion con el resultado valor
    
    def graphviz(self, node_id=0, label="", direction=""):
        if self.L is None and self.R is None: #si l y r no son nulos, si lo son entonces es un nodo hoja
            graphviz_code = f"node_{node_id} [label=\"{self.tipo.operar(None)}\\n{self.valor}\"];\n" #se crea un nodo con el resultado valor
        else: # si no son nulos r y l crea dos nodos uno para cada subexpresion y un nodo adicional para la operacion aritmetica 
            graphviz_code = f"node_{node_id} [label=\"{self.tipo.operar(None)}\\n{self.valor}\"];\n" #nodo actual
            if self.L: #si la rama L no es ninguno entonces hay un nodo secundario L para recorrer
                left_label = str(self.L) #convierte el nodo secundario en una cadena
                left_node_id = f"{node_id}_izq" #crea un id para el nodo L
                if direction: #si no es ninguno se esta recorriendo desde una deter. direccion
                    left_label += f" ({direction})" #agrega la direccion a la etiqueta
                graphviz_code += self.L.graphviz(left_node_id, left_label) #Rec. 
                graphviz_code += f"node_{node_id} -> node_{left_node_id};\n"
            if self.R: #si la rama no es niguno enonces hay un nodo secundario 
                right_label = str(self.R) 
                right_node_id = f"{node_id}_der"
                if direction: #si no ninguno el nodo sec. se esta recorriendo desde una detrm. direc.
                    right_label += f" ({direction})" #agrega la direccion al nodo
                graphviz_code += self.R.graphviz(right_node_id, right_label)
                graphviz_code += f"node_{node_id} -> node_{right_node_id};\n"
        return graphviz_code