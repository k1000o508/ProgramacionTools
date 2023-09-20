#Clases Universales para el proceso C.R.U.D de sqlite3
class UniversalCRUD():
    class ChargeState():
        def __init__(self,table):
            global nombres
            self.table = table  

        def InputData(self):
            cursor = conector.cursor()
            cursor.execute("SELECT name FROM pragma_table_info('"+ self.table +"')")
            nombres = cursor.fetchall()
            print('Campos de la tabla',cursor.fetchall())
            datos = []
            for i in nombres:
                if "ID" in i[0]:
                    pass
                else:
                    datos.append(input("Ingrese el campo " + i[0] + ' > '))
            
            cursor = conector.cursor()
            
            #Adaptacion para sqlite (?,?,?,?,?)


            #ATENCION: NO EJECUTAR SIN VALIDAR LOS DATOS ANTERIORMENTE
            # print((len(datos)/2)-1)

            # print(len(datos))

            # print(datos)

            # ValuesInputs = "?,"*((len(datos)))

            #Sacamos la coma de mas (?,?,?,?,?,) <<<
            # ValuesInputs = ValuesInputs[:-1]

            # cursor.executemany("INSERT INTO "+ self.table +" VALUES (null," + ValuesInputs + ")",datos)
            # conector.commit()   


    class ReadState():

    def __init__(self,table):
        self.table = table

    def ReadAll(self):
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        #Tabulate formate table 
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)

    def ReadColumn(self):
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        print(len(rows))

        IdOption = numeric(input("Registro especifico(ID) : "),1,len(rows))

        #Arreglar Error del fetchall()
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + " WHERE ID = '"+ IdOption +"'")
        rows = c.fetchall()
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)
            

    class UpdateState():
        # def __init__(self,table,column,modify,columnId,id):
        #     self.table = table 
        #     self.column = column
        #     self.id = id 
        #     self.columnId = columnId
        #     self.modify = modify 

        def __init__(self,table):
            self.table = table 

        def UpdateTable(self,column,modify,id):
            self.column = column #Columna que sera modificada
            self.id = id #Id unico de cada instancia 
            self.modify = modify #Dato guardado en una instancia anterior que sera modificada

            c = conector.cursor()
            c.execute("UPDATE " + self.table + " SET " + self.column + "='" + self.modify + "' WHERE ID ='" + self.id + "'")
            c.commit()

            c.close()

    class DeleteState():
        def __init__(self,table):
            self.table = table        

        def DeleteTableColumn(self,id):
            self.id = id
            c = conector.connect("GestionGanadera.db")
            c.execute("DELETE FROM "+ self.table +" WHERE ID ='"+self.id+"'")
            c.commit()

            c.close()

        #Inhabilitado para el usuario comun
        def DeleteTable(self):
            c = conector.connect("GestionGanadera.db")
            c.execute("DELETE FROM "+ self.table +"")
            c.commit()

            c.close()
