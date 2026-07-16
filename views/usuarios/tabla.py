import flet as ft

from models.usuario import Usuario
from views.usuarios.service import eliminar_usuario

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

            Usuario.eliminar(usuario[0])

            cargar()

        mostrar_confirmacion(

            page,

            "Eliminar usuario",

            f"¿Desea eliminar el usuario '{usuario[1]}'?",

            ejecutar

        )

    def confirmar_eliminacion(id_usuario):

        eliminar_usuario(id_usuario)

        cargar()

        page.update()

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

                                            abrir_modal(page)

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
        tabla.update()

    cargar()
    
    return tabla, cargar