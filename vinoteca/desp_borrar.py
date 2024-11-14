    # @staticmethod
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     vinos = list(Vinoteca.__vinos)
        
    #     if isinstance(anio, int):
    #         vinos = [vino for vino in vinos if any(partida.anio == anio for partida in vino.partidas)]
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             vinos.sort(key=lambda v: v.nombre, reverse=reverso)
    #         elif orden == "bodega":
    #             vinos.sort(key=lambda v: v.bodega.nombre, reverse=reverso)
    #         elif orden == "cepas":
    #             vinos.sort(key=lambda v: len(v.cepas), reverse=reverso)
        
    #     return vinos
    # @staticmethod
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     vinos = list(Vinoteca.__vinos)
        
    #     if isinstance(anio, int):
    #         vinos = [vino for vino in vinos if any(partida.anio == anio for partida in vino.partidas)]
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             vinos.sort(key=lambda v: v.nombre, reverse=reverso)
    #         elif orden == "bodega":
    #             vinos.sort(key=lambda v: v.bodega.nombre, reverse=reverso)
    #         elif orden == "cepas":
    #             vinos.sort(key=lambda v: len(v.cepas), reverse=reverso)
        
    #     return vinos
    
    # @staticmethod
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     # Copiamos la lista de vinos para trabajar sobre ella sin modificar la original
    #     vinos = list(Vinoteca.__vinos)
        
    #     # Filtrado por año de partida, si se proporciona
    #     if isinstance(anio, int):
    #         vinos = [vino for vino in vinos if anio in vino.obtenerPartidas()]

    #     # Ordenar la lista según el parámetro 'orden'
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             vinos.sort(key=lambda v: v.obtenerNombre(), reverse=reverso)
    #         elif orden == "bodega":
    #             vinos.sort(key=lambda v: v.obtenerBodega().obtenerNombre(), reverse=reverso)
    #         elif orden == "cepas":
    #             vinos.sort(key=lambda v: len(v.obtenerCepas()), reverse=reverso)

    #     return vinos   

    # @classmethod
    # def obtenerBodegas(cls, orden=None, reverso=False):
    #     if orden is not None:
    #         return sorted(cls.__bodegas, key=lambda b: getattr(b, orden), reverse=reverso)
    #     return cls.__bodegas

    # @classmethod
    # def obtenerCepas(cls, orden=None, reverso=False):
    #     if orden is not None:
    #         return sorted(cls.__cepas, key=lambda c: getattr(c, orden), reverse=reverso)
    #     return cls.__cepas

    # @classmethod
    # def obtenerVinos(cls, anio=None, orden=None, reverso=False):
    #     vinos = cls.__vinos
    #     if anio is not None:
    #         vinos = [vino for vino in vinos if vino.anio == anio]
    #     if orden is not None:
    #         vinos = sorted(vinos, key=lambda v: getattr(v, orden), reverse=reverso)
    #     return vinos
    

############################################################################

  # @staticmethod
    # def obtenerBodegas(orden=None, reverso=False):
    #     bodegas = list(Vinoteca.__bodegas)
        
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             bodegas.sort(key=lambda b: b.nombre, reverse=reverso)
    #         elif orden == "vinos":
    #             bodegas.sort(key=lambda b: len(b.vinos), reverse=reverso)

    #     return bodegas


    # @staticmethod
    # def obtenerCepas(orden=None, reverso=False):
    #     cepas = list(Vinoteca.__cepas)
        
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             cepas.sort(key=lambda c: c.nombre, reverse=reverso)
    #     return cepas
    

    # @staticmethod
    # def obtenerVinos(anio=None, orden=None, reverso=False):
    #     vinos = list(Vinoteca.__vinos)
        
    #     if isinstance(anio, int):
    #         vinos = [vino for vino in vinos if any(partida.anio == anio for partida in vino.partidas)]
        
    #     if isinstance(orden, str):
    #         if orden == "nombre":
    #             vinos.sort(key=lambda v: v.nombre, reverse=reverso)
    #         elif orden == "bodega":
    #             vinos.sort(key=lambda v: v.bodega.nombre, reverse=reverso)
    #         elif orden == "cepas":
    #             vinos.sort(key=lambda v: len(v.cepas), reverse=reverso)
    #     return vinos


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



########################################################################################################################################
    # @classmethod
    # def obtenerCepas(cls, id:str, orden=None, reverso=False):
    #     cepa = cls.buscarCepa(id)
    #     cepa = cls.buscarCepa(id)
    #     if cepa:
    #         print(json.dumps({
    #             "id": cepa.obtenerId(),
    #             "nombre": cepa.obtenerNombre(),
    #             "vinos": [f"{vino.obtenerNombre()} ({vino.obtenerBodega().obtenerNombre()})" for vino in cepa.obtenerVinos()]
    #         }))
    #     else:
    #         print(f"Cepa con id {id} no encontrada.")
    #         return []
           
    #     if isinstance(orden, str) and orden == "nombre":
    #         return sorted(cls.__cepas, key=lambda c: c.obtenerNombre(), reverse=reverso)
        
    #     return cls.__cepas

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