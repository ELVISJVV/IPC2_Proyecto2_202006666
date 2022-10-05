from nodo import Nodo
import xml.etree.ElementTree as ET
from clases import *

class ListaDoble:

    def __init__(self):

        self.primero = None
        self.ultimo = None
        self.size = 0

    #insertar en lista
    def insertar(self, dato):

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

    #mostrar datos en consola
    def mostrar(self):

        temp = self.primero

        while temp != None:

            print(temp.getDato().getNombreCliente())
            print(temp.getDato().getTiempo())
            print(temp.getDato().getTiempoTotal())

            temp = temp.siguiente

    def mostrarIngredientes(self):

        temp = self.primero

        while temp != None:

            print('F: {}\nC: {}\n'.format(
                temp.dato.tipoIngrediente, temp.dato.tiempoIngrediente))

            temp = temp.siguiente

    def returnElement(self, posicion):

        actual = self.primero
        i = 1

        while actual != None:

            if posicion == i:

                return actual
                # return actual.dato.nombre

            actual = actual.getSiguiente()
            i += 1

    def borrarNodo(self, dato):
        #creamos un nodo temporal
        # nodoTemporal = Nodo("")

        #el temporal empieza en la cabeza
        nodoTemporal = self.primero

        #Mientras que el temporal no sea nulo
        while nodoTemporal != None:

            #validamos si ese nodo es el que busco
            if nodoTemporal.dato == dato:

                #Si ese nodo es la cabeza
                if nodoTemporal == self.primero:

                    # print("Borrando dato en la cabeza")
                    if self.size == 1:
                        self.primero = None
                        self.ultimo = None

                    else:
                        self.primero = self.primero.siguiente
                        nodoTemporal.siguiente = None
                        self.primero.anterior = None
                #Si ese nodo es la ultimo
                elif nodoTemporal == self.ultimo:
                    # print("Borrando dato en la ultimo")
                    self.ultimo = self.ultimo.anterior
                    nodoTemporal.anterior = None
                    self.ultimo.siguiente = None
                #Si no es ni la ultimo ni la cabeza
                else:
                    # print("Borrando dato del medio")
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None
                self.size -= 1
            nodoTemporal = nodoTemporal.siguiente

    def __setitem__(self, indice, dato):
        if indice >= 0 and indice <= self.size:
            actual = self.primero

            for _ in range(indice - 1):
                actual = actual.siguiente

            actual.dato = dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')

      


    def mostrarEmpresas(self):

        temp = self.primero

        while temp != None:

            print('------------------------------------\nEmpresa \nID: {}\nNombre: {}\nAbreviatura: {}'.format(
                temp.dato.idEmpresa, temp.dato.nombreEmpresa, temp.dato.abreviaturaEmpresa))

            temp.dato.puntosAtencion.mostrarPuntosAtencion()
            temp.dato.transacciones.mostrarTransacciones()
            temp = temp.siguiente

    def mostrarPuntosAtencion(self):

        temp = self.primero

        while temp != None:

            print('\nPuntos Atencion \nidPA: {}\nnombrePA: {}\ndireccionPA: {}'.format(
                temp.dato.idPA, temp.dato.nombrePA, temp.dato.direccionPA))
            
            print("Escritorios Inactivos")
            temp.dato.idlesDesks.mostrarEscritoriosInactivos()
            print("Escritorios Activos")
            temp.dato.activeDesks.mostrarActivosEscritorios()

            temp = temp.siguiente
    
    def mostrarEscritoriosInactivos(self):

        temp = self.primero

        while temp != None:

            print('\nEscritorios Inactivos \nidDesk: {}\nidentificacionDesk: {}\nnombreEncargadoDesk: {}\n'.format(
                temp.dato.idDesk, temp.dato.identificacionDesk, temp.dato.nombreEncargadoDesk))

            temp = temp.siguiente

    def mostrarActivosEscritorios(self):

        temp = self.primero

        while temp != None:

            print('\nEscritorios Activos \nidDesk: {}\nidentificacionDesk: {}\nnombreEncargadoDesk: {}\n'.format(
                temp.dato.idDesk, temp.dato.identificacionDesk, temp.dato.nombreEncargadoDesk))

            temp = temp.siguiente

    def mostrarTransacciones(self):

        temp = self.primero

        while temp != None:

            print('\nTRANSACCIONES \nidTransaccion: {}\nnombreTransaccion: {}\ntiempoAtencion: {}'.format(
                temp.dato.idTransaccion, temp.dato.nombreTransaccion, temp.dato.tiempoAtencion))

            temp = temp.siguiente



    def mostrarConfiguracion(self):

        temp = self.primero

        while temp != None:

            print('------------------------------------\nConfiguracion \nCodigo Configuracion: {}\nCodigo Empresa: {}\nCodigo Punto: {}\n '.format(
                temp.dato.codConfi, temp.dato.codEmpresa, temp.dato.codPunto))

            temp.dato.activeDesks.mostrarEscritoriosActivos()
            temp.dato.clientes.mostrarConfiClientes()
            temp = temp.siguiente


    def mostrarEscritoriosActivos(self):

        temp = self.primero

        while temp != None:

            print('\nEscritorios Activos \nidActiveDesk {}\n'.format(
                temp.dato.idActiveDesk))

            temp = temp.siguiente


    def mostrarConfiClientes(self):

        temp = self.primero

        while temp != None:

            print('\nClientes \nDPI: {}\nnombre Cliente: {}\n'.format(
                temp.dato.dpi, temp.dato.nombreCliente))

            temp.dato.listadoTrans.mostrarTransClientes()
            temp = temp.siguiente

    def mostrarTransClientes(self):

        temp = self.primero

        while temp != None:

            print('\nTransacciones Clientes \nID Transaccion: {}\nCantidad Transaccion: {}\n'.format(
                temp.dato.idTrans, temp.dato.cantTrans))

            temp = temp.siguiente



    
