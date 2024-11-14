# librerias
import os
import json

from abc import ABC, abstractmethod


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
    
