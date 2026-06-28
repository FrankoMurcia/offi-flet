class ComprasState:

    def __init__(self):

        # ========= PERÍODO =========

        self.periodo_actual = None

        # ========= EDICIÓN =========

        self.id_edicion = None

        # ========= CLASIFICACIÓN =========

        self.clasificacion_id = None
        self.sector_id = None
        self.tipo_gasto_id = None
        self.tipo_operacion_id = None

        # ========= EMISORES =========

        self.emisores_cache = []
        self.resultados_actuales = []
        self.indice_seleccionado = -1

