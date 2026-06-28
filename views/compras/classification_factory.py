import flet as ft
from views.compras.modal_clasificacion import mostrar_modal_clasificacion

def crear_btn_clasificacion(page, state, controls):

    btn_clasificacion = ft.ElevatedButton(
        "Seleccionar Clasificación",
        icon=ft.Icons.CATEGORY,
        on_click = lambda e: mostrar_modal_clasificacion(page, state, controls)
    )

    return btn_clasificacion