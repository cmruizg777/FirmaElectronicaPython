from datetime import date

class Modulo11DTO:
    Fecha              = date.today()
    TipoComprobante    = ''
    RucEmpresa         = ''
    Ambiente           = ''
    PtoEmision         = ''
    Sucursal           = ''
    Secuencial         = ''
    Digito8            = ''
    def __init__(self, fecha, tipoComprobante, rucEmpresa, ambiente, ptoEmision, sucursal, secuencial, digito8 = ''):
        self.Fecha = fecha
        self.TipoComprobante = tipoComprobante
        self.RucEmpresa = rucEmpresa
        self.Ambiente = ambiente
        self.PtoEmision = ptoEmision
        self.Sucursal = sucursal
        self.Secuencial = secuencial
        self.Digito8 = digito8