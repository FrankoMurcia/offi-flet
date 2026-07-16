from models.usuario import Usuario


def guardar_usuario(state, controls):

    Usuario.guardar(
        controls.txt_usuario.value,
        controls.txt_contraseña.value,
        controls.txt_nombre.value,
        controls.dd_rol.value
    )

def editar_usuario(state, controls):

    Usuario.editar(

        state.id_edicion,

        controls.txt_usuario.value,

        controls.txt_contraseña.value,

        controls.txt_nombre.value,

        controls.dd_rol.value

    )

def guardar_o_editar(state, controls):

    if state.id_edicion is None:

        guardar_usuario(state, controls)

    else:

        editar_usuario(state, controls)

def eliminar_usuario(id_usuario):

    Usuario.eliminar(id_usuario)