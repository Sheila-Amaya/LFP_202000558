from Nodo import Nodo



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
                print("La pelicula ",pelicula.nombre, "ya se encuentra en la lista.")
                actual.dato = pelicula # actualiza la información de la película
                return
            actual = actual.siguiente
    
        # Compara el nombre de la nueva película con el nombre de la última película en la lista
        if actual.dato.nombre == pelicula.nombre: #Si la película ya está en la última posición de la lista
            print("La película", pelicula.nombre, "ya está en la lista.")
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
        
        while actual:
            print("\n",str(i)+ '. : ',actual.dato.nombre)
            i+=1
            actual = actual.siguiente
            
    def mostrarActores(self):
        actual = self.primero
        i=1
        while actual:
            print("\n",str(i)+". ",actual.dato.nombre,)
            i +=1
            for actor in actual.dato.actores: #recorre la lista de actores
                print("-",actor)
            actual = actual.siguiente


