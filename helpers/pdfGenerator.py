# Python program to convert
# text file to pdf file


from fpdf import FPDF


class pdfGenerator:

    def generateRemissionGuidePdf(self, data):

        pdf = FPDF(unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font('Times', '', 10.0)
        epw = pdf.w - 2 * pdf.l_margin
        # Set column width to 1/4 of effective page width to distribute content
        # evenly across table and page
        col_width = epw / 2
        # Document title centered, 'B'old, 12 pt

        #################################### SECCION NRO 1 ###########################################################
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size*2
        pdf.set_fill_color(52, 103, 235)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_width, th, 'GUIA DE REMISION NRO: ' + '001', align='C', border=0,  ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(col_width, th, 'CLAVE DE ACCESO - AUTORIZACIÓN', align='L', border=0,  ln=1)
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size * 4
        pdf.cell(col_width, th, 'Codigo de barras', align='L', border=0, ln=1)
        pdf.set_font('Times', '', 8.0)
        th = pdf.font_size * 1
        pdf.cell(col_width, th, 'PDF SIN AUTORIZACION' + data.secuencial , align='C', border=0, ln=1)

        #################################### SECCION NRO 2 ###########################################################
        col_width = epw / 6
        pdf.set_font('Times', 'B', 12.0)
        th = pdf.font_size * 1
        pdf.cell(col_width, th, 'Fecha y Hora:', align='L', border=0, ln=0)
        pdf.cell(col_width*2, th,  data.fecha, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Ambiente:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.ambiente, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Emision:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.emision, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Fecha Inicio:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Fecha Fin:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)

        #################################### SECCION NRO 3 ###########################################################
        col_width = epw / 2
        pdf.set_text_color(255, 255, 255)
        pdf.cell(col_width, th*2, 'IDENTIFICACION CLIENTE', align='C', border=0, ln=1, fill=True)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(col_width, th*1.5, 'NOMBRE CLIENTE', align='C', border=0, ln=1)

        col_width = epw / 6
        pdf.cell(col_width, th, 'Identificación:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Hora Llegada:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.ambiente, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Libras programadas:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.emision, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Biologo:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Guardia:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)
        pdf.cell(col_width, th, 'Dirección:', align='L', border=0, ln=0)
        pdf.cell(col_width * 2, th, data.fecha, align='L', border=0, ln=1)

        #################################### SECCION NRO 4 ###########################################################
        col_width = epw*0.96 / 4
        pdf.set_font('Times', 'B', 10.0)
        pdf.set_xy(pdf.get_x(), pdf.get_y() + 2*th)
        yTransporte = pdf.get_y()
        pdf.cell(col_width, th, 'Via Maritima', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Nombre Embarcación ', align='L', border='LRT', ln=1)
        pdf.cell(col_width, th, '/ Gabarra ', align='L', border='LRB', ln=0)
        pdf.set_xy(pdf.get_x(),pdf.get_y()-th)
        pdf.cell(col_width, 2*th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Nombre del Marinero', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Fluvial / Patrón Costero', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Ruc/ C.I. Transportista', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Matrícula Embarcación"', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)

        #################################### SECCION LOGO ###########################################################
        col_width = epw / 2
        pdf.set_xy(pdf.l_margin, pdf.t_margin)
        #pdf.cell(col_width, th*35, '', align='L', border=1)

        normal_margin = pdf.l_margin
        pdf.set_left_margin(normal_margin + col_width)
        pdf.set_y(yTransporte)
        col_width = epw / 4
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(col_width, th, 'Via Terrestre', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Nombres Apellidos ', align='L', border='LRT', ln=1)
        pdf.cell(col_width, th, '/ Razón Social ', align='L', border='LRB', ln=0)
        pdf.set_xy(pdf.get_x(), pdf.get_y() - th)
        pdf.cell(col_width, 2 * th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'RUC/CI Transp.', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Placas Vehiculo', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, 'Marca Vehiculo', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)
        pdf.cell(col_width, th, '', align='L', border=1, ln=0)
        pdf.cell(col_width, th, '', align='L', border=1, ln=1)

        pdf.output('testPdf.pdf', 'F')



