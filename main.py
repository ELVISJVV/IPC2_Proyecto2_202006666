
from listaDoble import *
from clases import *
from os import startfile, system

if __name__ == '__main__':

    salir = False
    rutas = ListaDoble()
    empresas = ListaDoble()
    listaEmpresas = ListaDoble()
    listaConfi = ListaDoble()
    rutas2 = ListaDoble()
    listaIdleDesks = ListaDoble()
    listaActiveDesk = ListaDoble()
    listaPA = ListaDoble()
    listaClientes = ListaDoble()
    listaTrans = ListaDoble()
    seleccion_empresa = ''
    seleccion_punto_atencion = ''

    def generarGraphvizDesk(lista):
        graphviz = '''
        digraph L{
        node [shape=box fillcolor="#FFEDBB" style = filled]

        subgraph cluster_p{
            label="Escritorios"
            bgcolor = "#398D9C"
        '''

        size = int(lista.size)

        for i in range(1, size+1, 1):
            # print("numero de rango")
            # print(i)
            # print("numero de size")
            # print(size)
            
            # print(cliente)
            
            # print(nombreCliente)
            graphviz += 'Columna' + str(i) + '''[label=<<TABLE  BORDER="0" CELLBORDER="1" CELLSPACING="0"> 
            <TR>
            <TD  > Encargado </TD> <TD>''' + str(lista.returnElement(int(i)).getDato().getEncargado()) + '''</TD>

            </TR>

            <TR>
            

            <TD>ID Escritorio</TD>
            <TD>''' + str(lista.returnElement(int(i)).getDato().getIdDesk()) + '''</TD>
            </TR>
            
            

            </TABLE>>,group=1, fillcolor=yellow]; '''

        

        for i in range(size, 0, -1):
            if i-1 == 0:
                break
            graphviz += 'Columna' + str(i) + '-> Columna' + str(i-1) + ';'

        graphviz += ''' 
        }
        }
        '''

        miArchivo = open("graphviz.dot", 'w')
        miArchivo.write(graphviz)
        miArchivo.close()

        system('dot -Tpng graphviz.dot -o graphviz.png')
        # system('cd ./graphviz.png')
        startfile('graphviz.png')

    def generarGraphviz(lista):
        graphviz = '''
        digraph L{
        node [shape=box fillcolor="#FFEDBB" style = filled]

        subgraph cluster_p{
            label="Orden de Clientes"
            bgcolor = "#398D9C"
        '''

        size = int(lista.size)

        for i in range(1, size+1, 1):
           
            graphviz += 'Columna' + str(i) + '''[label = " ''' + str(lista.returnElement(i).getDato().getNombre()) + '''", fillcolor=yellow]; '''

       
        graphviz += '''{rank = same;'''

        for a in range(1, size+1, 1):
            if a == size:
                graphviz += 'Columna' + str(a) + '}'
            else:
                graphviz += 'Columna' + str(a) + ';'

        for i in range(size, 0, -1):
            if i-1 == 0:
                break
            graphviz += 'Columna' + str(i) + '-> Columna' + str(i-1) + ';'

        graphviz += ''' 
        }
        }
        '''

        miArchivo = open("graphviz1.dot", 'w')
        miArchivo.write(graphviz)
        miArchivo.close()

        system('dot -Tpng graphviz1.dot -o graphviz1.png')
        # system('cd ./graphviz.png')
        startfile('graphviz1.png')

    while not salir:

        print("\n======= MENU PRINCIPAL ========")
        print("1. Configuración de empresas")
        print("2. Selección de empresa y punto de atención")
        print('3. Manejo de Puntos de Atencion')
        print("4. Listado de Empresas")
        print("5. Listado de Configuracion ")
        print("6. Salir")
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

                            escritorio = Escritorio(id_escritorio, identificacion_escritorio, encargado_escritorio)
                            listaIdleDesks.insertar(escritorio)

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
                        
                        punto_Atencion = PuntoAtencion(id_punto_atencion, nombre_punto_atencion, direccion_punto_atencion, listaActiveDesk,listaIdleDesks, listaClientes)
                        listaPA.insertar(punto_Atencion)
                        listaIdleDesks = ListaDoble()

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

                        # listaConfi.returnElement(1)
                        # listaEmpresas.returnElement(1)
                        # print(listaEmpresas.returnElement(1).getDato().getiIDEmpresa())
                        # print(listaConfi.returnElement(1).getDato().getCodEmpresa())
                        # print(listaConfi.returnElement(1).dato.codEmpresa)
                        
                        for i in  range(1, int(listaEmpresas.size)+1, 1):
                            # listanuevosdesks = ListaDoble()
                            # print("=============")

                            for j in range(1, int(listaConfi.size) +1 , 1):

                                get_id_empresa = listaEmpresas.returnElement(i).getDato().getIDEmpresa()
                                get_id_empresa_confi = listaConfi.returnElement(j).getDato().getCodEmpresa()
                                
                                
                                # si el id de la lista empresa coincide con el id de la empresa confi
                                if get_id_empresa == get_id_empresa_confi:
                                    
                                    # print('+++++++++++++')
                                    # print("coincidencia  id empresa")
                                    # print(get_id_empresa)
                                    # print('Coincidencia id empresa confi')
                                    # print(get_id_empresa_confi)

                                    # for para verificar cual punto de atencion tiene coincidencia
                                    for a in range(1, int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().size)+1, 1):
                                        
                                        get_idpa_empresa = listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIDPA()

                                        get_idpa_confi = listaConfi.returnElement(j).getDato().getCodPunto()
                                        if get_idpa_empresa == get_idpa_confi:


                                            # print('Coincidencia empresa Puntos')
                                            # print(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIDPA())
                                            # print('Coincidencia  puntos confi')
                                            # print(listaConfi.returnElement(j).getDato().getCodPunto())        
                                            contador = 1
                                            # for b in range(1, int(listaConfi.returnElement(j).getDato().getActiveDesk().size) + 1, 1):
                                            #     print(contador)
                                            #     contador +=1
                                            for b in range(1, int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().size) + 1, 1):
                                                
                                                for c in range(1, int(listaConfi.returnElement(j).getDato().getActiveDesk().size) + 1, 1):
                                                    
                                                #     print(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().size)

                                                    get_id_desk_empresa = listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().returnElement(b).getDato().getIdDesk()
                                                    get_id__desk_confi = listaConfi.returnElement(j).getDato().getActiveDesk().returnElement(c).getDato().getIdActiveDesk()

                                                    if get_id_desk_empresa == get_id__desk_confi:

                                                        # print('revison')
                                                        # print(get_id_desk_empresa)
                                                        # print(get_id__desk_confi)

                                                        # print('fin revison')
                                                        # listanuevosdesks.insertar(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().returnElement(b).getDato())
                                                        listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getActiveDesk().insertar(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().returnElement(b).getDato())
                                                        # print(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().returnElement(b).getDato())
                                                        # listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().borrarNodo(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIdlesDesk().returnElement(b).getDato())
                                                        # print('se pudo 2.0')
                                                            # else:
                                                            #     print('no se pudo 2.0')

                                            for clientes in range(1, int(listaConfi.returnElement(j).getDato().getClientes().size) + 1, 1):
                                                listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getClientesPA().insertar(listaConfi.returnElement(j).getDato().getClientes().returnElement(clientes).getDato())
                                                
                                                

                                        else:
                                            # print('C no hay oincidencia empresa Puntos')
                                            # print(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(a).getDato().getIDPA())
                                            # print(' no hay Coincidencia  puntos confi')
                                            # print(listaConfi.returnElement(j).getDato().getCodPunto())
                                            pass

                                else:
                                    # print('+++++++++++++')
                                    # print("no hay coincidencia  id empresa")
                                    # print(get_id_empresa)
                                    # print(' no hay Coincidencia id empresa confi')
                                    # print(get_id_empresa_confi)
                                    pass

                        # for para cada empresa
                        for a in range(1, int(listaEmpresas.size)+1, 1):
                            # for para cada punto de atencion
                            for b in range(1, int(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().size)+1, 1):
                                # for para cada escritorio activo
                                for c in range(1, int(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getActiveDesk().size)+1, 1):
                                    # for para escritorio inactivo
                                    for d in range(1, int(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getIdlesDesk().size)+1, 1):
                                        
                                        if listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getActiveDesk().returnElement(c).getDato().getIdDesk() == listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getIdlesDesk().returnElement(d).getDato().getIdDesk():

                                            # print("son iguales")
                                            # print(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getIdlesDesk().returnElement(d).getDato().getIdDesk())
                                            # print(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getActiveDesk().returnElement(c).getDato().getIdDesk())

                                            listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getIdlesDesk().borrarNodo(listaEmpresas.returnElement(a).getDato().getPuntosAtencion().returnElement(b).getDato().getActiveDesk().returnElement(c).getDato())
                                            break
                        
                        # contador = 1
                        # # colocar los tiempos
                        # for i in range(1, int(listaEmpresas.size)+1, 1):
                           
                        #     for j in range(1, int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().size) + 1, 1):
                                
                        #         if listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().size != 0:
                                    
                        #             tiempoTransaccion = 0
                        #             for a in range(1, int(listaEmpresas.returnElement(i).getDato().getTransacciones().size)+1, 1):

                        #                 for b in range (1, int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().size)+1, 1):
                        #                     contador = 1
                        #                     print("==========")
                        #                     for c in range(1, int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().getListadoTrans().size) + 1, 1):

                        #                         # contador = 0
                        #                         if listaEmpresas.returnElement(i).getDato().getTransacciones().returnElement(a).getDato().getIdTransaccion() == listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().getListadoTrans().returnElement(c).getDato().getIdTrans():
                        #                             time_trans = float(listaEmpresas.returnElement(i).getDato().getTransacciones().returnElement(a).getDato().getTiempoAtencion())
                        #                             cant_trans = float(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().getListadoTrans().returnElement(c).getDato().getCantTrans())
                                                    
                        #                             time_trans2 = time_trans * cant_trans

                        #                             tiempoTransaccion += float(time_trans2)
                        #                             print(time_trans)
                        #                             print(cant_trans)
                        #                             print(tiempoTransaccion)
                        #                     print('++++++++++++++')
                        #                     print(tiempoTransaccion)
                        #                     print('++++++++++++++')
                        #                     if b == 1 :
                        #                         listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().setTiempoTras(tiempoTransaccion)
                        #                         listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().setTiempoEspera(0)
                        #                         print('++++++++++++++')
                        #                         print(tiempoTransaccion)
                        #                         print('++++++++++++++')
                        #                         tiempoTransaccion = 0

                        #                     else:
                        #                         listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().setTiempoTras(tiempoTransaccion)

                        #                         tiempo_trans = int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().getTiempoTras())
                        #                         tiempo_anterior = int(listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b-1).getDato().getTiempoEspera())

                        #                         tiempoTotalEspera = float(tiempo_trans + tiempo_anterior)
                        #                         listaEmpresas.returnElement(i).getDato().getPuntosAtencion().returnElement(j).getDato().getClientesPA().returnElement(b).getDato().setTiempoEspera(tiempoTotalEspera)
                        #                         print('++++++++++++++')

                        #                         print(tiempoTransaccion)
                                    
                        #                         print('++++++++++++++')
                        #                         tiempoTransaccion = 0
                                    
                                    


                                

                        print("Se han agregado las configuraciones")
                        print("\n")

                    except:
                        print("NO se pudo cargar el archivo")
                        print("Intentalo Nuevamente")
                        print("\n")
                elif opcion1 == '5':
                    salir1 = True
                else:
                    print('\nIngrese una opcion valida\n')

        elif opcion == '2':
            try:
                if listaEmpresas.size != 0:
                    listaEmpresas.verEmpresa()
                    # print(listaEmpresas.size)

                    print('Ingrese el numero de empresa deseado')
                    eleccion_empresa = input()
                    listaEmpresas.returnElement(int(eleccion_empresa)).getDato().getPuntosAtencion().verPuntoAtencion()
                    seleccion_empresa = listaEmpresas.returnElement(int(eleccion_empresa)).getDato()
                    print('Ingrese el numero del punto de atencion deseado')
                    eleccion_punto = input()
                    seleccion_punto_atencion = listaEmpresas.returnElement(int(eleccion_empresa)).getDato().getPuntosAtencion().returnElement(int(eleccion_punto)).getDato()
                    # print(seleccion_punto_atencion)
                    # print(seleccion_punto_atencion.getIDPA())
                else:
                    print('\nNO HAY EMPRESAS AGREGADAS')
            except:
                print('Vuelve a intentarlo y Selecciona una opcion correcta ')
        
        elif opcion == '3':
            if seleccion_punto_atencion != '':
                print('\nSe ha seleccionado la empresa: ' + str(seleccion_empresa.getNombreEmpresa()))
                print()
                print("Se ha seleccionado el punto de atencion: " + str(seleccion_punto_atencion.getNombrePA()))
                print()

                while True:
                    print("\n======= Manejo de Puntos de Atencion ========")
                    print("1. Ver estado del punto de atención")
                    print("2. Activar escritorio de servicio")
                    print("3. Desactivar escritorio")
                    print("4. Atender cliente")
                    print("5. Solicitud de atención")
                    print('6. Simular actividad del punto de atención')
                    print('7. Regresar')
                    print("===========================================")
                    opcion3 = input()
                    if opcion3 == '1':
                        print('PUNTO DE ATENCION')
                        print(seleccion_punto_atencion.getNombrePA())
                        print('Cantidad de escritorios de servicio activos:')
                        print(seleccion_punto_atencion.getActiveDesk().size)
                        print('Cantidad de escritorios de servicio inactivos:')
                        print(seleccion_punto_atencion.getIdlesDesk().size)
                        print("clientes en espera de atención:")
                        seleccion_punto_atencion.getClientesPA().verClientes()
                        print("Tiempo Minimo de espera:")
                        print('0')
                    elif opcion3 == '2':
                        if seleccion_punto_atencion.getIdlesDesk().size != 0:
                            generarGraphvizDesk(seleccion_punto_atencion.getActiveDesk())
                            print('Presiona ENTER para continuar')
                            a = input()
                            seleccion_punto_atencion.getActiveDesk().insertar(seleccion_punto_atencion.getIdlesDesk().returnElement(int(seleccion_punto_atencion.getIdlesDesk().size)).getDato())
                            seleccion_punto_atencion.getIdlesDesk().borrarNodo(seleccion_punto_atencion.getIdlesDesk().returnElement(int(seleccion_punto_atencion.getIdlesDesk().size)).getDato())
                            print('\nSe ha activado el escritorio\n')
                        else:
                            print('\nNo es posible activar mas escritorios\n')

                        pass
                    elif opcion3 == '3':

                        if seleccion_punto_atencion.getActiveDesk().size != 0 :
                            generarGraphvizDesk(seleccion_punto_atencion.getIdlesDesk())
                            print('Presiona ENTER para continuar')
                            a = input()
                            seleccion_punto_atencion.getIdlesDesk().insertar(seleccion_punto_atencion.getActiveDesk().returnElement(int(seleccion_punto_atencion.getActiveDesk().size)).getDato())
                            seleccion_punto_atencion.getActiveDesk().borrarNodo(seleccion_punto_atencion.getActiveDesk().returnElement(int(seleccion_punto_atencion.getActiveDesk().size)).getDato())
                            
                            generarGraphvizDesk(seleccion_punto_atencion.getIdlesDesk())
                            print('\nSe ha desactivado el escritorio\n')
                        else: 
                            print('\nNO es posible desactivar mas escritorios\n')

                    elif opcion3 == '4':
                        try:
                            if seleccion_punto_atencion.getClientesPA().size != 0:
                                print('Atencion de Clientes')
                                contador_desk = 1
                                generarGraphviz(seleccion_punto_atencion.getClientesPA())
                                input('Prresiona ENTER para continuar')
                                for i in range(1, int(seleccion_punto_atencion.getActiveDesk().size)+1,1):
                                    if seleccion_punto_atencion.getClientesPA().size == 0:
                                        break
                                    print('Se ha atendido a: ' + str(seleccion_punto_atencion.getClientesPA().returnElement(1).getDato().getNombre()))

                                    print(' En el escritorio: ' + str(seleccion_punto_atencion.getActiveDesk().returnElement(int(contador_desk)).getDato().getIdDesk()) +
                                          " Escritorio encargado de " + str(seleccion_punto_atencion.getActiveDesk().returnElement(int(contador_desk)).getDato().getEncargado()))

                                    seleccion_punto_atencion.getClientesPA().borrarNodo(seleccion_punto_atencion.getClientesPA().returnElement(1).getDato())

                                    if seleccion_punto_atencion.getActiveDesk().size > 1:
                                        contador_desk += 1
                                generarGraphviz(seleccion_punto_atencion.getClientesPA())
                            else:
                                print('No hay clientes que atender')
                        except:
                            pass

                    elif opcion3 == '5':
                        try:
                            print('Ingrese nombre del cliente')
                            name_cliente  = input()
                            print('Ingrese DPI del cliente')
                            no_dpi = input()
                            print("listado de transacciones")
                            # seleccion_empresa.getTransacciones().verTransacciones()
                            listadoTransacciones = ListaDoble()
                            while True:
                                seleccion_empresa.getTransacciones().verTransacciones()
                                print('Ingresa el numero de Transaccion que desea. ')
                                transaccion_deseada = input()
                                print('digite el numero de Transacciones que desea')
                                cantidad_trans = input()
                                print('Si ya no desea transacciones ingrese 0')
                                a= input()
                                transss = Transaccion(
                                    seleccion_empresa.getTransacciones().returnElement(int(transaccion_deseada)).getDato().getIdTransaccion(), seleccion_empresa.getTransacciones().returnElement(int(transaccion_deseada)).getDato().getNombreTrans(), seleccion_empresa.getTransacciones().returnElement(int(transaccion_deseada)).getDato().getTiempoAtencion())
                                listadoTransacciones.insertar(transss)
                                if a == '0':
                                    break
                            cliente = Cliente(no_dpi, name_cliente,listadoTransacciones,0,0)
                            seleccion_punto_atencion.getClientesPA().insertar(cliente)
                        except:
                            print("No se ha ingresado el cliente correctamente\nVuelva a intentar")

                    elif opcion3 == '6':
                        try:
                            generarGraphviz(seleccion_punto_atencion.getClientesPA())
                            for x in range(1, int(seleccion_punto_atencion.getClientesPA().size)+1,1):
                                if seleccion_punto_atencion.getClientesPA().size != 0:
                                    print('Atencion de Clientes')
                                    contador_desk = 1


                                    for i in range(1, int(seleccion_punto_atencion.getActiveDesk().size)+1, 1):
                                        if seleccion_punto_atencion.getClientesPA().size == 0:
                                            break
                                        print('Se ha atendido a: ' + str(
                                            seleccion_punto_atencion.getClientesPA().returnElement(1).getDato().getNombre()))

                                        print(' En el escritorio: ' + str(seleccion_punto_atencion.getActiveDesk().returnElement(int(contador_desk)).getDato().getIdDesk()) +
                                              " Escritorio encargado de " + str(seleccion_punto_atencion.getActiveDesk().returnElement(int(contador_desk)).getDato().getEncargado()))

                                        seleccion_punto_atencion.getClientesPA().borrarNodo(
                                            seleccion_punto_atencion.getClientesPA().returnElement(1).getDato())

                                        if seleccion_punto_atencion.getActiveDesk().size > 1:
                                            contador_desk += 1

                            else:
                                print('No hay clientes que atender')
                        except:
                            pass
                    elif opcion3 == '7':
                        break
                    else:
                        print('Ingrese una opcion correcta')

            else:
                print('No se ha sellecionado un punto de Atencion')
        
        elif opcion == '4':
                listaEmpresas.mostrarEmpresas()
        elif opcion == '5':
            listaConfi.mostrarConfiguracion()
        elif opcion == '6':
            salir = True

              
        else: 
            print('\nIngrese una opcion valida\n')




