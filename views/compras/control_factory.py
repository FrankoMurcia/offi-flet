import flet as ft
from views.compras.controls import ComprasControls

from views.compras.formatters import formatear_fecha, formatear_codigo_generacion, formatear_numero_control, formatear_sello_recepcion, formatear_subtotal
from views.compras.calculations import calcular_totales
from views.compras.validaciones import validar_factura_existente
# from views.compras.dialogs import mostrar_error
from views.compras.proveedor_search import filtrar_emisor
from views.compras.validaciones import mostrar_error

def crear_controles (page, state, sugerencias):
    
    controls = ComprasControls()

    controls.txt_fecha = ft.TextField(
        label="Fecha",
        width=200,
        keyboard_type= ft.KeyboardType.NUMBER,
        on_change= lambda e:
        formatear_fecha(
            e,
            controls.txt_fecha,
            page
        )
    )

    controls.txt_codigo_generacion = ft.TextField(
        label="Código Generación",
        width=300,
        prefix_icon=ft.Icons.QR_CODE,
        on_change= lambda e: formatear_codigo_generacion(e, controls.txt_codigo_generacion, page),
        on_blur = lambda e: validar_factura_existente(controls, lambda titulo, mensaje: mostrar_error(page, titulo, mensaje), page)
    )

    controls.txt_numero_control = ft.TextField(
        label="Número Control",
        width=300,
        prefix_icon=ft.Icons.TAG,
        on_change=lambda e: formatear_numero_control(e, controls.txt_numero_control, page)
    )

    controls.txt_sello_recepcion = ft.TextField(
        label="Sello Recepción",
        width=300,
        prefix_icon=ft.Icons.VERIFIED,
        on_change= lambda e: formatear_sello_recepcion(e,controls.txt_sello_recepcion, page)
    )


    controls.txt_subtotal = ft.TextField(
        label="Subtotal",
        width=220,
        prefix_icon=ft.Icons.ATTACH_MONEY,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change= lambda e: calcular_totales(page, controls),
        on_blur= lambda e: formatear_subtotal(e, controls.txt_subtotal, page)
    )

    controls.txt_iva = ft.TextField(
        label="IVA",
        width=150,
        prefix_icon=ft.Icons.PERCENT,
        read_only= True
    )

    controls.txt_total = ft.TextField(
        label="Total",
        width=220,
        prefix_icon=ft.Icons.PAID,
        read_only=True,
        text_style=ft.TextStyle(
            size=18,
            weight=ft.FontWeight.BOLD
        )
    )

    controls.txt_iva_percibido = ft.TextField(
        label="IVA Percibido",
        width=180,
        prefix_icon=ft.Icons.PERCENT,
        read_only=True
    )

    controls.txt_compras_internas_exentas = ft.TextField(
        label="Compras Internas Exentas",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.txt_internaciones_exentas_no_sujetas = ft.TextField(
        label="Internaciones Exentas y/o No Sujetas",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.txt_importaciones_exentas_no_sujetas = ft.TextField(
        label="Importaciones Exentas y/o No Sujetas",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.txt_internaciones_gravadas_bienes = ft.TextField(
        label="Internaciones Gravadas de Bienes",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.txt_importaciones_gravadas_bienes = ft.TextField(
        label="Importaciones Gravadas de Bienes",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.txt_importaciones_gravadas_servicios = ft.TextField(
        label="Importaciones Gravadas de Servicios",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    controls.dd_tipo_documento = ft.Dropdown(
        label="Tipo Documento",
        width=300
    )

    controls.dd_emisor = ft.Dropdown(
        label="Emisor",
        width=400,
        visible= False
    )

    controls.dd_clase_documento = ft.Dropdown(
        label="Clase Documento",
        width=300
    )

    controls.txt_clasificacion = ft.Text(
        "Sin seleccionar",
        weight=ft.FontWeight.BOLD
    )

    controls.txt_sector = ft.Text(
        "Sin seleccionar",
        weight=ft.FontWeight.BOLD
    )

    controls.txt_tipo_gasto = ft.Text(
        "Sin seleccionar",
        weight=ft.FontWeight.BOLD
    )

    controls.txt_tipo_operacion = ft.Text(
        "Sin seleccionar",
        weight=ft.FontWeight.BOLD
    )

    controls.txt_buscar_nit = ft.TextField(
        label="Buscar Proveedor (NIT o NRC)",
        width=250,
        prefix_icon=ft.Icons.SEARCH,
        on_change= lambda e: filtrar_emisor(e, state, controls, sugerencias, page)
    )
    controls.txt_nombre_emisor = ft.TextField(
        label="Nombre Emisor",
        width=400,
        read_only=True,
        prefix_icon=ft.Icons.BUSINESS
    )

    return controls