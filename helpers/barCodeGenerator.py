from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
class barCodeGenerator:
    def generate(self, input=''):
        # print to a file-like object:
        #rv = BytesIO()
        #Code128(input, writer=ImageWriter()).write(rv)

        # or sure, to an actual file:
        with open('files/img/barcode.png', 'wb') as f:
            Code128(input, writer=ImageWriter()).write(f)