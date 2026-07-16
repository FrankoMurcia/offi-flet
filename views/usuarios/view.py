import flet as ft

from views.usuarios.controller import UsuarioController

from views.usuarios.tabla import crear_tabla

from views.usuarios.modal_controller import abrir_modal
import flet as ft

from models.usuario import Usuario
from views.usuarios.service import eliminar_usuario
from views.compras.dialogs import mostrar_confirmacion

def crear_tabla(page,abrir_modal, mostrar_confirmacion):

    tabla = ft.DataTable(

        columns=[

            ft.DataColumn(ft.Text("Usuario")),

            ft.DataColumn(ft.Text("Contraseña")),

            ft.DataColumn(ft.Text("Nombre")),

            ft.DataColumn(ft.Text("Rol")),

            ft.DataColumn(ft.Text("Acciones"))

        ],

        rows=[]

    )

    def eliminar(usuario):

        def ejecutar():

            eliminar_usuario(usuario[0])

            cargar()

            page.update()

        mostrar_confirmacion(
            page,
            "Eliminar usuario",
            f"¿Desea eliminar el usuario '{usuario[1]}'?",
            ejecutar
        )

    def cargar():

        tabla.rows.clear()

        for usuario in Usuario.obtener_todos():

            tabla.rows.append(

                ft.DataRow(

                    cells=[

                        ft.DataCell(

                            ft.Text(usuario[1])

                        ),

                        
                        ft.DataCell(

                            ft.Text(usuario[2])

                        ),

                        ft.DataCell(

                            ft.Text(usuario[3])

                        ),

                        ft.DataCell(

                            ft.Text(usuario[4])

                        ),
                        ft.DataCell(

                            ft.Row(

                                [

                                    ft.IconButton(

                                        ft.Icons.EDIT,

                                        tooltip="Editar",

                                        on_click=lambda e,
                                        u=usuario:

                                            abrir_modal(u)

                                    ),

                                    ft.IconButton(

                                        ft.Icons.DELETE,

                                        tooltip="Eliminar",

                                        on_click=lambda e,
                                        u=usuario:

                                            eliminar(u)

                                    )

                                ]

                            )

                        )

                    ]

                )
            )
        #tabla.update()
        page.update()

    cargar()
    
    return tabla, cargar

def vista_usuarios(page):

    controller = UsuarioController(page)

    controller.crear_controles()

    abrir_modal_callback = lambda usuario=None: abrir_modal(

        page,

        controller,

        cargar,

        usuario

    )

    tabla,cargar=crear_tabla(

        page,

        abrir_modal_callback,

        mostrar_confirmacion

    )


    boton = ft.ElevatedButton(

        "Nuevo Usuario",

        on_click=lambda e:

            abrir_modal_callback()

    )

    return ft.Container(

        padding=20,

        content=ft.Column(

            [

                ft.Row(

                    [

                        ft.Text(

                            "Usuarios",

                            size=28,

                            weight=ft.FontWeight.BOLD

                        ),

                        boton

                    ],

                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN

                ),

                tabla

            ]

        )

    )