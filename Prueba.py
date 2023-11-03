from AccesoDatos import Coneccion
from Consultas import Consultas
from Varios import Varios
c = Consultas()
v = Varios()
# registro = [c.Registro(Codigo = 100, Descripcion="Bueno", Costo=25.5)]
# c.Insertar("Insert into productos values(null,?,?,?)", "produccion.sqlite3",registro)
class Menu(Coneccion):
    def __init__(self):
        self.M()

    def M(self):
        
        self.Elegir(self.IngresarProducto, self.IngresarPaquete, self.IngresarPaquete)
             
    def Elegir(self,op1, op2, op3):
        while True:
            v.Opciones("Produccion")
            opcion = v.LeerString("Elige una opcion: ")

            if (opcion == "1"):
                op1
            elif (opcion == "2"):
                op2
            elif (opcion == "3"):
                op3
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")
    def IngresarProducto(self):
        registro = []
        cos = v.LeerString("Codigo: ")
        des = v.LeerString("Descripcion: ")
        pre = v.LeerString("Costo: ")
        registro.append(self.Coleccion(Codigo=cos, Descripcion=des, Costo=pre))
        # registro = []
        # registro.append(self.Coleccion(Codigo = "100", Descripcion="Bueno", Costo="25.5"))
        self.Insertar(c.InsertarTabla("productos","null,?,?,?"), "produccion", registro)
    def IngresarPaquete(self):
        registroE = []
        empaque = v.LeerString("Empaque: ")
        des = v.LeerString("Costo: ")
        registroE.append(self.Coleccion(Empaque=empaque, Costo=pre))
        self.Insertar(c.InsertarTabla("empaque","null,?,?"), "produccion", registroE)
#  self, query, base, coleccion