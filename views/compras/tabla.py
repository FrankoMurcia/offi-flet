import flet as ft

from models.compras import Factura
from models.emisor import Emisor
from models.Clasificaciones.tipo_documento import TipoDocumento


def crear_tabla_compras(page, state, abrir_modal, mostrar_mensaje, mostrar_confirmacion):

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Tipo Documento")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Código de Generación")),
            ft.DataColumn(ft.Text("Número de Control")),
            ft.DataColumn(ft.Text("Sello de Recepción")),
            ft.DataColumn(ft.Text("Emisor")),
            ft.DataColumn(ft.Text("Sub-Total")),
            ft.DataColumn(ft.Text("IVA")),
            ft.DataColumn(ft.Text("Total")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[],
    )

    def eliminar(id_factura):

        def ejecutar_eliminacion():
            Factura.eliminar(id_factura)

            mostrar_mensaje(
                "Compra eliminada correctamente"
            )

            cargar()

        mostrar_confirmacion(
            "Eliminar",
            "¿Desea eliminar esta Compra?",
            ejecutar_eliminacion,
        )

    def cargar():

        tabla.rows.clear()

        if state.periodo_actual:
            facturas = Factura.obtener_por_periodo(
                state.periodo_actual
            )
        else:
            facturas = []

        total_subtotal = 0.0
        total_iva = 0.0
        total_general = 0.0

        for f in facturas:

            total_subtotal += float(f[6])
            total_iva += float(f[7])
            total_general += float(f[8])

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                tooltip="Editar",
                on_click=lambda e, factura=f: abrir_modal(factura),
            )

            btn_eliminar = ft.IconButton(
                icon=ft.Icons.DELETE,
                tooltip="Eliminar",
                on_click=lambda e, id_factura=f[0]: eliminar(id_factura),
            )

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(
                            ft.Text(TipoDocumento.obtener_por_id(f[16]))
                        ),
                        ft.DataCell(ft.Text(str(f[2]))),
                        ft.DataCell(ft.Text(str(f[3]))),
                        ft.DataCell(ft.Text(str(f[4]))),
                        ft.DataCell(ft.Text(str(f[5]))),
                        ft.DataCell(ft.Text(Emisor.obtener_por_id(f[17]))),
                        ft.DataCell(ft.Text(f"{float(f[6]):,.2f}")),
                        ft.DataCell(ft.Text(f"{float(f[7]):,.2f}")),
                        ft.DataCell(ft.Text(f"{float(f[8]):,.2f}")),
                        ft.DataCell(
                            ft.Row(
                                [
                                    btn_editar,
                                    btn_eliminar,
                                ]
                            )
                        ),
                    ]
                )
            )

        # ================================
        # FILA DE TOTALES
        # ================================

        if facturas:

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(
                            ft.Text(
                                "TOTAL",
                                weight=ft.FontWeight.BOLD,
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                f"{total_subtotal:,.2f}",
                                weight=ft.FontWeight.BOLD,
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                f"{total_iva:,.2f}",
                                weight=ft.FontWeight.BOLD,
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                f"{total_general:,.2f}",
                                weight=ft.FontWeight.BOLD,
                            )
                        ),
                        ft.DataCell(ft.Text("")),
                    ]
                )
            )

        #page.update()

    return tabla, cargar