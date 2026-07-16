import flet as ft

from views.usuarios.formulario import crear_formulario
from views.usuarios.service import guardar_o_editar
from views.usuarios.validaciones import validar_usuario


def abrir_modal(

        page,

        controller,

        cargar,

        usuario=None

):

    controls = controller.controls

    state = controller.state

    if usuario:

        state.id_edicion = usuario[0]

        controls.txt_usuario.value = usuario[1]

        controls.txt_contraseña.value = usuario[2]

        controls.txt_nombre.value = usuario[3]

        controls.dd_rol.value = usuario[4]

        titulo = "Editar Usuario"
    
    else:

        state.id_edicion = None

        controls.txt_usuario.value = ""

        controls.txt_contraseña.value = ""

        controls.txt_nombre.value = ""

        controls.dd_rol.value = None

        titulo = "Nuevo Usuario"

    dialog = ft.AlertDialog(

        modal=True,

        title=ft.Text(titulo),

        content=crear_formulario(controls),

        actions=[

            ft.TextButton(

                "Cancelar",

                on_click=lambda e: cerrar()

            ),

            ft.ElevatedButton(

                "Guardar",

                on_click=lambda e: guardar()

            )

        ]

    )

    def cerrar():

        dialog.open = False

        page.update()

    def guardar():

        valido, mensaje = validar_usuario(

            state,

            controls

        )

        if not valido:

            page.snack_bar = ft.SnackBar(

                ft.Text(mensaje)

            )

            page.snack_bar.open = True

            page.update()

            return

        guardar_o_editar(

            state,

            controls

        )

        dialog.open = False

        cargar()

        page.update()
    
    page.show_dialog(dialog)