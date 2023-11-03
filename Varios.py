from AccesoDatos import Coneccion
class Varios(Coneccion):
    op = ["Ingresar Producto", "Ingresar Paquete", "Ingresar Detallaes de Paquete", "Salir"]
    # def __init__(self):
        # self.Opciones()
    def LeerInt(self, entero):
        return int(input(entero))
    def LeerFloat(self, flotante):
        return float(input(flotante))
    def LeerString(self, texto):
        return input(texto)
    def Opciones(self, titulo):
        print(titulo)
        # self.op.append("Ingresar Producto")
        # self.op.append("Ingresar Paquete")
        # self.op.append("Ingresar Detalles de Paquete")
        # self.op.append("Salir")
        [print(f"{num+1}. {opciones}") for num, opciones in enumerate(self.op)]