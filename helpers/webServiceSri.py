from io import StringIO
import base64
import helpers.models.utils as utils
from suds.client import Client

class webServiceSri(object):
    __AMBIENTE_PRUEBA = '1'
    __AMBIENTE_PROD = '2'
    __ACTIVE_ENV = False
    # revisar el utils
    __WS_TEST_RECEIV = 'https://celcer.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl'  # noqa
    __WS_TEST_AUTH = 'https://celcer.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl'  # noqa
    __WS_RECEIV = 'https://cel.sri.gob.ec/comprobantes-electronicos-ws/RecepcionComprobantesOffline?wsdl'  # noqa
    __WS_AUTH = 'https://cel.sri.gob.ec/comprobantes-electronicos-ws/AutorizacionComprobantesOffline?wsdl'  # noqa

    __WS_TESTING = (__WS_TEST_RECEIV, __WS_TEST_AUTH)
    __WS_PROD = (__WS_RECEIV, __WS_AUTH)

    _WSDL = {
        __AMBIENTE_PRUEBA: __WS_TESTING,
        __AMBIENTE_PROD: __WS_PROD
    }
    __WS_ACTIVE = __WS_TESTING

    @classmethod
    def set_active_env(self, env_service):
        if env_service == self.__AMBIENTE_PRUEBA:
            self.__ACTIVE_ENV = self.__AMBIENTE_PRUEBA
        else:
            self.__ACTIVE_ENV = self.__AMBIENTE_PROD
        self.__WS_ACTIVE = self._WSDL[self.__ACTIVE_ENV]

    @classmethod
    def get_active_env(self):
        return self.__ACTIVE_ENV

    @classmethod
    def get_env_test(self):
        return self.__AMBIENTE_PRUEBA

    @classmethod
    def get_env_prod(self):
        return self.__AMBIENTE_PROD

    @classmethod
    def get_ws_test(self):
        return self.__WS_TEST_RECEIV, self.__WS_TEST_AUTH

    @classmethod
    def get_ws_prod(self):
        return self.__WS_RECEIV, self.__WS_AUTH

    @classmethod
    def get_active_ws(self):
        return self.__WS_ACTIVE
    @classmethod
    def get_receipt_soap_envelope_xml(self, document):
        return '<soapenv:Envelope  xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ec="http://ec.gob.sri.ws.recepcion"><soapenv:Header/><soapenv:Body><ec:validarComprobante><!--Optional:--><xml>"'+document+'"</xml>\</ec:validarComprobante></soapenv:Body></soapenv:Envelope>'

    @classmethod
    def send_receipt(self, document:str):
        buf = StringIO()
        buf.write(document)
        #print(buf.getvalue())
        buffer_xml = base64.b64encode(bytes(buf.getvalue().encode('utf-8')))
        text = buffer_xml.decode('ascii')
        #print(buffer_xml.decode('ascii'))
        #print(len(buffer_xml))
        if not utils.check_service('prueba'):
            # TODO: implementar modo offline
            raise Exception('Error SRI', 'Servicio SRI no disponible.')

        client = Client(self.get_active_ws()[0])
        result = client.service.validarComprobante(buffer_xml.decode('ascii'))
        errores = []

        #print(result.status_code)
        #print(result)

        if result.estado == 'RECIBIDA':
            return True, errores
        else:
            for comp in result.comprobantes:
                for m in comp[1][0].mensajes:
                    rs = [m[1][0].tipo, m[1][0].mensaje]
                    rs.append(getattr(m[1][0], 'informacionAdicional', ''))
                    errores.append(' '.join(rs))

            return False, ', '.join(errores)

    @classmethod
    def request_authorization(self, access_key):
        messages = []
        client = Client(self.get_active_ws()[1])
        result = client.service.autorizacionComprobante(access_key)
        print(result)
        autorizacion = result.autorizaciones[0][0]
        mensajes = autorizacion.mensajes and autorizacion.mensajes[0] or []

        for m in mensajes:
            messages.append([m.identificador, m.mensaje,
                             m.tipo, m.informacionAdicional])
        if not autorizacion.estado == 'AUTORIZADO':
            return False, messages
        return autorizacion, messages