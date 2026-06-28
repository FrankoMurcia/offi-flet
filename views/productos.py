import flet as ft
from models.producto import Producto


def vista_productos(page: ft.Page):

    txt_nombre = ft.TextField(
        label="Nombre", 
        width=300,
        border_radius= 10,
    )
    txt_cantidad = ft.TextField(
        label="Cantidad", 
        width=300,
        border_radius= 10
    )
    txt_precio = ft.TextField(
        label="Precio", 
        width=300,
        border_radius= 10
        )

    id_edicion = None

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Cantidad")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[]
    )

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()

    def limpiar_campos():

        txt_nombre.value = ""
        txt_cantidad.value = ""
        txt_precio.value = ""

        page.update()

    print("ANTES DEL MODAL")

    def mostrar_confirmacion(titulo, mensaje, accion):

        def confirmar(e):
            print("CONFIRMADO")
            dialog.open = False
            page.update()
            accion()

        def cancelar(e):
            print("CANCELADO")
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton("Cancelar", on_click=cancelar),
                ft.TextButton("Confirmar", on_click=confirmar),
            ],
        )

        page.show_dialog(dialog)

    def cargar():

        tabla.rows.clear()

        productos = Producto.obtener_todos()

        for p in productos:

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                tooltip="Editar",
                on_click=lambda e, producto=p: seleccionar_edicion(producto)
            )

            btn_eliminar = ft.IconButton(
                icon=ft.Icons.DELETE,
                tooltip="Eliminar",
                on_click=lambda e, producto_id=p[0]: eliminar_producto(producto_id)
            )

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(p[0]))),
                        ft.DataCell(ft.Text(p[1])),
                        ft.DataCell(ft.Text(str(p[2]))),
                        ft.DataCell(ft.Text(f"${p[3]:.2f}")),
                        ft.DataCell(
                            ft.Row(
                                [btn_editar, btn_eliminar]
                            )
                        )
                    ]
                )
            )

        page.update()

    def seleccionar_edicion(producto):

        nonlocal id_edicion

        id_edicion = producto[0]

        txt_nombre.value = producto[1]
        txt_cantidad.value = str(producto[2])
        txt_precio.value = str(producto[3])

        btn_guardar.content = ft.Text("Actualizar")
        page.update()

    def guardar(e):
        print("BOTON GUARDAR PRESIONADO")
        nombre = txt_nombre.value.strip()

        if not nombre:
            mostrar_mensaje("Debe ingresar un nombre.")
            return

        try:
            cantidad = int(txt_cantidad.value)
            precio = float(txt_precio.value)
        except ValueError:
            mostrar_mensaje("Cantidad o precio inválidos.")
            return

        def ejecutar_guardado():

            print("EJECUTANDO GUARDADO")
            nonlocal id_edicion

            if id_edicion is None:

                Producto.guardar(
                    nombre,
                    cantidad,
                    precio
                )

                mostrar_mensaje(
                    "Producto guardado correctamente."
                )

            else:

                Producto.editar(
                    id_edicion,
                    nombre,
                    cantidad,
                    precio
                )

                mostrar_mensaje(
                    "Producto actualizado correctamente."
                )

                id_edicion = None
                btn_guardar.content = ft.Text("Guardar")

            limpiar_campos()
            cargar()

        mensaje = (
            "¿Desea guardar este producto?"
            if id_edicion is None
            else
            "¿Desea actualizar este producto?"
        )

        mostrar_confirmacion(
            
            "Confirmación",
            mensaje,
            ejecutar_guardado
        )

    def eliminar_producto(producto_id):

        def ejecutar_eliminacion():

            Producto.eliminar(producto_id)

            mostrar_mensaje(
                "Producto eliminado correctamente."
            )

            cargar()

        mostrar_confirmacion(
            "Eliminar producto",
            "¿Está seguro de eliminar este producto?",
            ejecutar_eliminacion
        )

    btn_guardar = ft.ElevatedButton(
        "Guardar",
        icon=ft.Icons.SAVE,
        on_click=guardar
        
    )

    cargar()

    return ft.Column(
        [
            ft.Text(
                "Gestión de Productos",
                size=28,
                weight=ft.FontWeight.BOLD,
            ),
            ft.Row(
                [
                    txt_nombre,
                    txt_cantidad,
                    txt_precio
                ]
            ),
            btn_guardar,

            #ft.Divider(),

            tabla,
        ],
        expand=True,
        scroll=ft.ScrollMode.AUTO,
    )