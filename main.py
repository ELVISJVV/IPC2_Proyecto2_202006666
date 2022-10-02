
from listaDoble import *
from clases import *

if __name__ == '__main__':

    salir = False
    rutas = ListaDoble()
    empresas = ListaDoble()
    listaEmpresas = ListaDoble()
    listaConfi = ListaDoble()
    rutas2 = ListaDoble()
    listaDesks = ListaDoble()
    listaPA = ListaDoble()
    listaClientes = ListaDoble()
    listaTrans = ListaDoble()
    while not salir:

        print("\n======= MENU PRINCIPAL ========")
        print("1. Configuración de empresas")
        print("2. Selección de empresa y punto de atención")
        print("3. Seleccionar  Paciente")
        print("4. Generar Reporte")
        print("5. Salir")
        print("================================")
        opcion = input()
        if opcion == '1':
            salir1 =False
            while not salir1:
                print("\n======= Configuración de empresas ========")
                print("1. Limpiar sistema")
                print("2. Cargar archivo de configuración del sistema")
                print("3. Crear nueva empresa")
                print("4. Cargar archivo con configuración inicial")
                print("5. Regresar")
                print("===========================================")
                opcion1 = input()
                if opcion1 == '1':
                    # rutas = ListaDoble()
                    listaEmpresas = ListaDoble()
                    listaConfi = ListaDoble()
                    # print(listaEmpresas.size)
                    # rutas2 = ListaDoble()
                    print("Se han borrado todos los datos \n")
                elif opcion1 == '2':
                    try:
                        print('Ingrese la ruta de su archivo: \n')
                        ruta = input('\t -> ')
                        # cargarEmpresas
                        # rutas.insertar(ruta)
                        cargarEmpresas(ruta,listaEmpresas)
                        print("Se han agregado las empresas")
                        print("\n")
                    except:
                        print("NO se pudo cargar el archivo")
                        print("Intentalo Nuevamente")
                        print("\n")
                elif opcion1 == '3':

                    salir13 = False
                    print('\nCrear Nueva Empresa')
                    print('Ingrese el ID de la nueva empresa')
                    idEmpresa = input()
                    print('Ingrese nombre de la nueva empresa')
                    nombreEmpresa = input()
                    print('Ingrese abreviatura de la empresa')
                    abrevEmpresa = input()
                    while True:
                        print('\nPuntos de Atención')
                        print('Ingrese ID del punto de Atención')
                        id_punto_atencion = input()
                        print('Nombre Punto Atención')
                        nombre_punto_atencion = input()
                        print('Direccion Punto Atención')
                        direccion_punto_atencion = input()

                        print('\nAgregar Escritorios')
                        while True:
                            print('Ingrese ID del Escritorio')
                            id_escritorio = input ()
                            print('Ingrese Identificacion del Escritorio')
                            identificacion_escritorio = input()
                            print('Ingrese Encargado del escritorio')
                            encargado_escritorio = input()

                            escritorio = Escritorio(id_escritorio, identificacion_escritorio, encargado_escritorio, True)
                            listaDesks.insertar(escritorio)

                            print('\nDesea agreagar otro escritorio')
                            print('1. Si')
                            print('2. No')
                            otro_escritorio = input()
                            if otro_escritorio == '1':
                                pass
                            elif otro_escritorio == '2':
                                break
                            else:
                                break
                        
                        punto_Atencion = PuntoAtencion(id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion,listaDesks, listaClientes)
                        listaPA.insertar(punto_Atencion)
                        listaDesks = ListaDoble()

                        print('\nDesea Agregar otro punto de Atencion')
                        print('1. Si')
                        print('2. No')
                        otro_punto = input()
                        if otro_punto == '1':
                            pass
                        elif otro_punto == '2':
                            break
                        else:
                            break

                    while True:
                        print('\nAgregar Transacciones')
                        print('Ingrese ID de la Transaccion')
                        id_transaccion = input()
                        print('Ingrese nombre de la transaccion')
                        nombre_transaccion = input()
                        print('Ingrese el tiempo de atencion')
                        tiempo_atencion_transaccion = input()

                        trans = Transaccion(id_transaccion,nombre_transaccion,tiempo_atencion_transaccion)
                        listaTrans.insertar(trans)


                        print('\nDesea Agregar otra Transaccion')
                        print('1. Si')
                        print('2. No')
                        otra_transaccion = input()
                        if otra_transaccion == '1':
                            pass
                        elif otra_transaccion == '2':
                            break
                        else:
                            break

                    empresa = Empresa(idEmpresa,nombreEmpresa,abrevEmpresa,listaPA,listaTrans)
                    listaEmpresas.insertar(empresa)
                    listaTrans = ListaDoble()
                    listaPA = ListaDoble()


                    print('\nSe ha creado la nueva empresa\n')
                elif opcion1 == '4':
                    try:
                        print('Ingrese la ruta de su archivo: \n')
                        ruta2 = input('\t -> ')
                        rutas2.insertar(ruta2)
                        cargarConfiguracion(listaConfi,ruta2)

                        listaConfi.returnElement(1)
                        listaEmpresas.returnElement(1)
                        
                        for i in  range(1, int(listaEmpresas.size)+1, 1):
                            for j in range(1, listaConfi.size +1 , 1):
                                listaEmpresas.returnElement(i).getiIDEmpresa()


                        print("Se han agregado las configuraciones")
                        print("\n")

                    except:
                        print("NO se pudo cargar el archivo")
                        print("Intentalo Nuevamente")
                        print("\n")
                elif opcion1 == '5':
                    salir1 = True

        elif opcion == '5':
            salir = True
        elif opcion == '3':
            listaEmpresas.mostrarEmpresas()
        elif opcion == '2':
           pass
        elif opcion == '4':
            listaConfi.mostrarConfiguracion()
