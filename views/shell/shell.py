import flet as ft

from views.shell.navigation import crear_navigation
from views.shell.router import cambiar_vista
from views.shell.close_controller import registrar_evento_cierre
from views.shell.logout_controller import cerrar_sesion

def crear_shell(page, mostrar_login):

    contenido = ft.Container(expand=True)
    registrar_evento_cierre(page)

    def cambiar(e):

        cambiar_vista(
            rail.selected_index,
            contenido,
            page,
            rail
        )

        page.update()

    rail = crear_navigation(cambiar)

    cambiar_vista(
        0,
        contenido,
        page,
        rail
    )

    menu = ft.Container(
        width=120,
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    content=rail,
                    expand=True,
                ),

                ft.Divider(height=1),

                ft.Container(
                    padding=10,
                    expand = False,
                    content=ft.Column(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.LOGOUT,
                                icon_size=26,
                                tooltip="Cerrar sesión",
                                on_click=lambda e: cerrar_sesion(
                                    page,
                                    mostrar_login
                                ),
                            ),
                            ft.Text(
                                "Cerrar Sesion",
                                size=11,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=2,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ),
            ],
        )
    )

    return ft.Row(
        controls=[
            menu,
            ft.VerticalDivider(width=1),
            contenido,
        ],
        expand=True,
    )