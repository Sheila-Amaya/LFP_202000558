#palabras reservadas son los lexemas
#token | lexema
reservadas = {
    'ROPERACION'        :   'Operacion',
    'RVALOR1'           :   'Valor1',
    'RVALOR2'           :   'Valor2',
    'RSUMA'             :   'Suma',
    'RRESTA'            :   'Resta',
    'RMULTIPLICACION'   :   'Multiplicacion',
    'RDIVISION'         :   'Division',
    'RPOTENCIA'         :   'Potencia',
    'RRAIZ'             :   'Raiz',
    'RINVERSO'          :   'Inverso',
    'RSENO'             :   'Seno',
    'RCOSENO'           :   'Coseno',
    'RTANGENTE'         :   'Tangente',
    'RMOD'              :   'Mod',
    'RTEXTO'            :   'Texto',
    'RCOLORFONDONODO'   :   'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  :   'Color-Fuente-Nodo',
    'RFORMANODO'        :   'Forma-Nodo',
    'COMA'              :   ',',
    'PUNTO'             :   '.',
    'DPUNTO'            :   ':',
    'CORI'              :   '[',
    'CORD'              :   ']',
    'LLAVEI'            :   '}',
    'LLAVED'            :   '{',
}

Lexemas = list(reservadas.values())
global n_linea
global n_columna
global instrucciones
global lista_lexema

n_linea = 1
n_columna = 1

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexema

    lexema = ''
    puntero = 0
    
    while cadena:
        char = cadena[puntero]
        puntero += 1
        

        if char == '\"':
            lexema = armar_Lexema(cadena[puntero:])
            

def armar_Lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexema
    lexema = ''
    puntero = ''
    

    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema
        else:
            lexema += char