import pyodbc as pyodbc

class Connection():
    cnxn = None
    def __init__(self):
        try:

            self.cnxn = pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=DBGUIASREMISION;Trusted_Connection=yes;')

            print("Conexion Exitosa!")
        except Exception as e:
            print("Ocurrió un error al conectar a SQL Server: ", e)

    def getCursor(self):
        return self.cnxn.cursor()

