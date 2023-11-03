import sqlite3
class Coneccion:
    # Funcion para general para insertar datos
    def Insertar(self, query, base, coleccion):
        with sqlite3.connect(f"{base}.sqlite3") as conn:
            com = query
            for c in coleccion:
                conn.execute(com, tuple(c.values()))
                conn.commit()
    # Funcion general para mostrar datos
    def Mostrar(self, query, base):
        with sqlite3.connect(f"{base}.sqlite3") as conn:
            # com = query
            com = query
            rs = conn.execute(com)
            return rs.fetchall()
    # Funcion para obtener costo de producto por id
    def Operacion(self,query,base):
        with sqlite3.connect(f"{base}.sqlite3") as conn:
            com = query
            rs = conn.execute(com)
            return rs.fetchall()
    # Funcion para agregar a una lista varios datos
    def Coleccion(self, **datos):
        return datos
        # Funcion para agergar registros a la lista


