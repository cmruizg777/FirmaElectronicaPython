from datetime import date


class Module11:

    def __init__(self, fecha, tipoComprobante, rucEmpresa, ambiente, ptoEmision, sucursal, secuencial, digito8=''):
        self.Fecha = fecha
        self.TipoComprobante = tipoComprobante
        self.RucEmpresa = rucEmpresa
        self.Ambiente = ambiente
        self.PtoEmision = ptoEmision
        self.Sucursal = sucursal
        self.Secuencial = secuencial
        self.Digito8 = digito8

    def getModule11(self):



        year = self.Fecha.strftime("%Y")
        month = self.Fecha.strftime("%m")
        day = self.Fecha.strftime("%d")
        claveAcceso = (
                day+month+year +
                self.TipoComprobante +
                self.RucEmpresa +
                self.Ambiente +
                self.PtoEmision +
                self.Sucursal +
                self.Secuencial +
                self.Digito8 +
                "1"
        )

        suma = 0
        factor = [3, 2, 7, 6, 5, 4]
        #claveAccesoArray = claveAcceso.split("")
        index = 0
        idx = 0
        for item in claveAcceso:

            if idx%6 == 0:
                index = 0
            currentFactor = factor[index]
            suma = suma + int(item) * currentFactor

            #factor = factor - 1
            #if (factor == 1):
            #    factor = 7
            index += 1
            idx += 1
        digitoVerificador = (suma % 11)
        digitoVerificador = 11 - digitoVerificador

        if (digitoVerificador == 11):
            digitoVerificador = 0

        if (digitoVerificador == 10):
            digitoVerificador = 1

        return claveAcceso + str(digitoVerificador)
