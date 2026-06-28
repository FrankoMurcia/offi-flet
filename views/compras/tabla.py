import flet as ft

from models.compras import Factura
from models.emisor import Emisor
from models.Clasificaciones.tipo_documento import TipoDocumento

def crear_tabla_compras(page, state, abrir_modal, mostrar_mensaje, mostrar_confirmacion):

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Tipo Documento")),
            ft.DataColumn(ft.Text("Fecha")),
            ft.DataColumn(ft.Text("Codigo de Generacion")),
            ft.DataColumn(ft.Text("Numero de Control")),
            ft.DataColumn(ft.Text("Sello de Recepcion")),
            ft.DataColumn(ft.Text("Emisor")),
            ft.DataColumn(ft.Text("Sub-Total")),
            ft.DataColumn(ft.Text("IVA")),
            ft.DataColumn(ft.Text("Total")),
            ft.DataColumn(ft.Text("Acciones"))
        ],
        rows=[]
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
            ejecutar_eliminacion
        )  
    
    def cargar():

        tabla.rows.clear()

        if state.periodo_actual:
            facturas = Factura.obtener_por_periodo(
                state.periodo_actual
            )
        else:
            facturas = []

        for f in facturas:

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                tooltip="Editar",
                on_click=lambda e, factura=f:
                abrir_modal(factura)
            )

            btn_eliminar = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=lambda e, id_factura=f[0]:
                eliminar(id_factura)
            )

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(TipoDocumento.obtener_por_id(f[15]))),
                        ft.DataCell(ft.Text(str(f[1]))),
                        ft.DataCell(ft.Text(str(f[2]))),
                        ft.DataCell(ft.Text(str(f[3]))),
                        ft.DataCell(ft.Text(str(f[4]))),
                        ft.DataCell(ft.Text(Emisor.obtener_por_id(f[16]))),
                        ft.DataCell(ft.Text(str(f[5]))),
                        ft.DataCell(ft.Text(str(f[6]))),
                        ft.DataCell(ft.Text(str(f[7]))),
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
    
    return tabla, cargar