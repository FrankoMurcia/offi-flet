import flet as ft


class FormularioEmisor:
    def __init__(self):
        self.txt_nombre_comercial = ft.TextField(
            label="Nombre Comercial",
            border_radius=10,
            prefix_icon=ft.Icons.STORE,
            col={"xs": 12, "sm": 6},
        )
        self.txt_razon_social = ft.TextField(
            label="Razón Social",
            border_radius=10,
            prefix_icon=ft.Icons.BUSINESS,
            col={"xs": 12, "sm": 6},
        )
        self.txt_nit = ft.TextField(
            label="NIT",
            border_radius=10,
            prefix_icon=ft.Icons.BADGE,
            on_change=self.formatear_nit,
            col={"xs": 12, "sm": 6, "md": 4},
        )
        self.txt_dui = ft.TextField(
            label="DUI",
            border_radius=10,
            prefix_icon=ft.Icons.PERSON,
            on_change=self.formatear_dui,
            col={"xs": 6, "md": 4},
        )
        self.txt_nrc = ft.TextField(
            label="NRC",
            border_radius=10,
            prefix_icon=ft.Icons.CONFIRMATION_NUMBER,
            on_change=self.formatear_nrc,
            col={"xs": 6, "md": 4},
        )
        self.ddl_tamaño_contribuyente = ft.Dropdown(
            label="Tamaño Contribuyente",
            col={"xs": 12, "sm": 6},
            options=[
                ft.dropdown.Option("1", "Pequeño"),
                ft.dropdown.Option("2", "Mediano"),
                ft.dropdown.Option("3", "Grande"),
                ft.dropdown.Option("4", "Fiscalización o Agente de Percepción"),
                ft.dropdown.Option("5", "Retención No Inscritos al IVA 13%"),
            ]
        )
        self.txt_actividad = ft.TextField(
            label="Actividad Económica",
            border_radius=10,
            prefix_icon=ft.Icons.WORK,
            col={"xs": 12, "sm": 6},
        )
        self.txt_telefono = ft.TextField(
            label="Teléfono",
            border_radius=10,
            prefix_icon=ft.Icons.PHONE,
            on_change=self.formatear_telefono,
            col={"xs": 12, "sm": 6},
        )
        self.txt_correo = ft.TextField(
            label="Correo Electrónico",
            border_radius=10,
            prefix_icon=ft.Icons.EMAIL,
            col={"xs": 12, "sm": 6},
        )
        self.txt_direccion = ft.TextField(
            label="Dirección",
            border_radius=10,
            prefix_icon=ft.Icons.LOCATION_ON,
            col={"xs": 12},
        )

    # --- formateadores (idénticos a los que ya tenías, solo con self) ---
    def formatear_nit(self, e):
        numeros = "".join(filter(str.isdigit, e.control.value))[:14]
        resultado = ""
        if len(numeros) > 0:
            resultado += numeros[:4]
        if len(numeros) > 4:
            resultado += "-" + numeros[4:10]
        if len(numeros) > 10:
            resultado += "-" + numeros[10:13]
        if len(numeros) > 13:
            resultado += "-" + numeros[13:14]
        if e.control.value != resultado:
            e.control.value = resultado
            e.page.update()

    def formatear_dui(self, e):
        numeros = "".join(filter(str.isdigit, e.control.value))[:9]
        resultado = ""
        if len(numeros) > 0:
            resultado += numeros[:8]
        if len(numeros) > 8:
            resultado += "-" + numeros[8:9]
        e.control.value = resultado
        e.control.update()

    def formatear_nrc(self, e):
        valor = e.control.value
        valor = "".join(c for c in valor if c.isdigit() or c == "-")
        partes = valor.split("-")
        if len(partes) > 2:
            valor = partes[0] + "-" + "".join(partes[1:])
        e.control.value = valor
        e.control.update()

    def formatear_telefono(self, e):
        numeros = "".join(filter(str.isdigit, e.control.value))[:8]
        resultado = ""
        if len(numeros) > 0:
            resultado += numeros[:4]
        if len(numeros) > 4:
            resultado += "-" + numeros[4:8]
        e.control.value = resultado
        e.control.update()

    def limpiar(self):
        self.txt_nombre_comercial.value = ""
        self.txt_razon_social.value = ""
        self.txt_nit.value = ""
        self.txt_dui.value = ""
        self.txt_nrc.value = ""
        self.ddl_tamaño_contribuyente.value = ""
        self.txt_actividad.value = ""
        self.txt_telefono.value = ""
        self.txt_correo.value = ""
        self.txt_direccion.value = ""

    def cargar_emisor(self, emisor):
        self.txt_nombre_comercial.value = emisor[2]
        self.txt_razon_social.value = emisor[3]
        self.txt_nit.value = emisor[4]
        self.txt_dui.value = emisor[5]
        self.txt_nrc.value = emisor[6]
        self.ddl_tamaño_contribuyente.value = str(emisor[7])
        self.txt_actividad.value = emisor[8]
        self.txt_telefono.value = emisor[9]
        self.txt_correo.value = emisor[10]
        self.txt_direccion.value = emisor[11]

    def construir_campos(self):
        """Retorna la lista plana de campos para usar dentro de un ResponsiveRow."""
        return [
            self.txt_nombre_comercial,
            self.txt_razon_social,
            self.txt_nit,
            self.txt_dui,
            self.txt_nrc,
            self.ddl_tamaño_contribuyente,
            self.txt_actividad,
            self.txt_telefono,
            self.txt_correo,
            self.txt_direccion,
        ]

    def construir_formulario(self):
        return ft.Column(
            [
                # ---------------- INFORMACIÓN GENERAL ----------------
                ft.Row(
                    [
                        ft.Icon(ft.Icons.BUSINESS, color=ft.Colors.BLUE),
                        ft.Text(
                            "Información General",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ]
                ),
                ft.Divider(),

                ft.ResponsiveRow(
                    [
                        self.txt_nombre_comercial,
                        self.txt_razon_social,
                        self.txt_nit,
                        self.txt_dui,
                        self.txt_nrc,
                    ],
                    spacing=15,
                    run_spacing=15,
                ),

                ft.Container(height=10),

                # ---------------- INFORMACIÓN TRIBUTARIA ----------------
                ft.Row(
                    [
                        ft.Icon(ft.Icons.DESCRIPTION_OUTLINED,
                                color=ft.Colors.BLUE),
                        ft.Text(
                            "Información Tributaria",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ]
                ),
                ft.Divider(),

                ft.ResponsiveRow(
                    [
                        self.ddl_tamaño_contribuyente,
                        self.txt_actividad,
                    ],
                    spacing=15,
                    run_spacing=15,
                ),

                ft.Container(height=10),

                # ---------------- CONTACTO ----------------
                ft.Row(
                    [
                        ft.Icon(ft.Icons.CONTACT_PHONE_OUTLINED,
                                color=ft.Colors.BLUE),
                        ft.Text(
                            "Información de Contacto",
                            size=18,
                            weight=ft.FontWeight.BOLD,
                        ),
                    ]
                ),
                ft.Divider(),

                ft.ResponsiveRow(
                    [
                        self.txt_telefono,
                        self.txt_correo,
                        self.txt_direccion,
                    ],
                    spacing=15,
                    run_spacing=15,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=5,
        )