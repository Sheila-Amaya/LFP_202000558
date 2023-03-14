from Nodo import Nodo
from Pelicula import Pelicula
from graphviz import Digraph

class Lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self,pelicula):
        nuevo_nodo = Nodo(pelicula) #crea un nodo y le asigna una pelicula
        if self.primero is None: #si la lista esta vacia
            self.primero = nuevo_nodo #asigna el nuevo nodo como el primer nodo de la lista
            return
        #si la lista no esta vacia
        actual = self.primero
        while actual.siguiente: 
            if actual.dato.nombre == pelicula.nombre:
                print("\nLa pelicula ",pelicula.nombre, "ya se encuentra en la lista.")
                actual.dato = pelicula # actualiza la información de la película
                return
            actual = actual.siguiente
    
        # Compara el nombre de la nueva película con el nombre de la última película en la lista
        if actual.dato.nombre == pelicula.nombre: #Si la película ya está en la última posición de la lista
            print("\nLa película", pelicula.nombre, "ya está en la lista.")
            actual.dato = pelicula # actualiza la información de la película
            return
        
        actual.siguiente = nuevo_nodo #si no esta agrega el nuevo nodo
        nuevo_nodo.siguiente = None

    def mostrar(self):
        actual = self.primero

        while actual:
            print("Nombre de la pelicula: ",actual.dato.nombre)
            print("Actores :",actual.dato.actores)
            print("Año:",actual.dato.anio)
            print("Genero",actual.dato.genero)
            actual = actual.siguiente

    def mostrarPelicula(self):
        actual = self.primero
        i=1
        print()
        while actual:
            print(str(i)+ '. ',actual.dato.nombre)
            i+=1
            actual = actual.siguiente
        print()

    def mostrarP_A(self):#no se usa
        actual = self.primero #muestra la lita de peliculas
        i=1
        while actual:
                print(str(i)+". ",actual.dato.nombre,)
                actual = actual.siguiente
                i +=1
        num_peli = input("\n\tIngrese el número de la pelicula seleccionanda para ver sus actores: ")
        actual = self.primero
        
        i=1
        #busca la pelicula en la lista
        while actual and i<int(num_peli):
            actual = actual.siguiente
            i += 1
            # muestra la lista de actores sefun la pelicula seleccionada
        if actual:
            for actor in actual.dato.actores: #recorre la lista  de actores
                print("\t-",actor)
            return #termina la funcion luego de encontrar la pelicula
        else:
            print("\nNo se encontro la pelicula \n")

    def mostrarActores(self):#mostrar actores sin repetir
        actual = self.primero
        i = 1
        actores_ = [] #lista aux para almacenar los actores
        while actual: #mientras hay nodos en la lista
            #print(str(i)+".", actual.dato.actores)
            for actor in actual.dato.actores:
                if actor not in actores_: #si el actor no a sido agregado a []
                    actores_.append(actor)
            actual = actual.siguiente
            i += 1
            
        #print("\nLista de actores:")
        for actor in actores_: #recorre la lista []
            print("\t-"+actor)
    

    def buscar_actor(self, nombre_actor):
        actual = self.primero
        peliculas_encontradas = [] #lista auxiliar que almacena el nombre de cada pelicula
        
        while actual: #recorre la lista enlazada
            if nombre_actor in actual.dato.actores: #verifica si el nombre del actor esta en la lista
                peliculas_encontradas.append(actual.dato.nombre) #se agrega a la lista peliculas_encontradas
            actual = actual.siguiente
        
        if len(peliculas_encontradas)>0: #si tiene almenos un elemento
                print("\nPeliculas en las que participe el actor ",nombre_actor)
                for pelicula in peliculas_encontradas: #muestra la lista de peliculas encontradas
                    print("- ", pelicula)
        else:
            print("\tNo se encontraron peliculas en las que participo el actor, ",nombre_actor)

    def buscar_anio(self, entrada):
        actual = self.primero
        anio_peli = []
        
        while actual:
            if entrada == actual.dato.anio:
                anio_peli.append((actual.dato.nombre,actual.dato.genero))
            actual = actual.siguiente
            
        if anio_peli:
            #print("Peliculas del año: ", entrada)
            for anio in anio_peli:
                #print(anio)
                a = anio[0]
                genero = anio[1]
                print("\tPelicula: ",a, ", genero: ",genero)
        else:
            print("El año,",entrada," no se encuentra en el sistema.")
                

    def buscar_genero(self,entrada):
        actual = self.primero
        genero_peli = []
        
        while actual:
            if entrada == actual.dato.genero:
                genero_peli.append(actual.dato.nombre)
            actual = actual.siguiente
            
        if genero_peli:
            for genero in genero_peli:
                print("\t-",genero)
        else:
            print("No se encontro el genero",entrada)

    def graph(self):
        dot = Digraph(filename='peliculas.gv', node_attr={'shape': 'rectangle'}) # Crear una instancia de Digraph
        # recorremos la lista y creamos los nodos
        actual = self.primero
        while actual:
            etiqueta_nodo = "{}\n[{},{}]".format(actual.dato.nombre, actual.dato.genero, actual.dato.anio)
            dot.node(actual.dato.nombre, label=etiqueta_nodo)
            actual = actual.siguiente
        # recorremos la lista de nuevo y creamos las conexiones
        actual = self.primero
        while actual:
            for actor in actual.dato.actores:
                dot.edge(actual.dato.nombre,actor)
            actual = actual.siguiente
        # mostramos el grafo
        print("Grafico generado con exito..")
        dot.render("../Grafico/peliculas",format="pdf")
        