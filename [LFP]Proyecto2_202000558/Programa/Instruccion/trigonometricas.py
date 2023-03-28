from abst.abstract import Expresion
from math import *

class Trigonometrica(Expresion):
    
    def __init__(self, L, tipo, fila, columna):
        self.L = L
        self.tipo = tipo
        self.valor = ""
        super().__init__(fila, columna)
        
        
    def operar(self, arbol): #devuelve un resultado al aplicar una func. trig.
        Lvalue = ''

        if self.L != None:
            Lvalue = self.L.operar(arbol)
            
        if self.tipo.operar(arbol) == 'Seno': #comprueba el tipo de ope
            resultado = sin(Lvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Coseno':
            resultado = cos(Lvalue)
            self.valor = resultado
            return resultado
        elif self.tipo.operar(arbol) == 'Tangente':
            resultado = tan(Lvalue)
            self.valor = resultado
            return resultado
        else:
            return 0
        
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    def __str__(self):
        return f"{self.tipo.operar(None)}\n {self.valor}" #devuelve una cadena que contiene el tipo y valor de la ope
    
    def graphviz(self, node_id=0, label="", direction=""):
        graphviz_code = f"node_{node_id} [label=\"{label}\"];\n"
        if self.L: #si la expre. tiene un hijo izquierdo
            left_label = str(self.L)
            left_node_id = f"{node_id}_izq"
            if direction:
                left_label += f" ({direction})"
            graphviz_code += self.L.graphviz(left_node_id, left_label)
            graphviz_code += f"node_{node_id} -> node_{left_node_id};\n"
        return graphviz_code #devuelve la cadena que contiene la representacion 