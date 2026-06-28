from database.conexion import conectar

class TipoOperacion:
        
    tipo_operacion = {
        1: "Gravada",
        2: "No Gravada o exenta",
        3: "Excluido o no constituye renta",
        4: "Mixta (Se refiere cuando en un mismo documento se encuentre una operacion gravada y exenta)", 
        5: "Operaciones informadas en más de un anexo",
        6: "Excepciones (Instituciones públicas, no inscritas a IVA, operaciones no deducibles para renta, entre otros)", 
    }

    @staticmethod
    def obtener_todos():
        return list(TipoOperacion.tipo_operacion.items())

    @staticmethod
    def obtener_por_id(id_operacion):
        return TipoOperacion.tipo_operacion.get(id_operacion)

    @staticmethod
    def existe(id_clase):
        return id_clase in TipoOperacion.tipo_operacion
