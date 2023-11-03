import sqlite3
class Coneccion:
    # Funcion para general para insertar datos
    def Insertar(self, query, base, coleccion):
        with sqlite3.connect(base) as conn:
            com = query
            for c in coleccion:
                conn.execute(com, tuple(c.values()))
                conn.commit()
    # Funcion general para mostrar datos
    def Mostrar(self, tabla, base):
        with sqlite3.connect(base) as conn:
            # com = query
            com = (f"SELECT * FROM {tabla}")
            rs = conn.execute(com)
            return rs.fetchall()
    # Funcion para agregar datos a las consultas
    def Registro(self, **datos):
        return datos
