



from pickletools import read_uint1


class Empresa:
    def __init__ (self, idEmpresa, nombreEmpresa,abreviaturaEmpresa,puntosAtencion,transacciones):
        self.idEmpresa = idEmpresa
        self.nombreEmpresa = nombreEmpresa
        self.abreviaturaEmpresa = abreviaturaEmpresa
        self.puntosAtencion = puntosAtencion
        self.transacciones = transacciones

    def getIDEmpresa(self):
        return self.idEmpresa 

    def getPuntosAtencion(self):
        return self.puntosAtencion
    
    def getNombreEmpresa(self):
        return self.nombreEmpresa

    def getAbreviatura(self):
        return self.abreviaturaEmpresa

    def getTransacciones(self):
        return self.transacciones

class PuntoAtencion:
    def __init__ (self,idPA,nombrePA,direccionPA,activeDesks,idlesDesks, clientes):
        self.idPA = idPA
        self.nombrePA = nombrePA
        self.direccionPA = direccionPA
        self.activeDesks = activeDesks
        self.idlesDesks = idlesDesks
        self.clientes = clientes

    def getIDPA(self):
        return self.idPA

    def getNombrePA(self):
        return self.nombrePA

    def getDireccionPA(self):
        return self.direccionPA

    def setClientes(self, clientes):
        self.clientes = clientes

    def getClientesPA(self):
        return self.clientes

    def setActiveDesks(self, activeDesks):
        self.activeDesks = activeDesks

    def getActiveDesk(self):
        return self.activeDesks
    
    def getIdlesDesk(self):
        return self.idlesDesks

class Escritorio:
    def __init__(self, idDesk, identificacionDesk, nombreEncargadoDesk):
        self.idDesk = idDesk
        self.identificacionDesk = identificacionDesk
        self.nombreEncargadoDesk = nombreEncargadoDesk

    def getIdDesk(self):
        return self.idDesk
    def getEncargado(self):
        return self.nombreEncargadoDesk
    
class Transaccion:
    def __init__(self,idTransaccion,nombreTransaccion,tiempoAtencion):
        self.idTransaccion  = idTransaccion 
        self.nombreTransaccion = nombreTransaccion
        self.tiempoAtencion = tiempoAtencion

    def getTiempoAtencion(self):
        return self.tiempoAtencion

    def getIdTransaccion(self):
        return self.idTransaccion

    def getNombreTrans(self):
        return self.nombreTransaccion
    
        



class ConfiguracionInical:
    def __init__ (self, codConfi, codEmpresa, codPunto,activeDesks,clientes):
        self.codConfi = codConfi
        self.codEmpresa = codEmpresa
        self.codPunto = codPunto
        self.activeDesks = activeDesks
        self.clientes = clientes
    
    def getActiveDesk(self):
        return self.activeDesks

    def getCodEmpresa(self):
        return self.codEmpresa

    def getCodPunto(self):
        return self.codPunto

    def getClientes(self):
        return self.clientes

class ConfiEscritorio:
    def __init__(self,idActiveDesk):
        self.idActiveDesk = idActiveDesk

    def getIdActiveDesk(self):
        return self.idActiveDesk

    def getIDActiveDesk(self):
        return self.idActiveDesk

class Cliente:
    def __init__ (self ,dpi,nombreCLiente,listadoTrans,tiempoTransaccion, tiempoespera):
        self.dpi = dpi
        self.nombreCliente = nombreCLiente
        self.listadoTrans = listadoTrans
        self.tiempoTransaccion = tiempoTransaccion
        self.tiempoespera  = tiempoespera

    def getTiempoTras(self):
        return self.tiempoTransaccion

    def getTiempoEspera(self):
        return self.tiempoespera

    def setTiempoTras(self, tiempoTransaccion):
        self.tiempoTransaccion = tiempoTransaccion

    def setTiempoEspera(self, tiempoespera):
        self.tiempoespera = tiempoespera

    def getListadoTrans(self):
        return self.listadoTrans 

    def getNombre(self):
        return self.nombreCliente

    def getDPI(self):
        return self.dpi


    
class ClienteTrans:
    def __init__(self,idTrans, cantTrans):
        self.idTrans = idTrans
        self.cantTrans = cantTrans

    def getIdTrans(self):
        return self.idTrans

    def getCantTrans(self):
        return self.cantTrans

    