def cargarEmpresas(ruta, listaEmpresas):
    # temp = self.primero
    # Lista para las empresas
    # listaEmpresas = ListaDoble()
    # Atributos de la empresa
    idEmpresa = ''
    nameEmpresa = ''
    abreviatura = ''
    # Lista Puntos Atencion
    listaPA = ListaDoble()
    # Atributos Punto de Atencion
    idPA = ''
    nombrePA = ''
    direccionPA = ''
    # Lista Escritorios
    listaIdleDesks = ListaDoble()
    # Atributos Escritorio
    idDesk = ''
    identificacionDesk = ''
    nombreEncargadoDesk = ''
    activeDesk = ''
    #lista Escritorios Activos
    listaActiveDesk = ListaDoble()
    # Lista Transacciones
    listaTrans = ListaDoble()
    # Atributos Transaccion
    idTrans = ''
    nombreTrans = ''
    tiempoTrans = ''
    # Lista Clientes
    listaClientes = ListaDoble()  # Se mantendra vacia
    # Inicio Lectura XML
    # while temp != None:
    # while ruta != None:
        # tree = ET.parse(temp.dato)
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        if elemento.tag == 'empresa':
            idEmpresa = elemento.get('id')
            for subelemeto in elemento:
                if subelemeto.tag == 'nombre':
                    nameEmpresa = subelemeto.text
                elif subelemeto.tag == 'abreviatura':
                    abreviatura = subelemeto.text
                elif subelemeto.tag == 'listaPuntosAtencion':
                    for sub in subelemeto:
                        if sub.tag == 'puntoAtencion':
                            idPA = sub.get('id')
                            for a in sub:
                                if a.tag == 'nombre':
                                    nombrePA = a.text
                                elif a.tag == 'direccion':
                                    direccionPA = a.text
                                elif a.tag == 'listaEscritorios':
                                    for sub2 in a:
                                        if sub2.tag == 'escritorio':
                                            idDesk = sub2.get('id')
                                            for b in sub2:
                                                if b.tag == 'identificacion':
                                                    identificacionDesk = b.text
                                                elif b.tag == 'encargado':
                                                    nombreEncargadoDesk = b.text
                                        escritorio = Escritorio(
                                            idDesk, identificacionDesk, nombreEncargadoDesk)
                                        listaIdleDesks.insertar(escritorio)
                                        idDesk = ''
                                        identificacionDesk = ''
                                        nombreEncargadoDesk = ''
                        puntoAtencion = PuntoAtencion(
                            idPA, nombrePA, direccionPA, listaActiveDesk, listaIdleDesks, listaClientes)
                        listaPA.insertar(puntoAtencion)
                        idPA = ''
                        nombrePA = ''
                        direccionPA = ''
                        listaIdleDesks = ListaDoble()
                        listaClientes = ListaDoble()
                elif subelemeto.tag == 'listaTransacciones':
                    for sub3 in subelemeto:
                        if sub3.tag == 'transaccion':
                            idTrans = sub3.get('id')
                            for c in sub3:
                                if c.tag == 'nombre':
                                    nombreTrans = c.text
                                elif c.tag == 'tiempoAtencion':
                                    tiempoTrans = c.text
                        transaccion = Transaccion(
                            idTrans, nombreTrans, tiempoTrans)
                        listaTrans.insertar(transaccion)
                        idTrans = ''
                        nombreTrans = ''
                        tiempoTrans = ''
            print("####################")
            empresa = Empresa(idEmpresa, nameEmpresa,
                              abreviatura, listaPA, listaTrans)
            listaEmpresas.insertar(empresa)
            idEmpresa = ''
            nameEmpresa = ''
            abreviatura = ''
            listaPA = ListaDoble()
            listaTrans = ListaDoble()
            # temp = temp.siguiente

    return listaEmpresas


