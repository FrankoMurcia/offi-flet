import flet as ft

from database.crear_tablas import crear_tablas

from auth.admin import crear_admin

from auth.login import vista_login

from views.shell.shell import crear_shell


def main(page: ft.Page):

    crear_tablas()

    crear_admin()   # <-- ESTA LÍNEA FALTA

    page.title = "Offi-Flet - Sistema de Libros Fiscales"
    
    page.window.icon = "assets/offiflet.ico"

    contenido = ft.Container(expand=True)

    page.add(contenido)

    def mostrar_login():

        contenido.content = vista_login(
            page,
            mostrar_sistema
        )

        page.update()

    def mostrar_sistema():

        contenido.content = crear_shell(page, mostrar_login)

        page.update()

    mostrar_login()


ft.run(main)