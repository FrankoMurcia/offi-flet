import flet as ft

def crear_modal(titulo, controls, sugerencias, btn_nuevo_proveedor, btn_clasificacion, btn_fecha, guardar_modal, cerrar_modal):
    
    dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Container(
                width=1000,
                padding=25,
                border_radius=20,
                bgcolor="#252A34",
                content=ft.Column(
                    [
                        ft.Text(
                            "Información del Documento",
                            size=16,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Row([
                            ft.Row([controls.txt_fecha, btn_fecha]),
                            controls.dd_clase_documento,
                            controls.dd_tipo_documento,
                        ]),

                        ft.Row([
                            controls.txt_codigo_generacion,
                            controls.txt_numero_control,
                            controls.txt_sello_recepcion
                        ]),
                        ft.Divider(),

                        ft.Text(
                            "Información del Emisor",
                            size=16,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Row([
                            ft.Column([
                                ft.Row([
                                    controls.txt_buscar_nit,
                                    ft.Container(
                                        expand=True,
                                        content=controls.txt_nombre_emisor
                                    )
                                ]),
                                sugerencias,
                                btn_nuevo_proveedor
                            ])
                        ]),

                        ft.Divider(),

                            ft.Text(
                                "Clasificación Fiscal",
                                size=16,
                                weight=ft.FontWeight.BOLD
                            ),

                            btn_clasificacion,

                            ft.Column([

                                ft.Container(
                                padding=15,
                                border_radius=10,
                                bgcolor=ft.Colors.BLUE_GREY_800,
                                content=ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Tipo Operación",
                                                    size=12,
                                                    color=ft.Colors.GREY_400
                                                ),
                                                controls.txt_tipo_operacion
                                            ],
                                            spacing=5
                                        ),
                                        ft.VerticalDivider(width=20),

                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Clasificación",
                                                    size=12,
                                                    color=ft.Colors.GREY_400
                                                ),
                                                controls.txt_clasificacion
                                            ],
                                            spacing=5
                                        ),

                                        ft.VerticalDivider(width=20),

                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Sector",
                                                    size=12,
                                                    color=ft.Colors.GREY_400
                                                ),
                                                controls.txt_sector
                                            ],
                                            spacing=5
                                        ),

                                        ft.VerticalDivider(width=20),

                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Tipo Costo/Gasto",
                                                    size=12,
                                                    color=ft.Colors.GREY_400
                                                ),
                                                controls.txt_tipo_gasto
                                            ],
                                            spacing=5
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                )
                            )
                            ]),

                        ft.Divider(),

                        ft.Text(
                            "Totales",
                            size=16,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Column([
                            ft.Row([
                                controls.txt_compras_internas_exentas,
                                controls.txt_internaciones_exentas_no_sujetas,
                                controls.txt_importaciones_exentas_no_sujetas,
                            ]),
                            ft.Row([
                                controls.txt_subtotal
                            ]),
                            ft.Row([
                                controls.txt_internaciones_gravadas_bienes,
                                controls.txt_importaciones_gravadas_bienes,
                                controls.txt_importaciones_gravadas_servicios,
                            ]),
                            ft.Row([
                                controls.txt_iva,
                                controls.txt_iva_percibido,
                                controls.txt_total
                            ])
                        ])
                    ],
                    #tight=True,
                    scroll= ft.ScrollMode.AUTO
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
    return dialog