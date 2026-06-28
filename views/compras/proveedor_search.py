from views.compras.calculations import calcular_totales
import flet as ft

def seleccionar_emisor(emisor, controls, sugerencias, page):

        controls.dd_emisor.value = str(emisor[0])

        controls.txt_buscar_nit.value = emisor[3] if emisor[3] else emisor[5]     # NIT

        controls.txt_nombre_emisor.value = emisor[1]   # Nombre

        sugerencias.content.controls.clear()
        sugerencias.visible = False

        calcular_totales(page, controls)

        page.update()

def actualizar_resaltado(sugerencias,state, page):

        for i, control in enumerate(
            sugerencias.content.controls
        ):

            control.bgcolor = (
                ft.Colors.BLUE_GREY_700
                if i == state.indice_seleccionado
                else None
            )

        page.update()

def navegar_sugerencias(e, state, sugerencias, controls, page):

        if not state.resultados_actuales:
            return

        if e.key == "Arrow Down":

            state.indice_seleccionado += 1

            if state.indice_seleccionado >= len(state.resultados_actuales):
                state.indice_seleccionado = 0

            actualizar_resaltado(sugerencias, state, page)

        elif e.key == "Arrow Up":

            state.indice_seleccionado -= 1

            if state.indice_seleccionado < 0:
                state.indice_seleccionado = len(state.resultados_actuales) - 1

            actualizar_resaltado(sugerencias, state, page)

        elif e.key == "Enter":

            if state.indice_seleccionado >= 0:

                seleccionar_emisor(
                    state.resultados_actuales[state.indice_seleccionado], 
                    controls, sugerencias, page
                )

def filtrar_emisor(e, state, controls, sugerencias, page):

        texto = e.control.value.strip().lower()

        state.indice_seleccionado = -1
        state.resultados_actuales = []

        sugerencias.content.controls.clear()

        if not texto:
            sugerencias.visible = False
            controls.btn_nuevo_proveedor.visible = False
            page.update()
            return

        encontrados = [
            emisor
            for emisor in state.emisores_cache

            if(
                texto in str(emisor[3]).lower() or #NIT
                texto in str(emisor[5]).lower() #NRC
            )
        ]
        state.resultados_actuales = encontrados

        if encontrados:

            for emisor in encontrados:

             sugerencias.content.controls.append(
                ft.Container(
                    content=ft.Text(f"{emisor[1]} | NIT {emisor[3]} | NRC {emisor[5]}"),

                    padding=10,
                    border_radius=5,
                    on_click= lambda e, emp=emisor: seleccionar_emisor(emp,controls, sugerencias, page)
                )
            )
            sugerencias.visible = True
            controls.btn_nuevo_proveedor.visible = False
        else:   
            sugerencias.visible = False
            controls.btn_nuevo_proveedor.visible = True
        page.update()