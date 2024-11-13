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
