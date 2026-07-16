import flet as ft
from views.compras.modal_controller import abrir_modal
from views.compras.export_controller import descargar_csv, descargar_excel, descargar_casilla_163

def crear_btn_nueva_factura(page, state,controls, limpiar, cargar, abrir_proveedor, btn_clasificacion, btn_fecha, sugerencias,):

    return ft.ElevatedButton(
        content=ft.Text("Nueva Compra"),
        icon=ft.Icons.ADD,
        on_click=lambda e: abrir_modal(
            page=page,
            state=state,
            controls=controls,
            factura=None,
            limpiar=limpiar,
            cargar=cargar,
            abrir_proveedor=abrir_proveedor,
            btn_clasificacion=btn_clasificacion,
            btn_fecha=btn_fecha,
            sugerencias=sugerencias,
        )
    )

def crear_btn_exportar_csv(page, state, mostrar_mensaje, mostrar_error):

    return ft.ElevatedButton(

        "Exportar CSV",

        icon=ft.Icons.DOWNLOAD,

        on_click=lambda e: descargar_csv(page,state,mostrar_mensaje, mostrar_error)
    )

def crear_btn_exportar_excel(page, state, mostrar_mensaje, mostrar_error):

    return ft.ElevatedButton(

        "Exportar Excel",

        icon=ft.Icons.TABLE_VIEW,

        on_click=lambda e: descargar_excel(page, state, mostrar_mensaje, mostrar_error)
    )

def crear_btn_exportar_casilla_163(page, state, mostrar_mensaje, mostrar_error):

    return ft.ElevatedButton(

        "Exportar Casilla 163",

        icon=ft.Icons.REQUEST_PAGE,

        on_click=lambda e: descargar_casilla_163(page, state, mostrar_mensaje, mostrar_error)
    )