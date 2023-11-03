class Consultas:
    def InsertarTabla(self,tabla,datos):
        # Producto = (f"Insert into {tabla} values({datos})")
        return (f"Insert into {tabla} values({datos})")
    def Operacion(self, dato, tabla, ide):
        query = (f"Select {dato} from {tabla} where {ide} = id")
    def __init__(self):
        self.Operacion("costo", "producto", "2")