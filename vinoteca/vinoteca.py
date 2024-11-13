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


# Para las consultas obtenerBodegas, obtenerCepas y obtenerVinos, si 
# se recibe: 
# i. Los  parámetros  opcionales  orden  <>  None  y  reverso  =  True, 
# devolver  una  copia  de  la  colección  correspondiente,  ordenando 
# los objetos de la misma por el atributo indicado en orden inverso. 
# ii. Ninguno de los parámetros opcionales, devolver una referencia a 
# la colección correspondiente sin alterar su orden
# Para la consulta obtenerVinos, si se recibe el parámetro anio <> None, 
# antes de ordenar la colección a retornar, esta debe filtrarse manteniendo 
# únicamente aquellos vinos cuyas partidas contengan el año en cuestión.

###################################################################################
####SANTI DESDE ACA ABAJO
    # @staticmethod
    # def obtenerBodegas(orden=None, reverso=False):
    #     bodegas = list(Vinoteca.__bodegas)  # Copia de la lista original
        
    #     if orden == "nombre":
    #         bodegas.sort(key=lambda b: b.obtenerNombre(), reverse=reverso)
    #     elif orden == "vinos":
    #         bodegas.sort(key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        
    #     return bodegas

    # @staticmethod
    # def obtenerCepas(orden=None, reverso=False):
    #     cepas = list(Vinoteca.__cepas)  # Copia de la lista original
        
    #     if orden == "nombre":
    #         cepas.sort(key=lambda c: c.obtenerNombre(), reverse=reverso)
        
    #     return cepas

    # @staticmethod
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     vinos = list(Vinoteca.__vinos)  # Copia de la lista original
        
    #     if isinstance(anio, int):
    #         vinos = [vino for vino in vinos if anio in vino.obtenerPartidas()]

    #     if orden == "nombre":
    #         vinos.sort(key=lambda v: v.obtenerNombre(), reverse=reverso)
    #     elif orden == "bodega":
    #         vinos.sort(key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
    #     elif orden == "cepas":
    #         vinos.sort(key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        
    #     return vinos
    
##############buscar
#    @staticmethod
#    def buscarBodega(id: str) -> Bodega:
#        for bodega in Vinoteca.__bodegas:
#            if bodega.obtenerId() == id:
#                return bodega
#        return None
#
#    @staticmethod
#    def buscarCepa(id: str) -> Cepa:
#        for cepa in Vinoteca.__cepas:
#            if cepa.obtenerId() == id:
#                return cepa
#        return None
#
#    @staticmethod
#    def buscarVino(id: str) -> Vino:
#        for vino in Vinoteca.__vinos:
#            if vino.obtenerId() == id:
#                return vino
#        return None



########################################################################################
#original 
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
    

##############FUNCIONA####################
    @classmethod
    def __parsearArchivoDeDatos(cls):
        ruta_archivo = os.path.join(os.path.dirname(__file__), cls.__archivoDeDatos) #Obtiene el directorio del archivo actual
        with open(ruta_archivo, 'r') as archivo: #Abre el archivo en modo lectura
            return json.load(archivo)

    @classmethod
    def __convertirJsonAListas(cls, lista):
        cls.__bodegas = []   
        cls.__cepas = []
        cls.__vinos = []

        for bodega in lista["bodegas"]:
            if 'id' in bodega:
                cls.__bodegas.append(Bodega(bodega['id']))
            # else:
            #     print("Error: 'id' key is missing in bodega:", bodega)
        
        for cepa in lista["cepas"]:
            if 'id' in cepa and 'nombre' in cepa:
                cls.__cepas.append(Cepa(cepa['id'], cepa['nombre']))
            # else:
            #     print("Error: 'id' or 'nombre' key is missing in cepa:", cepa)

        for vinos in lista["vinos"]:
            if 'id'  and 'nombre'  and 'bodega'  and 'cepas'  and 'partidos' in vinos:
                cls.__vinos.append(Vino(vinos['id'], vinos['nombre'], vinos['bodega'], vinos['cepas'], vinos['partidas']))
            # else:
            #     print("Error: 'id' key is missing in bodega:", vinos)

