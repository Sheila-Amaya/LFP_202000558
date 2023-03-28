from abst.abstract import Expresion

class Num(Expresion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)
        
    def operar(self, arbol):
        return self.valor
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    def get_valor(self):
        return self.valor
    
    def __str__(self):
        return str(self.valor)

    def graphviz(self, node_id=0, label="", direction=""): #se utilizan para personalizar la apariencia del nodo en el gráfico.
        graphviz_code = f"node_{node_id} [label=\"{label}\"];\n" #contiene una cadena de texto 
        return graphviz_code