import flet as ft

def crear_date_picker(page, controls):

    def fecha_seleccionada(e):
        if e.control.value:
            controls.txt_fecha.value = e.control.value.strftime("%d-%m-%Y")
            page.update()

    def abrir_calendario(e):
        date_picker.open = True
        page.update()

    date_picker = ft.DatePicker(on_change=fecha_seleccionada)
    page.overlay.append(date_picker)

    btn_fecha = ft.IconButton(
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=abrir_calendario
    )

    return btn_fecha