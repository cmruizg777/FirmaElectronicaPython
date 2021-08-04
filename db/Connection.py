import pyodbc as pyodbc

class Connection():

    def __init__(self):
        try:

            self.cnxn = pyodbc.connect(r'Driver=SQL Server;Server=EDWIN-PC\DESARROLLO;Database=DBGUIASREMISION;Trusted_Connection=yes;')

            print("Conexion Exitosa!")
        except Exception as e:
            print("Ocurrió un error al conectar a SQL Server: ", e)

    def getCursor(self):
        return self.cnxn.cursor()

    def __del__(self):
        self.cnxn.close()