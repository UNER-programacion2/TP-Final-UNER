import json
from modelos.entidadVineria import EntidadVineria
#from vinoteca import Vinoteca

class Cepa(EntidadVineria):

    # hereda de entidadVineria
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    ### Consultas
    def obtenerVinos(self):  
        from vinoteca import Vinoteca  # Importación retrasada para evitar el ciclo de dependencias

        vinos_con_cepa = []
        vinos = Vinoteca.obtenerVinos()
        for vino in vinos:
            if self in vino.obtenerCepas():
                vinos_con_cepa.append(vino)
        return vinos_con_cepa

######################################################################
######Esto ya estaba en el código original
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)