


class Empresa:
    def __init__ (self, idEmpresa, nombreEmpresa,abreviaturaEmpresa,puntosAtencion,transacciones):
        self.idEmpresa = idEmpresa
        self.nombreEmpresa = nombreEmpresa
        self.abreviaturaEmpresa = abreviaturaEmpresa
        self.puntosAtencion = puntosAtencion
        self.transacciones = transacciones

    def getiIDEmpresa(self):
        return self.idEmpresa 

class PuntoAtencion:
    def __init__ (self,idPA,nombrePA,direccionPA,escritorios,clientes):
        self.idPA = idPA
        self.nombrePA = nombrePA
        self.direccionPA = direccionPA
        self.escritorios = escritorios
        self.clientes = clientes

    def setClientes(self, clientes):
        self.clientes = clientes

class Escritorio:
    def __init__(self, idDesk, identificacionDesk, nombreEncargadoDesk, activeDesk, idleDesk):
        self.idDesk = idDesk
        self.identificacionDesk = identificacionDesk
        self.nombreEncargadoDesk = nombreEncargadoDesk
        self.activeDesk = activeDesk
        self.idleDesk = idleDesk

    def setActiveDesk(self, activeDesk):
        self.activeDesk = activeDesk
    
    def getActiveDesk(self):
        return self.activeDesk

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

class ConfiEscritorio:
    def __init__(self,idActiveDesk):
        self.idActiveDesk = idActiveDesk

class Cliente:
    def __init__ (self ,dpi,nombreCLiente,listadoTrans):
        self.dpi = dpi
        self.nombreCliente = nombreCLiente
        self.listadoTrans = listadoTrans

    
class ClienteTrans:
    def __init__(self,idTrans, cantTrans):
        self.idTrans = idTrans
        self.cantTrans = cantTrans

