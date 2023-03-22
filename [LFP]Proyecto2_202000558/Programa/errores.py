class Error:
    def __init__(self, mensaje, linea, columna):
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna