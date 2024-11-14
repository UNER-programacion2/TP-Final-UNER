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

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

#vickyyyy############################################################################################################
    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(cls.__bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                return sorted(cls.__bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return cls.__bodegas

    @classmethod
    def obtenerCepas(cls, id:str, orden=None, reverso=False):
        cepa = cls.buscarCepa(id)
        cepa = cls.buscarCepa(id)
        if cepa:
            print(json.dumps({
                "id": cepa.obtenerId(),
                "nombre": cepa.obtenerNombre(),
                "vinos": [f"{vino.obtenerNombre()} ({vino.obtenerBodega().obtenerNombre()})" for vino in cepa.obtenerVinos()]
            }))
        else:
            print(f"Cepa con id {id} no encontrada.")
            return []
           
        if isinstance(orden, str) and orden == "nombre":
            return sorted(cls.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        
        return cls.__cepas

        # if isinstance(orden, str):
        #     if orden == "nombre":
        #         return sorted(cls.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        # return cls.__cepas
    
        # if cepa: esto para mostrar
        #     print(json.dumps({
        #         "id": cepa.obtenerId(),
        #         "nombre": cepa.obtenerNombre(),
        #         "vinos": [f"{vino.obtenerNombre()} ({vino.obtenerBodega().obtenerNombre()})" for vino in cepa.obtenerVinos()]
        #         }, ensure_ascii=False))
        # else:
        #     print(f"Cepa con id {id} no encontrada.")

        
        

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos_filtrados = cls.__vinos
        if isinstance(anio, int):
            vinos_filtrados = [vino for vino in cls.__vinos if anio in vino.partidas]
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(vinos_filtrados, key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                return sorted(vinos_filtrados, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                return sorted(vinos_filtrados, key=lambda v: len(v.obtenerCepas()), reverse=reverso)
            
        return vinos_filtrados

#funciona-original#################################################################################################

    @classmethod 
    def buscarBodega(cls, id: str) : 
        for bodega in cls.__bodegas: 
            if bodega.obtenerId() == id: 
                return bodega 
        return None 
        
    @classmethod 
    def buscarCepa(cls, id: str) : 
        for cepa in cls.__cepas: 
            if cepa.obtenerId() == id: 
                return cepa 
        return None 
        
    @classmethod 
    def buscarVino(cls, id: str) : 
        for vino in cls.__vinos: 
            if vino.obtenerId() == id: 
                return vino 
        return None
    
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
            if 'id' in bodega and 'nombre' in bodega:
                cls.__bodegas.append(Bodega(bodega['id'], bodega['nombre']))
            
        for cepa in lista["cepas"]:
            if 'id' in cepa and 'nombre' in cepa:
                cls.__cepas.append(Cepa(cepa['id'], cepa['nombre']))

        for vino in lista["vinos"]:
            if 'id' in vino and 'nombre' in vino and 'bodega' in vino and 'cepas' in vino and 'partidas' in vino:
                cls.__vinos.append(Vino(vino['id'], vino['nombre'], vino['bodega'], vino['cepas'], vino['partidas']))





#lo que estaba haciendo gabi
    
    # @classmethod
    # def cargar_datos(cls):
    #     try:
    #         whit open('vinoteca.json', 'r', endcoding-'utf-8') as file:
    #             cls.__archivoDeDatos = file.read()
    #             print(('datos cargados correctamente'))





########################################################################################
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

