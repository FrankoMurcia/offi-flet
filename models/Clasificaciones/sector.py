class Sector:
        
    secor = {
        1: "Industria",
        2: "Comercio",
        3: "Agropecuaria",
        4: "Servicios, Profesiones, Artes y Oficios",
        5: "Operaciones informadas en más de 1 año",
        6: "Excepciones (Instituciones públicas, no inscritas a IVA, operaciones no deducibles para renta, entre otros)",
    }

    @staticmethod
    def obtener_todos():
        return list(Sector.secor.items())

    @staticmethod
    def obtener_por_id(id_clase):
        return Sector.secor.get(id_clase)

    @staticmethod
    def existe(id_clase):
        return id_clase in Sector.secor