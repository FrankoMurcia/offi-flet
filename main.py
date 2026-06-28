import flet as ft

from database.crear_tablas import crear_tablas

from views.dashboard import dashboard
from views.productos import vista_productos
from views.emisor import vista_emisor
from views.detalle_clasificador import vista_detalle_clasificador
from views.compras.vista import vista_compras

def main(page: ft.Page):

    crear_tablas()

    page.title = "Sistema Facturación"

    contenido = ft.Container(
        expand=True
    )

    def abrir_proveedor():
        rail.selected_index = 2
        contenido.content = vista_emisor(page)
        page.update()

    def cambiar(e):

        if rail.selected_index == 0:
            contenido.content = dashboard()

        # elif rail.selected_index == 1:
        #     contenido.content = vista_productos(page)

        elif rail.selected_index == 1:
            contenido.content = vista_emisor(page)

        # elif rail.selected_index == 3:
        #     contenido.content = vista_detalle_clasificador(page)

        elif rail.selected_index == 2:
            contenido.content = vista_compras(
                page,
                lambda: abrir_proveedor()
                )
        page.update()


    rail = ft.NavigationRail(
        selected_index=0,
        on_change=cambiar,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME,
                label="Inicio"
            ),
            # ft.NavigationRailDestination(
            #     icon=ft.Icons.INVENTORY,
            #     label="Productos"
            # ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BUSINESS,
                label= "Proveedores"
            ),
            # ft.NavigationRailDestination(
            #     icon=ft.Icons.ACCOUNT_TREE,
            #     label="Clasificador"
            # ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ARTICLE,
                label="Compras"
            )
        ]
    )

    contenido.content = dashboard()

    page.add(
        ft.Row([
            rail,
            ft.VerticalDivider(),
            contenido
        ],
        expand=True)
    )

ft.run(main)