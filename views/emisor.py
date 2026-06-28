import flet as ft
from models.emisor import Emisor


def vista_emisor(page: ft.Page):

    txt_nombre_comercial = ft.TextField(
        label="Nombre Comercial",
        width=350,
        border_radius = 10,
        prefix_icon=ft.Icons.STORE,
    )

    txt_razon_social = ft.TextField(
        label="Razón Social",
        width=350,
        border_radius = 10,
        prefix_icon=ft.Icons.BUSINESS
    )

    def formatear_nit(e):
        # Solo números
        numeros = "".join(filter(str.isdigit, e.control.value))

        # Máximo 14 dígitos
        numeros = numeros[:14]

        resultado = ""

        if len(numeros) > 0:
            resultado += numeros[:4]

        if len(numeros) > 4:
            resultado += "-" + numeros[4:10]

        if len(numeros) > 10:
            resultado += "-" + numeros[10:13]

        if len(numeros) > 13:
            resultado += "-" + numeros[13:14]

        e.control.value = resultado
        e.control.update()

    txt_nit = ft.TextField(
        label="NIT",
        width=350,
        border_radius = 10,
        prefix_icon= ft.Icons.BADGE,
        on_change= formatear_nit
    )

    def formatear_dui(e):
        # Solo números
        numeros = "".join(filter(str.isdigit, e.control.value))

        # Máximo 9 dígitos
        numeros = numeros[:9]

        resultado = ""

        if len(numeros) > 0:
            resultado += numeros[:8]

        if len(numeros) > 8:
            resultado += "-" + numeros[8:9]

        e.control.value = resultado
        e.control.update()

    txt_dui = ft.TextField(
        label="DUI",
        width=170,
        border_radius = 10,
        prefix_icon=ft.Icons.PERSON,
        on_change= formatear_dui
    )

    def formatear_nrc(e):

        valor = e.control.value

        # Permitir solo números y guiones
        valor = "".join(
            c for c in valor
            if c.isdigit() or c == "-"
        )

        # Permitir un solo guion
        partes = valor.split("-")
        if len(partes) > 2:
            valor = partes[0] + "-" + "".join(partes[1:])

        e.control.value = valor
        e.control.update()

    txt_nrc = ft.TextField(
        label="NRC",
        width=170,
        border_radius = 10,
        prefix_icon=ft.Icons.CONFIRMATION_NUMBER,
        on_change= formatear_nrc
    )

    ddl_tamaño_contribuyente = ft.Dropdown(
        label="Tamaño Contribuyente",
        width=350,
        options=[
            ft.dropdown.Option("1", "Pequeño"),
            ft.dropdown.Option("2", "Mediano"),
            ft.dropdown.Option("3", "Grande"),
            ft.dropdown.Option("4", "Fiscalización o Agente de Percepción"),
            ft.dropdown.Option("5", "Retención No Inscritos al IVA 13%"),
        ]
    )

    txt_actividad = ft.TextField(
        label="Actividad Económica",
        width=350,
        border_radius = 10,
        prefix_icon=ft.Icons.WORK
    )

    def formatear_telefono(e):
        # Solo números
        numeros = "".join(filter(str.isdigit, e.control.value))

        # Máximo 8 dígitos
        numeros = numeros[:8]

        resultado = ""

        if len(numeros) > 0:
            resultado += numeros[:4]

        if len(numeros) > 4:
            resultado += "-" + numeros[4:8]

        e.control.value = resultado
        e.control.update()

    txt_telefono = ft.TextField(
        label="Teléfono",
        width=170,
        border_radius = 10,
        prefix_icon=ft.Icons.PHONE,
        on_change= formatear_telefono
    )

    txt_correo = ft.TextField(
        label="Correo Electrónico",
        width=350,
        border_radius = 10,
        prefix_icon=ft.Icons.EMAIL
    )

    txt_direccion = ft.TextField(
        label="Dirección",
        width=720,      
        border_radius = 10,  
        prefix_icon=ft.Icons.LOCATION_ON
    )

    btn_nuevo = ft.ElevatedButton(
        content= ft.Text("Nuevo Emisor"),
        icon= ft.Icons.ADD,
        on_click= lambda e: abrir_modal()
    )

    def cerrar_modal(dialog):

        dialog.open = False

        page.update()

    id_edicion = None

    tabla = ft.DataTable(
        columns=[
            #ft.DataColumn(ft.Text("ID")),
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

    def mostrar_mensaje(texto):

        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto)
        )

        page.snack_bar.open = True
        page.update()

    def limpiar():

        txt_nombre_comercial.value = ""
        txt_razon_social.value = ""
        txt_nit.value = ""
        txt_dui.value = ""
        txt_nrc.value = ""
        ddl_tamaño_contribuyente.value = ""
        txt_actividad.value = ""
        txt_telefono.value = ""
        txt_correo.value = ""
        txt_direccion.value = ""

    def mostrar_alerta(titulo, mensaje):

        def cerrar(e):
            dialog_alerta.open = False
            page.update()

        dialog_alerta = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton(
                    "Aceptar",
                    on_click=cerrar
                )
            ]
        )

        page.show_dialog(dialog_alerta)

    def abrir_modal(emisor=None):

        texto_boton = (
            "Actualizar"
            if emisor
            else "Guardar"
        )

        def guardar_modal(e):

            nombre_comercial = txt_nombre_comercial.value.strip()

            if nombre_comercial == "":
                mostrar_mensaje("Ingrese el nombre comercial.")
                return
            
            if not ddl_tamaño_contribuyente.value:
                mostrar_mensaje(
                    "Seleccione el tamaño del contribuyente."
                )
                return
            
            # Validar NIT duplicado
            if id_edicion is None and Emisor.existe_nit(txt_nit.value):
                mostrar_alerta(
                    "NIT duplicado",
                    f"Ya existe un emisor registrado con el NIT:\n\n{txt_nit.value}"
                )
                return
            
            # Validar NRC duplicado
            if id_edicion is None and Emisor.existe_nrc(txt_nrc.value):
                mostrar_alerta(
                    "NRC duplicado",
                    f"Ya existe un emisor registrado con el NRC:\n\n{txt_nrc.value}"
                )
                return

            def ejecutar_guardado():

                nonlocal id_edicion

                if id_edicion is None:

                    if Emisor.existe_nit(txt_nit.value):
                        mostrar_mensaje(
                            f"El NIT {txt_nit.value} ya se encuentra registrado"
                        )
                        return
                    
                    # if len(txt_nrc.value) != 8:
                    #     mostrar_alerta(
                    #         "NRC inválido",
                    #         "El NRC debe contener exactamente 8 dígitos."
                    #     )
                    #     return

                    Emisor.guardar(
                        txt_nombre_comercial.value,
                        txt_razon_social.value,
                        txt_nit.value,
                        txt_dui.value,
                        txt_nrc.value,
                        int(ddl_tamaño_contribuyente.value),
                        txt_actividad.value,
                        txt_telefono.value,
                        txt_correo.value,
                        txt_direccion.value
                    )

                    mostrar_mensaje(
                        "Emisor guardado correctamente."
                    )

                else:

                    if Emisor.existe_nit_otro(txt_nit.value, id_edicion):
                        mostrar_mensaje("Ya existe otro emisor con este NIT.")
                        return
                    
                    if Emisor.existe_nrc_otro(
                        txt_nrc.value,
                        id_edicion
                    ):
                        mostrar_alerta(
                            "NRC duplicado",
                            f"Ya existe otro emisor registrado con el NRC:\n\n{txt_nrc.value}"
                        )
                        return
                    
                    Emisor.editar(
                        id_edicion,
                        txt_nombre_comercial.value,
                        txt_razon_social.value,
                        txt_nit.value,
                        txt_dui.value,
                        txt_nrc.value,
                        int(ddl_tamaño_contribuyente.value),
                        txt_actividad.value,
                        txt_telefono.value,
                        txt_correo.value,
                        txt_direccion.value
                    )

                    mostrar_mensaje(
                        "Emisor actualizado correctamente."
                    )

                    id_edicion = None                

                dialog_emisor.open = False
                page.update()

                limpiar()
                cargar()

            mensaje = (
                "¿Desea guardar este emisor?"
                if id_edicion is None
                else
                "¿Desea actualizar este emisor?"
            )

            mostrar_confirmacion(
                "Confirmación",
                mensaje,
                ejecutar_guardado
            )

        nonlocal id_edicion

        if emisor:
            id_edicion = emisor[0]

            txt_nombre_comercial.value = emisor[1]
            txt_razon_social.value = emisor[2]
            txt_nit.value = emisor[3]
            txt_dui.value = emisor[4]
            txt_nrc.value = emisor[5]
            ddl_tamaño_contribuyente.value = str(emisor[6])
            txt_actividad.value = emisor[7]
            txt_telefono.value = emisor[8]
            txt_correo.value = emisor[9]
            txt_direccion.value = emisor[10]

            titulo = "Editar Emisor"
            texto_boton = "Actualizar"

        else:
            id_edicion = None
            limpiar()

            titulo= "Nuevo Emisor"
            texto_boton = "Guardar"

        dialog_emisor = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Container(
                width=850,
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                txt_nombre_comercial,
                                txt_razon_social
                            ]
                        ),

                        ft.Row(
                            [
                                txt_nit,
                                txt_dui,
                                txt_nrc
                            ],
                            wrap=True
                        ),

                        ft.Row(
                            [
                                ddl_tamaño_contribuyente,
                                txt_actividad
                            ]
                        ),

                        ft.Row(
                            [
                                txt_telefono,
                                txt_correo
                            ]
                        ),

                        ft.Row(
                            [
                                txt_direccion
                            ]
                        )
                    ]
                ),
            ),
            actions=[
                        ft.TextButton(
                            "Cancelar",
                            on_click= lambda e: cerrar_modal(dialog_emisor)
                        ),
                        ft.ElevatedButton(
                            texto_boton,
                            icon=ft.Icons.SAVE,
                            on_click=guardar_modal
                        )
                    ],
        )
        page.show_dialog(dialog_emisor)

    def mostrar_confirmacion(titulo, mensaje, accion):

        def confirmar(e):
            dialog_confirmacion.open = False
            page.update()
            accion()

        def cancelar(e):
            dialog_confirmacion.open = False
            page.update()

        dialog_confirmacion = ft.AlertDialog(
            modal=True,
            title=ft.Text(titulo),
            content=ft.Text(mensaje),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click= lambda e: cerrar_modal(dialog_confirmacion)
                ),
                ft.TextButton(   
                    "Confirmar",                 
                    on_click=confirmar
                )
            ]
        )
        page.show_dialog(dialog_confirmacion)

    def cargar():

        tabla.rows.clear()

        emisores = Emisor.obtener_todos()

        for e in emisores:

            btn_editar = ft.IconButton(
                icon=ft.Icons.EDIT,
                on_click=lambda ev, emisor=e: abrir_modal(emisor)
            )

            btn_eliminar = ft.IconButton(
                icon=ft.Icons.DELETE,
                on_click=lambda ev, id_emisor=e[0]: eliminar(id_emisor)
            )

            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        #ft.DataCell(ft.Text(str(e[0]))),
                        ft.DataCell(ft.Text(str(e[1]))),
                        ft.DataCell(ft.Text(str(e[2]))),
                        ft.DataCell(ft.Text(str(e[3]))),
                        ft.DataCell(ft.Text(str(e[4]))),
                        ft.DataCell(ft.Text(str(e[5]))),
                        ft.DataCell(ft.Text(Emisor.obtener_tamaño_contribuyente(e[6]))),
                        ft.DataCell(ft.Text(str(e[7]))),
                        ft.DataCell(ft.Text(str(e[8]))),
                        ft.DataCell(ft.Text(str(e[9]))),
                        ft.DataCell(ft.Text(str(e[10]))),
                        ft.DataCell(
                            ft.Row(
                                [
                                    btn_editar,
                                    btn_eliminar
                                ]
                            )
                        )
                    ]
                )
            )

        page.update()


    def eliminar(id_emisor):

        def ejecutar_eliminacion():

            Emisor.eliminar(id_emisor)

            mostrar_mensaje(
                "Emisor eliminado correctamente."
            )

            cargar()

        mostrar_confirmacion(
            "Eliminar emisor",
            "¿Desea eliminar este emisor?",
            ejecutar_eliminacion
        )

    cargar()

    return ft.Container(
        padding= ft.padding.only(top=10),
        content=ft.Column(
        [
            ft.Container(height=9),

            ft.Row(
                [
                    ft.Text(
                        "Gestión de Emisores",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),
                    btn_nuevo
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            ft.Divider(height=30),

            ft.Text(
                "Listado de Emisores",
                size=20,
                weight=ft.FontWeight.BOLD
            ),

            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text(
                                    "Emisores registrados",
                                    weight=ft.FontWeight.BOLD
                                )
                            ]
                        ),

                        ft.Divider(),

                        ft.Row(
                            [
                                tabla,

                            ],
                            scroll=ft.ScrollMode.AUTO
                        )
                    ]
                ),
                padding=20,
                border_radius=15,
                bgcolor=ft.Colors.BLUE_GREY_900
            )
        ],
        expand=True,
        spacing=20,
        scroll=ft.ScrollMode.AUTO
    )
    )
    