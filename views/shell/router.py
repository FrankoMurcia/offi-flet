from views.dashboard import dashboard
#from views.emisor2 import vista_emisor
from views.compras.vista import vista_compras
from views.usuarios.view import vista_usuarios
from views.emisor.vista_emisor import vista_emisor
from auth import session


def cambiar_vista(indice, contenido, page, rail):

    def abrir_proveedor():

        rail.selected_index = 1

        contenido.content = vista_emisor(page)

        page.update()

    usuario = session.obtener()

    es_admin = (
        usuario is not None
        and usuario[4] == "Administrador"
    )

    if indice == 0:

        contenido.content = dashboard()

    elif indice == 1:

        contenido.content = vista_emisor(page)

    elif indice == 2:

        contenido.content = vista_compras(

            page,

            abrir_proveedor

        )

    elif indice == 3:

        if es_admin:

            contenido.content = vista_usuarios(page)

        else:

            rail.selected_index = 0

            contenido.content = dashboard()