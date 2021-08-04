import db.Connection as db
import pyodbc as pyodbc


class guideRemission:
    fecha = ''
    secuencial = ''
    ambiente = ''
    emision = ''
    def getgGuideRemissionData(self):
        try:
            self.myDbConnection = db.Connection()
            cursor = self.myDbConnection.getCursor()
            cursor.execute("{call sp_xml_guiaRemision(192,'SAROCIBE')}")
            tables = [];
            dataset = cursor.fetchall()
            tables.append(dataset);
            #print(dataset)
            while (cursor.nextset()):
                dataset = cursor.fetchall()
                #print(dataset)
                tables.append(dataset);
            return tables
        except pyodbc.Error as ex:
            print(ex)
        except:
            print('Error')