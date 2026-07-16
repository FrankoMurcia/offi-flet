import flet as ft
# Exportaciones
from views.compras.export_controller import descargar_csv, descargar_excel
#Nuevos
from views.compras.modal_periodo import mostrar_modal_periodo, crear_nombre_periodo
from views.compras.tabla import crear_tabla_compras
from views.compras.dialogs import mostrar_error, mostrar_mensaje, mostrar_confirmacion
from views.compras.dropdowns import cargar_dropdowns, seleccionar_periodo, crear_dropdown_periodos
from views.compras.modal_controller import abrir_modal
from views.compras.form_actions import limpiar
from views.compras.date_picker_factory import crear_date_picker
from views.compras.classification_factory import crear_btn_clasificacion
from views.compras.suggestions_factory import crear_sugerencias, registrar_eventos
from views.compras.buttons_factory import crear_btn_nueva_factura, crear_btn_exportar_csv, crear_btn_exportar_excel, crear_btn_exportar_casilla_163
from views.compras.callbacks import crear_callback_modal
from views.compras.compras_controller import ComprasController

def vista_compras(page: ft.Page, abrir_proveedor):

    controller = ComprasController(
        page, abrir_proveedor
    )
    # ========= CAMPOS =========

    state = controller.state

    sugerencias = crear_sugerencias()

    controller.crear_controles(sugerencias)
    controls = controller.controls

    dd_periodos = crear_dropdown_periodos()

    nombre_periodo_actual = crear_nombre_periodo()
    
    btn_fecha = crear_date_picker(
        page,controls
    )

    accion_limpiar = lambda: limpiar(
        page, state, controls, sugerencias
    )

    # ========= FUNCIONES =========       


    btn_clasificacion = crear_btn_clasificacion(
        page, state, controls
    )

    cargar = None

    abrir_modal_callback = crear_callback_modal(
        page=page,
        state=state,
        controls=controls,
        limpiar=accion_limpiar,
        abrir_proveedor=abrir_proveedor,
        btn_clasificacion=btn_clasificacion,
        btn_fecha=btn_fecha,
        sugerencias=sugerencias,
        get_cargar=lambda: cargar,
    )

    tabla, cargar = crear_tabla_compras(
        page=page,
        state=state,
        abrir_modal= abrir_modal_callback,
        mostrar_mensaje = lambda texto: mostrar_mensaje(
            page, 
            texto
        ),
        mostrar_confirmacion = lambda titulo, mensaje, accion: mostrar_confirmacion(
            page,
            titulo,
            mensaje,
            accion
        )
    )

    btn_nueva_factura = crear_btn_nueva_factura(
        page=page,
        state=state,
        controls=controls,
        limpiar=accion_limpiar,
        cargar=cargar,
        abrir_proveedor=abrir_proveedor,
        btn_clasificacion=btn_clasificacion,
        btn_fecha=btn_fecha,
        sugerencias=sugerencias,
    )

    # Bloquear si no hay período seleccionado
    btn_nueva_factura.disabled = state.periodo_actual is None

    btn_exportar_csv = crear_btn_exportar_csv(
        page=page,
        state=state,
        mostrar_mensaje=mostrar_mensaje,
        mostrar_error=mostrar_error,
    )

    btn_exportar_excel = crear_btn_exportar_excel(
        page=page,
        state=state,
        mostrar_mensaje=mostrar_mensaje,
        mostrar_error=mostrar_error,
    )

    btn_exportar_casilla_163 = crear_btn_exportar_casilla_163(
        page=page,
        state=state,
        mostrar_mensaje=mostrar_mensaje,
        mostrar_error=mostrar_error,
    )

    cargar_dropdowns(state, controls, dd_periodos)

    mostrar_modal_periodo(
        page=page,
        state=state,
        dd_periodos=dd_periodos,
        nombre_periodo_actual=nombre_periodo_actual,
        btn_nueva_factura=btn_nueva_factura,
        seleccionar_periodo= lambda: seleccionar_periodo(
            dd_periodos
        ),
        cargar=cargar,
        mostrar_error = lambda titulo, mensaje: mostrar_error(
            page,
            titulo,
            mensaje
        )
    )
    cargar()

    registrar_eventos(page, state, sugerencias, controls)

    return ft.Container(
        padding=20,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Column([
                            ft.Text(
                                "Compras",
                                size=28,
                                weight=ft.FontWeight.BOLD
                            ),
                            nombre_periodo_actual
                        ]),
                        btn_exportar_csv,
                        btn_exportar_excel,
                        btn_exportar_casilla_163,
                        btn_nueva_factura,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Row(
                    [tabla],
                    scroll=ft.ScrollMode.AUTO
                )
            ]
        )
    )