# Cargar Segundo archivo XML


def cargarConfiguracion(listaConfi, ruta):

    # temp = self.primero
    # Lista para la configuracion
    # listaConfi = ListaDoble()
    # Atributos de la configuracion
    idConfi = ''
    idEmpresa = ''
    idPunto = ''
    # Lista escritorios Activos
    listaActiveDesks = ListaDoble()
    # Atributos escritorios activos
    idDesk = ''
    # Lista Clientes
    listaClientes = ListaDoble()
    # Atributos Clientes
    dpi = ''
    nombreCliente = ''
    # Lista Transacciones
    listaTransClientes = ListaDoble()
    # Atributos Transaccion
    idTrans = ''
    cantidadTrans = ''
    # Inicio Lectura XML
    # while temp != None:
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        if elemento.tag == 'configInicial':
            idConfi = elemento.get('id')
            idEmpresa = elemento.get('idEmpresa')
            idPunto = elemento.get('idPunto')
            for subelemeto in elemento:
                if subelemeto.tag == 'escritoriosActivos':
                    for sub in subelemeto:
                        if sub.tag == 'escritorio':
                            idDesk = sub.get('idEscritorio')
                        escritoriosActivos = ConfiEscritorio(idDesk)
                        listaActiveDesks.insertar(escritoriosActivos)
                        idDesk = ''
                elif subelemeto.tag == 'listadoClientes':
                    for sub3 in subelemeto:
                        if sub3.tag == 'cliente':
                            dpi = sub3.get('dpi')
                            for c in sub3:
                                if c.tag == 'nombre':
                                    nombreCliente = c.text
                                elif c.tag == 'listadoTransacciones':
                                    for a in c:
                                        if a.tag == 'transaccion':
                                            idTrans = a.get(
                                                'idTransaccion')
                                            cantidadTrans = a.get(
                                                'cantidad')
                                        transaccion = ClienteTrans(
                                            idTrans, cantidadTrans)
                                        listaTransClientes.insertar(
                                            transaccion)
                        cliente = Cliente(
                            dpi, nombreCliente, listaTransClientes)
                        listaClientes.insertar(cliente)
                        listaTransClientes = ListaDoble()
        print("####################")
        confiInicial = ConfiguracionInical(idConfi, idEmpresa, idPunto, listaActiveDesks, listaClientes)
        listaConfi.insertar(confiInicial)
        listaActiveDesks = ListaDoble()
        listaClientes = ListaDoble()
        # temp = temp.siguiente
    return listaConfi
