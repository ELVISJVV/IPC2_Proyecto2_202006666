class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None
        self.anterior = None


class ListaDoble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insertar en lista
    def insertar(self, dato):

        nuevo = Nodo(dato)
        self.size += 1

        if self.primero == None:

            self.primero = nuevo
            self.ultimo = nuevo
        else:

            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero

        while temp != None:

            print(temp.dato)

            temp = temp.siguiente

    def inserta2(self, dato):

        nuevo = Nodo(dato)

        if self.primero is None:

            self.primero = nuevo
            self.ultimo = self.primero
        else:
            # insertar ultimo
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

            # insertar al principio
            # nuevo.siguiente = self.primero
            # self.primero.anterior = nuevo
            # self.primero = nuevo
        self.size += 1


list = ListaDoble ()
list.inserta2(1)
list.inserta2(13)
list.inserta2(2)
list.mostrar()