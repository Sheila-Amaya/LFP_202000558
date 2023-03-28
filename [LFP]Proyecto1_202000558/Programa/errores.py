class Error:
    def __init__(self, lexema, linea, columna, tipo='ERROR'):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
