import flet as ft


class ComprasControls:

    def __init__(self):

        # ========= FECHA =========

        self.txt_fecha: ft.TextField | None = None

        # ========= DOCUMENTO =========

        self.txt_codigo_generacion: ft.TextField | None = None
        self.txt_numero_control: ft.TextField | None = None
        self.txt_sello_recepcion: ft.TextField | None = None

        # ========= MONTOS =========

        self.txt_subtotal: ft.TextField | None = None
        self.txt_iva: ft.TextField | None = None
        self.txt_iva_percibido: ft.TextField | None = None
        self.txt_total: ft.TextField | None = None

        #========== COMPRAS EXENTAS============
        self.txt_compras_internas_exentas: ft.TextField | None = None
        self.txt_internaciones_exentas_no_sujetas: ft.TextField | None = None
        self.txt_importaciones_exentas_no_sujetas: ft.TextField | None = None

        #========== COMPRAS GRAVADAS =======
        self.txt_internaciones_gravadas_bienes: ft.TextField | None = None
        self.txt_importaciones_gravadas_bienes: ft.TextField | None = None
        self.txt_importaciones_gravadas_servicios: ft.TextField | None = None

        #========== IMPUESTOS =========
        
        # ========= DOCUMENTOS =========

        self.dd_tipo_documento: ft.Dropdown | None = None
        self.dd_emisor: ft.Dropdown | None = None
        self.dd_clase_documento: ft.Dropdown | None = None

        # ========= PROVEEDOR =========

        self.txt_buscar_nit: ft.TextField | None = None
        self.txt_nombre_emisor: ft.TextField | None = None

        # ========= CLASIFICACIÓN =========

        self.txt_clasificacion: ft.Text | None = None
        self.txt_sector: ft.Text | None = None
        self.txt_tipo_gasto: ft.Text | None = None
        self.txt_tipo_operacion: ft.Text | None = None

        # ========= BOTONES =========

        self.btn_nuevo_proveedor: ft.Control | None = None