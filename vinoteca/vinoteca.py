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

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(cls.__bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
            elif orden == "vinos":
                return sorted(cls.__bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return cls.__bodegas
    
    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        if isinstance(orden, str) and orden == "nombre":
            return sorted(cls.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        return cls.__cepas
    

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos_f = cls.__vinos
        if isinstance(anio, int):
            vinos_f = [vino for vino in cls.__vinos if anio in vino._partidas]
        if isinstance(orden, str):
            if orden == "nombre":
                return sorted(vinos_f, key=lambda v: v.obtenerNombre(), reverse=reverso)
            elif orden == "bodega":
                return sorted(vinos_f, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
            elif orden == "cepas":
                return sorted(vinos_f, key=lambda v: len(v.obtenerCepas()), reverse=reverso) 
        return vinos_f

  
#para mostrar los datos de bodega,cepa y vino

    def mostrarDatos(cls, id: str):
        cepa = cls.buscarCepa(id)
        vino = cls.buscarVino(id)
        bodega = cls.buscarBodega(id)
        if cepa:
            print("Datos de la Cepa:")
            print(f"ID: {cepa.obtenerId()}")
            print(f"Nombre: {cepa.obtenerNombre()}")
            print("Vinos:")
            for v in cepa.obtenerVinos():
                print(f"  - {v.obtenerNombre()} (Bodega: {v.obtenerBodega().obtenerNombre()})")
            return
        
        if vino:
            print("Datos del Vino:")
            print(f"ID: {vino.obtenerId()}")
            print(f"Nombre: {vino.obtenerNombre()}")
            print("Cepas:")
            for c in vino.obtenerCepas():
                print(f"  - {c.obtenerNombre()}")
            print(f"Bodega: {vino.obtenerBodega().obtenerNombre()}")
            print(f"Partidas: {vino.obtenerPartidas()}")
            return
        
        if bodega:
            print("Datos de la Bodega:")
            print(f"ID: {bodega.obtenerId()}")
            print(f"Nombre: {bodega.obtenerNombre()}")
            print("Vinos:")
            for v in bodega.obtenerVinos():
                print(f"  - {v.obtenerNombre()}")
            return
        
        print(f"No se encontró una cepa, vino o bodega con el id '{id}'.")
 
   
#BUSCAR BODEGA, CEPA Y VINO#
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
        rutaArchivo = os.path.join(os.path.dirname(__file__), cls.__archivoDeDatos) #Obtiene el directorio del archivo actual 
        #y carga la información en un diccionario
        with open(rutaArchivo, 'r' , encoding='utf-8') as archivo: #Abre el archivo en modo lectura
            return json.load(archivo) #retorna el diccionario creado

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


    
    
