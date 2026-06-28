class ClaseDocumento:

    CLASE_DOCUMENTO = {
        1: "Impreso por imprenta o tiquetes",
        2: "Formulario único",
        3: "Otros",
        4: "Documento Tributario Electrónico (DTE)"
    }

    @classmethod
    def obtener_todos(cls):
        return cls.CLASE_DOCUMENTO.items()

    @staticmethod
    def obtener_por_id(cls, id__):
        return cls.CLASE_DOCUMENTO.get(id__)

    @staticmethod
    def existe(id_clase):
        return id_clase in ClaseDocumento.CLASE_DOCUMENTO