class TipoDocumento:

    tipo_documento = {
        1: "Factura Consumidor Final",
        2: "No Asignado",
        3: "Comprobante de Crédito Fiscal",
        4: "Nota de Remisión",
        5: "Nota de Débito",
        6: "Nota de Crédito",
        7: "Comprobante de Retención",
        8: "Comprobante de Liquidación",
        9: "Documento Contable de Liquidación",
        10: "No Asignado",
        11: "Factura de Exportación",
        12: "No Asignado",
        13: "No Asignado",
        14: "Factura de Sujeto Excluido",
        15: "Comprobante de Donación",
    }
    
    @staticmethod
    def obtener_todos():
        return list(TipoDocumento.tipo_documento.items())

    @staticmethod
    def obtener_por_id(id_operacion):
        return TipoDocumento.tipo_documento.get(id_operacion)

    @staticmethod
    def existe(id_clase):
        return id_clase in TipoDocumento.tipo_documento