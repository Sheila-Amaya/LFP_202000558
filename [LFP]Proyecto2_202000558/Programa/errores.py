class ErrorLexico:
    def __init__(self, caracter, linea, columna):
        self.caracter = caracter
        self.tipo = "Error léxico"
        self.linea = linea
        self.columna = columna
        
class ErrorSintactico:
    def __init__(self, caracter, linea, columna):
        self.caracter = caracter
        self.tipo = "Error Sináctico"
        self.linea = linea
        self.columna = columna