import flet as ft
from models.emisor import Emisor


def construir_tabla():
    return ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre Comercial")),
            ft.DataColumn(ft.Text("Razon Social")),
            ft.DataColumn(ft.Text("NIT")),
            ft.DataColumn(ft.Text("DUI")),
            ft.DataColumn(ft.Text("NRC")),
            ft.DataColumn(ft.Text("Tamaño Contribuyente")),
            ft.DataColumn(ft.Text("Actividad economica")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Correo")),
            ft.DataColumn(ft.Text("Direccion")),
            ft.DataColumn(ft.Text("Acciones"))
        ],
        rows=[]
    )


def cargar_filas(page: ft.Page, tabla: ft.DataTable, on_editar, on_eliminar):
    tabla.rows.clear()
    emisores = Emisor.obtener_todos()

    for e in emisores:
        btn_editar = ft.IconButton(
            icon=ft.Icons.EDIT,
            on_click=lambda ev, emisor=e: on_editar(emisor)
        )
        btn_eliminar = ft.IconButton(
            icon=ft.Icons.DELETE,
            on_click=lambda ev, id_emisor=e[0]: on_eliminar(id_emisor)
        )

        tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(e[2]))),
                    ft.DataCell(ft.Text(str(e[3]))),
                    ft.DataCell(ft.Text(str(e[4]))),
                    ft.DataCell(ft.Text(str(e[5]))),
                    ft.DataCell(ft.Text(str(e[6]))),
                    ft.DataCell(ft.Text(Emisor.obtener_tamaño_contribuyente(e[7]))),
                    ft.DataCell(ft.Text(str(e[8]))),
                    ft.DataCell(ft.Text(str(e[9]))),
                    ft.DataCell(ft.Text(str(e[10]))),
                    ft.DataCell(ft.Text(str(e[11]))),
                    ft.DataCell(ft.Row([btn_editar, btn_eliminar]))
                ]
            )
        )
    page.update()