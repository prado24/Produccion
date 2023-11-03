class Consultas:
    def InsertarProducto(self,tabla,datos):
        Producto = (f"Insert into {tabla} values({datos})")