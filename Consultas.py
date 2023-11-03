from AccesoDatos import Coneccion
class Consultas(Coneccion):
    def InsertarTabla(self,tabla,datos):
        # Producto = (f"Insert into {tabla} values({datos})")
        return (f"Insert into {tabla} values({datos})")
    def ObtenerCosto(self, dato,idp,ide, base):
        # [print(f"{c}") for c in self.Operacion((f"Select {dato} from {tabla} where id = {ide}"), (f"{base}"))]
        costop = self.Operacion((f"Select {dato} from productos where id = {idp}"), (f"{base}"))
        costoe = self.Operacion((f"Select {dato} from empaque where ide = {ide}"), (f"{base}"))
        valorp = costop[0][0]
        valore = costop[0][0]
        valor_costo = float(valorp)
        valor_empaque = float(valore)
        print(valor_costo)
        print(valor_empaque)
        # resultado_final = valor_float * 2
        # print(resultado_final)
    # def __init__(self):
    #    self.ObtenerCosto("costo","2","1", "produccion")