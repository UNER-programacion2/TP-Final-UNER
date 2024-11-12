import json

from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        
        # Crear objetos y añadirlos a las listas de bodegas, cepas, y vinos
        cls.__bodegas = []
        for bodega_data in datos["bodegas"]:
            cls.__bodegas.append(Bodega(bodega_data["id"], bodega_data["nombre"]))

        cls.__cepas = []
        for cepa_data in datos["cepas"]:
            cls.__cepas.append(Cepa(cepa_data["id"], cepa_data["nombre"]))

        cls.__vinos = []
        for vino_data in datos["vinos"]:
            cls.__vinos.append(Vino(
                vino_data["id"], vino_data["nombre"], vino_data["bodega"],
                vino_data["cepas"], vino_data["partidas"]
            ))

    @classmethod
    def obtenerBodegas(cls):
        return cls.__bodegas

    @classmethod
    def obtenerCepas(cls):
        return cls.__cepas

    @classmethod
    def obtenerVinos(cls):
        return cls.__vinos

    @classmethod
    def buscarBodega(cls, id):
        for bodega in cls.__bodegas:
            if bodega.obtenerId() == id:
                return bodega
        return None

    @classmethod
    def buscarCepa(cls, id):
        for cepa in cls.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None

    @classmethod
    def buscarVino(cls, id):
        for vino in cls.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.__archivoDeDatos, 'r') as archivo:
            return json.load(archivo)
