from abc import ABC, abstractmethod #decorador se utiliza para indicar que un método es abstracto

class Expresion(ABC): #al hererdar ABC se convierte en una clase abstracta
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        
    @abstractmethod #ind. que este método es abstracto y debe ser implementado por las subclases
    def operar(self, arbol):
        pass
    
    @abstractmethod
    def getFila(self):
        return self.fila
    
    @abstractmethod
    def getColumna(self):
        return self.columna # devuelve el valor de la variable
    