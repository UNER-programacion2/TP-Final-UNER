# vinoteca.py
import json
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    __archivoDeDatos = "vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso="no"):
        if orden == "nombre":
            return cls.bodegas[::-1] if reverso == "si" else cls.bodegas
        elif orden == "vinos":
            return sorted(cls.bodegas, key=lambda b: len(b.obtenerVinos()), reverse=(reverso == "si"))
        return cls.bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso="no"):
        if orden == "nombre":
            return sorted(cls.cepas, key=lambda c: c.obtenerNombre(), reverse=(reverso == "si"))
        return cls.cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso="no"):
        vinos_filtrados = [v for v in cls.vinos if anio in v.obtenerPartidas()] if anio else cls.vinos
        if orden == "nombre":
            vinos_filtrados.sort(key=lambda v: v.obtenerNombre(), reverse=(reverso == "si"))
        elif orden == "bodega":
            vinos_filtrados.sort(key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=(reverso == "si"))
        return vinos_filtrados

    @classmethod
    def buscarBodega(cls, id):
        for b in cls.bodegas:
            if b.obtenerId() == id:
                return b
        return None

    @classmethod
    def buscarCepa(cls, id):
        for c in cls.cepas:
            if c.obtenerId() == id:
                return c
        return None

    @classmethod
    def buscarVino(cls, id):
        for v in cls.vinos:
            if v.obtenerId() == id:
                return v
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.__archivoDeDatos, 'r') as archivo:
            return json.load(archivo)

    @classmethod
    def __convertirJsonAListas(cls, datos):
        cls.bodegas = [Bodega(b["id"], b["nombre"]) for b in datos["bodegas"]]
        cls.cepas = [Cepa(c["id"], c["nombre"]) for c in datos["cepas"]]
        cls.vinos = [Vino(v["id"], v["nombre"], v["bodega"], v["cepas"], v["partidas"]) for v in datos["vinos"]]





# import json
# from modelos.bodega import Bodega
# from modelos.cepa import Cepa
# from modelos.vino import Vino

# class Vinoteca:
#     __archivoDeDatos = "vinoteca.json"
#     __bodegas = []
#     __cepas = []
#     __vinos = []

#     @classmethod
#     def inicializar(cls):
#         datos = cls.__parsearArchivoDeDatos()
        
#         # Crear objetos y añadirlos a las listas de bodegas, cepas, y vinos
#         cls.__bodegas = []
#         for bodega_data in datos["bodegas"]:
#             cls.__bodegas.append(Bodega(bodega_data["id"], bodega_data["nombre"]))

#         cls.__cepas = []
#         for cepa_data in datos["cepas"]:
#             cls.__cepas.append(Cepa(cepa_data["id"], cepa_data["nombre"]))

#         cls.__vinos = []
#         for vino_data in datos["vinos"]:
#             cls.__vinos.append(Vino(
#                 vino_data["id"], vino_data["nombre"], vino_data["bodega"],
#                 vino_data["cepas"], vino_data["partidas"]
#             ))

#     @classmethod
#     def obtenerBodegas(cls):
#         return cls.__bodegas

#     @classmethod
#     def obtenerCepas(cls):
#         return cls.__cepas

#     @classmethod
#     def obtenerVinos(cls):
#         return cls.__vinos

#     @classmethod
#     def buscarBodega(cls, id):
#         for bodega in cls.__bodegas:
#             if bodega.obtenerId() == id:
#                 return bodega
#         return None

#     @classmethod
#     def buscarCepa(cls, id):
#         for cepa in cls.__cepas:
#             if cepa.obtenerId() == id:
#                 return cepa
#         return None

#     @classmethod
#     def buscarVino(cls, id):
#         for vino in cls.__vinos:
#             if vino.obtenerId() == id:
#                 return vino
#         return None

#     @classmethod
#     def __parsearArchivoDeDatos(cls):
#         with open(cls.__archivoDeDatos, 'r') as archivo:
#             return json.load(archivo)
