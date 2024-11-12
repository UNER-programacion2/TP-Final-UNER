import json
from modelos.entidadVineria import EntidadVineria

#from vinoteca import Vinoteca

class Vino(EntidadVineria):
    
    def __init__(self,id, nombre, bodega: str, cepas: list[str], partidas: list[int]):
        super().__init__(id,nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas
    
    def establecerBodega(self):
        self.__bodega
    
    def establecerCepas(self):
        self.__cepas

    def establecerPartida(self):
        self.__partidas 

    #<<CONSULTAS>>
    def obtenerBodega(self):
        from vinoteca import Vinoteca
        bodega = Vinoteca.buscarBodega(self.__bodega)
        return bodega
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca
        cepas_objetos=[]
        for nom_cepa in self.__cepas:
            cepa = Vinoteca.buscarCepa(nom_cepa)
            if cepa:
                cepas_objetos.append(cepa)
            else:
                print(f"cepa no encontrada: {nom_cepa} ")
        return cepas_objetos

    def obtenerPartidas(self):
        return self._partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)
        
    