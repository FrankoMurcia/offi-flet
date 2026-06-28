import flet as ft

from views.compras.proveedor_search import navegar_sugerencias

def crear_sugerencias():

    return ft.Container(
        content=ft.Column(
            spacing=0,
            scroll=ft.ScrollMode.AUTO
        ),
        height=150,
        visible=False,
        border= ft.border.all(1, ft.Colors.GREY_700),
        border_radius=8,
        bgcolor="#2b2d31"
    )

def registrar_eventos(page, state, sugerencias, controls):

    page.on_keyboard_event = lambda e: navegar_sugerencias(e, state, sugerencias, controls, page)