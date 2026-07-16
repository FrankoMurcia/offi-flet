import flet as ft

from auth import session


def crear_navigation(on_change):

    destinos = [

        ft.NavigationRailDestination(

            icon=ft.Icons.HOME,
            label="Inicio"

        ),

        ft.NavigationRailDestination(

            icon=ft.Icons.BUSINESS,
            label="Proveedores"

        ),

        ft.NavigationRailDestination(

            icon=ft.Icons.ARTICLE,
            label="Compras"

        )

    ]

    usuario = session.obtener()

    if usuario and usuario[4] == "Administrador":

        destinos.append(

            ft.NavigationRailDestination(

                icon=ft.Icons.GROUP,
                label="Usuarios"

            )

        )

    return ft.NavigationRail(
        
        expand= True,

        selected_index=0,

        on_change=on_change,

        destinations=destinos

    )