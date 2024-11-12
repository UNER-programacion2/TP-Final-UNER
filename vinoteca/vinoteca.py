# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    __archivoDeDatos = './vinoteca.json'
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

###################################################################################
#modificar esto################################
    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if orden is not None:
            return sorted(cls.__bodegas, key=lambda b: getattr(b, orden), reverse=reverso)
        return cls.__bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        if orden is not None:
            return sorted(cls.__cepas, key=lambda c: getattr(c, orden), reverse=reverso)
        return cls.__cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos = cls.__vinos
        if anio is not None:
            vinos = [vino for vino in vinos if vino.anio == anio]
        if orden is not None:
            vinos = sorted(vinos, key=lambda v: getattr(v, orden), reverse=reverso)
        return vinos
########################################################################################
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

    # @classmethod
    # def __parsearArchivoDeDatos(cls):
    #     with open(cls.__archivoDeDatos, 'r') as archivo:
    #         return json.load(archivo)
    @classmethod
    def __parsearArchivoDeDatos(cls):
        ruta_archivo = os.path.join(os.path.dirname(__file__), cls.__archivoDeDatos)
        with open(ruta_archivo, 'r') as archivo:
            return json.load(archivo)

    # @classmethod
    # def __convertirJsonAListas(cls, lista):
    #     for bodega in lista["bodegas"]:
    #         Vinoteca.__bodegas.append(Bodega(bodega[id]))

    #     for cepas in lista["cepas"]:
    #         Vinoteca.__cepas.append(Cepa(cepas[id]))

    #     for vinos in lista["vinos"]:
    #         Vinoteca.__vinos.append(Vino(vinos[id]))
    @classmethod
    def __convertirJsonAListas(cls, lista):
        cls.__bodegas = []   
        cls.__cepas = []
        cls.__vinos = []

        for bodega in lista["bodegas"]:
            if 'id' in bodega:
                cls.__bodegas.append(Bodega(bodega['id']))
            else:
                print("Error: 'id' key is missing in bodega:", bodega)
        
     
        for cepas in lista["cepas"]:
            if 'id' in cepas:
                cls.__cepas.append(Cepa(cepas['id']))
            else:
                print("Error: 'id' key is missing in bodega:", cepas)

        for vinos in lista["vinos"]:
            if 'id' in vinos:
                cls.__vinos.append(Vino(vinos['id']))
            else:
                print("Error: 'id' key is missing in bodega:", vinos)