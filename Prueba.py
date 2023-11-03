from AccesoDatos import Coneccion
# registro = [c.Registro(Codigo = 100, Descripcion="Bueno", Costo=25.5)]
# c.Insertar("Insert into productos values(null,?,?,?)", "produccion.sqlite3",registro)
class Prueba(Coneccion):
    registro = [self.Registro(Codigo = "100", Descripcion="Bueno", Costo="25.5")]
    def __init__(self):
        self.Insertar("Insert into productos values(null,?,?,?)", "produccion.sqlite3",self.registro)
#  self, query, base, coleccion