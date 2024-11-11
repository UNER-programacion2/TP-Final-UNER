import json
from entidadVineria import EntidadVineria
from vinoteca import Vinoteca
from vino import Vino

class Cepa(EntidadVineria):

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

###consultas
    def obtenerVinos(self, vino:Vinoteca):  ####NO SE SI FUNCIONA O ESTA BIEN. V
        vinos = Vinoteca.obtenerVinos()
        vinosCepa = []
        
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                if cepa.obtenerId() == self.obtenerId():
                    vinosCepa.append(vino)
                    break
        return vinosCepa

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


