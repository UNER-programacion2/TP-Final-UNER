# librerias
import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:

    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    def inicializar():
        datos = Vinoteca.__parsearArchivoDeDatos()
        Vinoteca.__convertirJsonAListas(datos)

    def obtenerBodegas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar    
            elif orden == "vinos":
                pass  # completar
        pass  # completar



    def obtenerCepas(orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
        pass  # completar

    def obtenerVinos(anio=None, orden=None, reverso=False):
        if isinstance(anio, int):
            pass  # completar
        if isinstance(orden, str):
            if orden == "nombre":
                pass  # completar
            elif orden == "bodega":
                pass  # completar
            elif orden == "cepas":
                pass  # completar
        pass  # completar

    def buscarBodega(id: int) -> Bodega: 
        for bodega in Vinoteca.__bodegas:
            if bodega.ObtenerId() == id:
                return bodega          
        return None    
          

    def buscarCepa(id: str) -> Cepa:  
        for cepa in Vinoteca.__cepas:
            if cepa.obtenerId() == id:
                return cepa
        return None
      

    def buscarVino(id) -> Vino:
        for vino in Vinoteca.__vinos:
            if vino.obtenerId() == id:
                return vino
        return None
    
    
#LOAD: crea y retorna un diccionario nuevo de Python con 
# los pares clave-valor del archivo JSON.
    def __parsearArchivoDeDatos():
        with open(Vinoteca. __archivoDeDatos, 'r') as archivo: #Abrir json en modo lectura
            arch_json = json.load(archivo) #leer archivo json y crea diccionario
        return arch_json

    def __convertirJsonAListas(lista):
        for bodega in lista["bodegas"]:
            Vinoteca.__bodegas.append(Bodega(bodega[id]))

        for cepas in lista["cepas"]:
            Vinoteca.__cepas.append(Cepa(cepas[id]))

        for vinos in lista["vinos"]:
            Vinoteca.__vinos.append(Vino(vinos[id]))

