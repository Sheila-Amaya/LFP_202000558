class Estilo:
        def __init__(self, texto, color_nodo, color_fuente, forma_nodo):
            self.texto = texto
            self.color_nodo = color_nodo
            self.color_fuente = color_fuente
            self.forma_nodo = forma_nodo
            
        def get_texto(self):
            return self.texto
    
        def get_color_nodo(self):
            return self.color_nodo
    
        def get_color_fuente(self):
            return self.color_fuente
    
        def get_forma_nodo(self):
            return self.forma_nodo