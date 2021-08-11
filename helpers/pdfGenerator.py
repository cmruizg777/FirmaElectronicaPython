# Python program to convert
# text file to pdf file


from fpdf import FPDF


class pdfGenerator:

    def generateRemissionGuidePdf(self, data, logo_file):

        infoTributariaEmpresa = data[0][0]
        infoTributariaSecuenciales = data[1][0]
        infoTransportista = data[2][0]
        infoDestinatario = data[3][0]
        infoDetalles = data[4]
        secuencialLength = len(str(infoTributariaSecuenciales[6]))
        zeros = ''

        for i in range(9 - secuencialLength):
            zeros += '0'

        secuencial = zeros + str(infoTributariaSecuenciales[6])
        fecha = infoTributariaSecuenciales[7]
        razonSocial = infoTributariaEmpresa[1]
        nombreComercial = infoTributariaEmpresa[1]
        ruc = infoTributariaEmpresa[-3]
        dirMatriz = infoTributariaEmpresa[3]
        ptoEmision = infoTributariaSecuenciales[4]
        sucursal = infoTributariaSecuenciales[5]  # sucursal
        dirEstablecimiento = infoTributariaEmpresa[3]
        dirPartida = infoTributariaEmpresa[3]
        razonSocialTransportista = infoTransportista[4]
        tipoIdentificacionTransportista = "04"
        rucTransportista = infoTransportista[2]
        obligadoContabilidad = "NO"
        fechaIniTransporte = infoTributariaSecuenciales[7]
        fechaFinTransporte = infoTributariaSecuenciales[7]
        placa = infoTransportista[-2].strip()
        identificacionDestinatario = infoDestinatario[3]
        razonSocialDestinatario = infoDestinatario[4]
        dirDestinatario = infoDestinatario[5]
        motivoTraslado = "MOVILIZACION DE MERCADERIA"
        ##################################### CREACION DE OBJETO FPDF #############################################
        pdf = FPDF(unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font('Times', '', 10.0)
        epw = pdf.w - 2 * pdf.l_margin
        # Set column width to 1/4 of effective page width to distribute content
        # evenly across table and page
        col_width = epw / 2
        # Document title centered, 'B'old, 12 pt
        #################################### SECCION LOGO ###########################################################
        col_width = epw / 2
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size * 1
        pdf.set_xy(pdf.l_margin, pdf.t_margin)
        # pdf.cell(col_width, th*35, '', align='L', border=1)

        normal_margin = pdf.l_margin
        pdf.image(logo_file, x=None, y=None, h=5 * th, w=col_width)

        #################################### SECCION SECUENCIAS ###########################################################
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size*2
        pdf.set_fill_color(52, 103, 235)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_width, th, 'GUIA DE REMISION' , align='C', border=0,  ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(col_width, th, 'No. ' + sucursal +'-'+ ptoEmision +'-'+ secuencial, align='L', border=0,  ln=1)
        barcodeImg = 'files/img/barcode.png'
        pdf.image(barcodeImg, x=None, y=None, h=2 * th, w=col_width)

        pdf.set_font('Times', '', 8.0)
        th = pdf.font_size * 1
        pdf.cell(col_width, th, 'PDF SIN AUTORIZACION', align='C', border=0, ln=1)
        pdf.ln(th)
        #################################### SECCION AUTORIZACION ###########################################################
        col_width = epw / 6
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size * 2
        pdf.cell(col_width, th, 'Fecha y Hora:', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 12.0)
        pdf.cell(col_width*2, th, fecha , align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 12.0)
        pdf.cell(col_width, th, 'Ambiente:', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 12.0)
        pdf.cell(col_width * 2, th, 'PRUEBAS', align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 12.0)
        pdf.cell(col_width, th, 'Emision:', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 12.0)
        pdf.cell(col_width * 2, th, 'NORMAL', align='L', border=0, ln=1)
        #################################### SECCION EMPRE ###########################################################
        col_width = epw / 2
        pdf.set_left_margin(normal_margin + col_width)
        pdf.set_xy(pdf.l_margin, pdf.t_margin)

        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_width, th, 'EMPRESA', align='C', border=0, ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th * 1.5, razonSocial, align='C', border=0, ln=1)

        pdf.set_font('Times', '', 10.0)
        th = pdf.font_size
        pdf.cell(col_width, th * 1.5, nombreComercial, align='C', border=0, ln=1)

        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size * 1.5
        col_width = epw / 6
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width*1, th, 'Dirección:', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.multi_cell(col_width*2, th, dirMatriz, align='L', border=0)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 1, th, 'RUC:', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 2, th, ruc, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width*2, th, 'Obligado a llevar Contabilidad :', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width*1, th, 'NO', align='C', border=0, ln=1)
        pdf.ln(th)
        #################################### SECCION TRANSPORTISTA ###########################################################

        col_width = epw / 2
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_width, th, 'TRANSPORTISTA', align='C', border=0, ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)

        col_width = epw / 4
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Nombres Apellidos ', align='L', border=0, ln=1)
        pdf.cell(col_width, th, '/ Razón Social ', align='L', border=0, ln=0)
        pdf.set_xy(pdf.get_x(), pdf.get_y() - th)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, 2 * th, razonSocialTransportista, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'RUC/CI Transp.', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, th, rucTransportista, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Placas Vehiculo', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, th, placa, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Punto Partida', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, th, ptoEmision, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Fecha Inicio', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, th, fecha, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Fecha Fin', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width, th, fecha, align='L', border=0, ln=1)

        #################################### SECCION DESTINOS ###########################################################
        col_width = epw / 8
        pdf.ln(th * 2)
        pdf.set_font('Times', 'B', 10.0)
        pdf.set_left_margin(normal_margin)
        pdf.set_x(pdf.l_margin)

        th = pdf.font_size

        yTransporte = pdf.get_y()
        pdf.cell(col_width * 3, th, 'Motivo Traslado', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, motivoTraslado, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 3, th, 'Destino(Punto de Llegada)', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, dirDestinatario, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 3, th, 'Identificación(Destinatario)', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, identificacionDestinatario, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 3, th, 'Razón Social/ Nombres y Apellidos', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, razonSocialDestinatario, align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 3, th, 'Documento aduanero', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, '', align='L', border=0, ln=1)
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width * 3, th, 'Ruta', align='L', border=0, ln=0)
        pdf.set_font('Times', '', 10.0)
        pdf.cell(col_width * 5, th, '', align='L', border=0, ln=1)
        pdf.set_y(yTransporte-th)
        pdf.cell(epw, 9 * th, border=1, ln=1)

        #################################### SECCION DETALLES ###########################################################
        col_width = epw / 6
        pdf.set_text_color(255, 255, 255)
        th = pdf.font_size*2
        pdf.cell(col_width, th, 'Cantidad', align='C', border=0, ln=0, fill=True)
        pdf.cell(col_width*3, th, 'Descripción', align='C', border=0, ln=0, fill=True)
        pdf.cell(col_width, th, 'Cod. Principal', align='C', border=0, ln=0, fill=True)
        pdf.cell(col_width, th, 'Cod. Auxiliar', align='C', border=0, ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)

        pdf.set_font('Times', '', 10.0)
        for infoDetalle in infoDetalles:
            codigoInterno = str(infoDetalle[0])
            codigoAdicional = str(infoDetalle[0])
            descripcion = str(infoDetalle[5])
            cantidad = str(infoDetalle[-3])
            pdf.cell(col_width, th, cantidad, align='C', border=1, ln=0)
            pdf.cell(col_width * 3, th, descripcion, align='C', border=1, ln=0)
            pdf.cell(col_width, th, codigoInterno, align='C', border=1, ln=0)
            pdf.cell(col_width, th, codigoAdicional, align='C', border=1, ln=1)

        pdf.output('testPdf.pdf', 'F')



