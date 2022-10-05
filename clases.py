



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

    def setClientes(self, clientes):
        self.clientes = clientes

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

    
class Transaccion:
    def __init__(self,idTransaccion,nombreTransaccion,tiempoAtencion):
        self.idTransaccion  = idTransaccion 
        self.nombreTransaccion = nombreTransaccion
        self.tiempoAtencion = tiempoAtencion
        



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

class ConfiEscritorio:
    def __init__(self,idActiveDesk):
        self.idActiveDesk = idActiveDesk

    def getIdActiveDesk(self):
        return self.idActiveDesk

    def getIDActiveDesk(self):
        return self.idActiveDesk

class Cliente:
    def __init__ (self ,dpi,nombreCLiente,listadoTrans):
        self.dpi = dpi
        self.nombreCliente = nombreCLiente
        self.listadoTrans = listadoTrans

    
class ClienteTrans:
    def __init__(self,idTrans, cantTrans):
        self.idTrans = idTrans
        self.cantTrans = cantTrans

