import json
from modelos.entidadVineria import EntidadVineria

class Vino(EntidadVineria):
        
    def __init__(self,id, nombre, bodega: str, cepas: list[str], partidas: list[int]):
            super().__init__(id,nombre)
            self._bodega = bodega
            self._cepas = cepas
            self._partidas = partidas
        
    def establecerBodega(self):
        self._bodega
    
    def establecerCepas(self):
        self._cepas

    def establecerPartida(self):
        self._partidas 

    #<<CONSULTAS>>
    def obtenerBodega(self):
        from vinoteca import Vinoteca
        bodega = Vinoteca.buscarBodega(self._bodega)
        return bodega
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        cepas_objetos=[]
        for nom_cepa in self._cepas:
            cepa = Vinoteca.buscarCepa(nom_cepa)
            if cepa:
                cepas_objetos.append(cepa)
            else:
                print(f"cepa no encontrada: {nom_cepa} ")
        return cepas_objetos

    def obtenerPartidas(self):
        return self._partidas


######################################################################
######Esto ya estaba en el código original
    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self._partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)