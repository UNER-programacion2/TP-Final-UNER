

# class Database:
#     def __init__(self, rutaDeArchivo):
#         self.rutaDeArchivo = rutaDeArchivo
#         self.data = self.cargarData()

#     #FUNCION NUEVA PARA LA CARGA DE DATOS DE LOS JSON
#     def cargarDatos(self):
#         if os.path.exists(self.rutaDeArchivo):
#             try:
#                 with open(self.rutaDeArchivo, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#                     # Convertir campos numéricos de string a int o float si es necesario
#                     for vehiculo in data:
#                         vehiculo['anio'] = int(vehiculo['anio']) if 'anio' in vehiculo and isinstance(vehiculo['anio'], (int, str)) else None
#                         vehiculo['precioVenta'] = float(vehiculo['precioVenta']) if 'precioVenta' in vehiculo and isinstance(vehiculo['precioVenta'], (float, int, str)) else None
#                     return data
#             except (json.JSONDecodeError, ValueError) as e:
#                 print(f"Error al cargar datos JSON: {e}")
#                 return []  # Archivo está vacío o no es un JSON válido
#         else:
#             return []
        
#     def guardarData(self):
#         with open(self.rutaDeArchivo, 'w', encoding='utf-8') as file:
#             json.dump(self.data, file, indent=4)


#@classmethod
#######################################
#    @classmethod
#     def obtenerCepaJSON(cls, id):
#         cepa = cls.buscarCepa(id)
#         if cepa:
#             return {
#                 "id": cepa.obtenerId(),
#                 "nombre": cepa.obtenerNombre(),
#                 "vinos": [f"{vino.obtenerNombre()} ({vino.obtenerBodega().obtenerNombre()})" for vino in cepa.obtenerVinos()]
#             }
#         return {"error": "Cepa no encontrada"}

#     @classmethod
#     def obtenerVinoJSON(cls, id):
#         vino = cls.buscarVino(id)
#         if vino:
#             return {
#                 "id": vino.obtenerId(),
#                 "nombre": vino.obtenerNombre(),
#                 "bodega": vino.obtenerBodega().obtenerNombre(),
#                 "cepas": [cepa.obtenerNombre() for cepa in vino.obtenerCepas()],
#                 "partidas": vino.obtenerPartidas()
#             }
#         return {"error": "Vino no encontrado"}

#     @classmethod
#     def obtenerVinosJSON(cls, anio=None, orden=None, reverso=False):
#         vinos = cls.obtenerVinos(anio, orden, reverso)
#         vinos_json = []
#         for vino in vinos:
#             vinos_json.append({
#                 "id": vino.obtenerId(),
#                 "nombre": vino.obtenerNombre(),
#                 "bodega": vino.obtenerBodega().obtenerNombre(),
#                 "cepas": [cepa.obtenerNombre() for cepa in vino.obtenerCepas()],
#                 "partidas": vino.obtenerPartidas()
#             })
#         return vinos_json
######################################################################


# librerias
import encodings
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

    # Obtaining Entities
    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if orden == "nombre":
            return sorted(cls.__bodegas, key=lambda b: b.obtenerNombre(), reverse=reverso)
        elif orden == "vinos":
            return sorted(cls.__bodegas, key=lambda b: len(b.obtenerVinos()), reverse=reverso)
        return cls.__bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        if orden == "nombre":
            return sorted(cls.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        return cls.__cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos_f = cls.__vinos
        if isinstance(anio, int):
            vinos_f = [vino for vino in cls.__vinos if anio in vino._partidas]
        if orden == "nombre":
            return sorted(vinos_f, key=lambda v: v.obtenerNombre(), reverse=reverso)
        elif orden == "bodega":
            return sorted(vinos_f, key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
        elif orden == "cepas":
            return sorted(vinos_f, key=lambda v: len(v.obtenerCepas()), reverse=reverso)
        return vinos_f

    # Display Data
    @classmethod
    def mostrarDatos(cls, id: str):
        cepa = cls.buscarCepa(id)
        vino = cls.buscarVino(id)
        bodega = cls.buscarBodega(id)
        if cepa:
            cls.__mostrarDatosCepa(cepa)
        elif vino:
            cls.__mostrarDatosVino(vino)
        elif bodega:
            cls.__mostrarDatosBodega(bodega)
        else:
            print(f"No se encontró una cepa, vino o bodega con el id '{id}'.")

    @staticmethod
    def __mostrarDatosCepa(cepa):
        print("Datos de la Cepa:")
        print(f"ID: {cepa.obtenerId()}")
        print(f"Nombre: {cepa.obtenerNombre()}")
        print("Vinos:")
        for v in cepa.obtenerVinos():
            print(f"  - {v.obtenerNombre()} (Bodega: {v.obtenerBodega().obtenerNombre()})")

    @staticmethod
    def __mostrarDatosVino(vino):
        print("Datos del Vino:")
        print(f"ID: {vino.obtenerId()}")
        print(f"Nombre: {vino.obtenerNombre()}")
        print("Cepas:")
        for c in vino.obtenerCepas():
            print(f"  - {c.obtenerNombre()}")
        print(f"Bodega: {vino.obtenerBodega().obtenerNombre()}")
        print(f"Partidas: {vino.obtenerPartidas()}")

    @staticmethod
    def __mostrarDatosBodega(bodega):
        print("Datos de la Bodega:")
        print(f"ID: {bodega.obtenerId()}")
        print(f"Nombre: {bodega.obtenerNombre()}")
        print("Vinos:")
        for v in bodega.obtenerVinos():
            print(f"  - {v.obtenerNombre()}")

    # File Parsing
    @classmethod
    def __parsearArchivoDeDatos(cls):
        ruta_archivo = os.path.join(os.path.dirname(__file__), cls.__archivoDeDatos)
        try:
            with open(ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error leyendo el archivo de datos: {e}")
            return {}

    @classmethod
    def __convertirJsonAListas(cls, lista):
        cls.__bodegas = []
        cls.__cepas = []
        cls.__vinos = []

        for bodega in lista.get("bodegas", []):
            cls.__bodegas.append(Bodega(bodega['id'], bodega['nombre']))
        for cepa in lista.get("cepas", []):
            cls.__cepas.append(Cepa(cepa['id'], cepa['nombre']))
        for vino in lista.get("vinos", []):
            cls.__vinos.append(Vino(vino['id'], vino['nombre'], vino['bodega'], vino['cepas'], vino['partidas']))

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)
