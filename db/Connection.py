import pyodbc as pyodbc

class Connection():

    def __init__(self):
        try:
            self.cnxn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=eFacturacion;Trusted_Connection=yes;')
            print("Conexion Exitosa!")
        except Exception as e:
            print("Ocurrió un error al conectar a SQL Server: ", e)

    def getConnection(self):
        return self.cnxn

    def __del__(self):
        self.cnxn.close()