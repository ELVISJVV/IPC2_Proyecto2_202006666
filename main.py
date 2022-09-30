
from listaDoble import *
from clases import *

if __name__ == '__main__':

    salir = False
    rutas = ListaDoble()
    empresas = ListaDoble()
    rutas2 = ListaDoble()
    while not salir:

        print("======= MENU PRINCIPAL ========")
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
                print("======= Configuración de empresas ========")
                print("1. Limpiar sistema")
                print("2. Cargar archivo de configuración del sistema")
                print("3. Crear nueva empresa")
                print("4. Cargar archivo con configuración inicial")
                print("5. Regresar")
                print("===========================================")
                opcion1 = input()
                if opcion1 == '1':
                    rutas = ListaDoble()
                    empresas = ListaDoble()
                    rutas2 = ListaDoble()
                    print("Se han borrado todos los datos \n")
                elif opcion1 == '2':
                    try:
                        print('Ingrese la ruta de su archivo: \n')
                        ruta = input('\t -> ')
                        rutas.insertar(ruta)
                        print("Se han agregado las empresas")
                        print("\n")
                    except:
                        print("NO se pudo cargar el archivo")
                        print("Intentalo Nuevamente")
                        print("\n")
                elif opcion1 == '3':
                    pass
                elif opcion1 == '4':
                    try:
                        print('Ingrese la ruta de su archivo: \n')
                        ruta2 = input('\t -> ')
                        rutas2.insertar(ruta2)
                        print("Se han agregado las empresas")
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
            listaEmpresas = rutas.cargarEmpresas()
            print("======")
            listaEmpresas.mostrarEmpresas()
        elif opcion == '2':
           pass
        elif opcion == '4':
            listaConfi = rutas2.cargarConfiguracion()
            listaConfi.mostrarConfiguracion()
