class Clasificacion:
        
    clasificacion = {
        1: "Costo",
        2: "Gasto",
        3: "Operaciones informadas en más de 1 año",
        4: "Excepciones (Instituciones publicas, no inscritas a IVA, operacionesno deducibles para renta, entre otros)",
    }

    @staticmethod
    def obtener_todos():
        return list(Clasificacion.clasificacion.items())

    @staticmethod
    def obtener_por_id(id_clase):
        return Clasificacion.clasificacion.get(id_clase)

    @staticmethod
    def existe(id_clase):
        return id_clase in Clasificacion.clasificacion 