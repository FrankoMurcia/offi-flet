class TipoCostoGasto:
        
    tipo_costo_gasto = {
        1: "Gasto de Venta sin Donación",
        2: "Gasto de Administración, sin Donación",
        3: "Gastos Financieros sin Donación",
        4: "Costo Artículos Producidos/Comprados Importaciones/Internaciones",
        5: "Costo Artículos Producidos/Comprados Internos",
        6: "Costo Indirectos de Fabricación",
        7: "Mano de Obra",
        8: "Operaciones Informadas en más de 1 año",
        9: "Excepciones (Instituciones públicas, no inscritas a IVA, operaciones no deducibles para renta, entre otros.)"
    }

    @staticmethod
    def obtener_todos():
        return list(TipoCostoGasto.tipo_costo_gasto.items())

    @staticmethod
    def obtener_por_id(id_clase):
        return TipoCostoGasto.tipo_costo_gasto.get(id_clase)

    @staticmethod
    def existe(id_clase):
        return id_clase in TipoCostoGasto.tipo_costo_gasto