import flet as ft

from models.detalle_clasificador import DetalleClasificador
from models.Clasificaciones.tipo_documento import TipoDocumento
from models.Clasificaciones.clase_documento import ClaseDocumento
from models.Clasificaciones.clasificacion import Clasificacion
from models.Clasificaciones.sector import Sector
from models.Clasificaciones.tipo_costo_gasto import TipoCostoGasto
from models.Clasificaciones.tipo_operacion  import TipoOperacion


def vista_detalle_clasificador(page: ft.Page):

    id_edicion = None

    dd_tipo_documento = ft.Dropdown(
        label="Tipo Documento",
        width=350
    )

    dd_clase_documento = ft.Dropdown(
        label="Clase Documento",
        width=350
    )

    dd_clasificacion = ft.Dropdown(
        label="Clasificación",
        width=350
    )

    dd_sector = ft.Dropdown(
        label="Sector",
        width=350
    )

    dd_tipo_costo_gasto = ft.Dropdown(
        label="Tipo Costo/Gasto",
        width=350
    )
    dd_tipo_operacion = ft.Dropdown(
        label= "Tipo Operacion",
        width=350
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Tipo Documento")),
            ft.DataColumn(ft.Text("Clase Documento")),
            ft.DataColumn(ft.Text("Clasificación")),
            ft.DataColumn(ft.Text("Sector")),
            ft.DataColumn(ft.Text("Costo/Gasto")),
            ft.DataColumn(ft.Text("Tipo Operacion")),
            ft.DataColumn(ft.Text("Acciones"))
        ],
        rows=[]
    )

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()

    def limpiar():

        dd_tipo_documento.value = None
        dd_clase_documento.value = None
        dd_clasificacion.value = None
        dd_sector.value = None
        dd_tipo_costo_gasto.value = None
        dd_tipo_operacion.value = None

        page.update()

    btn_nuevo = ft.ElevatedButton(
        content=ft.Text("Nuevo Registro"),
        icon=ft.Icons.ADD,
        on_click=lambda e: abrir_modal()
    )

    def cargar_dropdowns():

        # Tipo Documento
        dd_tipo_documento.options = [
            ft.dropdown.Option(
                key=str(t[0]),
                text=t[1]
            )
            for t in TipoDocumento.obtener_todos()
        ]

        # Clase Documento
        dd_clase_documento.options = [
            ft.dropdown.Option(
                key=str(id_),
                text=descripcion
            )
            for id_, descripcion in ClaseDocumento.obtener_todos()
        ]

        # Clasificación
        dd_clasificacion.options = [
            ft.dropdown.Option(
                key=str(id_),
                text=descripcion
            )
            for id_, descripcion in Clasificacion.obtener_todos()
        ]

        # Sector
        dd_sector.options = [
            ft.dropdown.Option(
                key=str(id_),
                text=descripcion
            )
            for id_, descripcion in Sector.obtener_todos()
        ]

        # Tipo costo gasto
        dd_tipo_costo_gasto.options = [
            ft.dropdown.Option(
                key=str(id_),
                text=descripcion
            )
            for id_, descripcion in TipoCostoGasto.obtener_todos()
        ]

        #tipo operacion
        dd_tipo_operacion.options = [
            ft.dropdown.Option(
                key=str(id_),
                text= descripcion
            )
            for id_, descripcion in TipoOperacion.obtener_todos()
        ]

    def cerrar_modal(dialog):
        dialog.open = False
        page.update()

    def abrir_modal(detalle=None):

        nonlocal id_edicion

        if detalle:

            id_edicion = detalle[0]

            dd_tipo_documento.value = str(detalle[1])
            dd_clase_documento.value = str(detalle[2])
            dd_clasificacion.value = str(detalle[3])
            dd_sector.value = str(detalle[4])
            dd_tipo_costo_gasto.value = str(detalle[5])
            dd_tipo_operacion.value = str(detalle[6])

            titulo = "Editar Registro"

        else:

            id_edicion = None

            limpiar()

            titulo = "Nuevo Registro"

        def guardar_modal(e):

            def ejecutar_guardado():

                nonlocal id_edicion

                try:

                    if id_edicion is None:

                        DetalleClasificador.guardar(
                            int(dd_tipo_documento.value),
                            int(dd_clase_documento.value),
                            int(dd_clasificacion.value),
                            int(dd_sector.value),
                            int(dd_tipo_costo_gasto.value),
                            int(dd_tipo_operacion.value)
                        )

                        mostrar_mensaje(
                            "Registro guardado correctamente"
                        )

                    else:

                        DetalleClasificador.editar(
                            id_edicion,
                            int(dd_tipo_documento.value),
                            int(dd_clase_documento.value),
                            int(dd_clasificacion.value),
                            int(dd_sector.value),
                            int(dd_tipo_costo_gasto.value),
                            int(dd_tipo_operacion.value)
                        )

                        mostrar_mensaje(
                            "Registro actualizado correctamente"
                        )

                    dialog.open = False

                    limpiar()
                    cargar()

                    page.update()

                except Exception as ex:

                    mostrar_mensaje(str(ex))

            mostrar_confirmacion(
                "Confirmación",
                "¿Desea guardar los cambios?",
                ejecutar_guardado
            )

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Container(
                width=850,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                dd_tipo_documento,
                                dd_clase_documento
                            ]
                        ),

                        ft.Row(
                            [
                                dd_clasificacion,
                                dd_sector,
                            ]
                        ),
                        ft.Row(
                            [
                                dd_tipo_costo_gasto,
                                dd_tipo_operacion
                            ]
                        )
                    ],
                    tight=True
                )
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: cerrar_modal(dialog)
                ),
                ft.ElevatedButton(
                    content=ft.Text("Guardar"),
                    icon=ft.Icons.SAVE,
                    on_click=guardar_modal
                )
            ]
        )

        page.show_dialog(dialog)

    def mostrar_confirmacion(titulo, mensaje, accion):

        def confirmar(e):
            dialog.open = False
            page.update()
            accion()

        def cancelar(e):
            dialog.open = False
            page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=cancelar
                ),
                ft.TextButton(
                    "Confirmar",
                    on_click=confirmar
                )
            ]
        )

        page.show_dialog(dialog)

    def cargar():

        tabla.rows.clear()

        datos = DetalleClasificador.obtener_todos()

        for d in datos:

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                tooltip= "Editar",
                on_click=lambda e, detalle=d:
                abrir_modal(detalle)
            )

            btn_eliminar = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=lambda e, id_detalle=d[0]:
                eliminar(id_detalle)
            )

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(d[0]))),
                        ft.DataCell(ft.Text(str(d[1]))),
                        ft.DataCell(ft.Text(str(d[2]))),
                        ft.DataCell(ft.Text(str(d[3]))),
                        ft.DataCell(ft.Text(str(d[4]))),
                        ft.DataCell(ft.Text(str(d[5]))),
                        ft.DataCell(ft.Text(str(d[6]))),
                        ft.DataCell(
                            ft.Row([
                                btn_editar,
                                btn_eliminar
                            ])
                        )
                    ]
                )
            )

        page.update()

    def eliminar(id_detalle):

        def ejecutar_eliminacion():

            DetalleClasificador.eliminar(id_detalle)

            mostrar_mensaje(
                "Registro eliminado correctamente"
            )

            cargar()

        mostrar_confirmacion(
            "Eliminar",
            "¿Desea eliminar este registro?",
            ejecutar_eliminacion
        )
        
    cargar_dropdowns()
    cargar()

    return ft.Container(
        padding=20,
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Detalle Clasificador",
                            size=28,
                            weight=ft.FontWeight.BOLD
                        ),

                        btn_nuevo
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                tabla
            ],
            spacing=10,
        )
    )