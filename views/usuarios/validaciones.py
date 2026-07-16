from models.usuario import Usuario

def validar_campos(controls):

    if not controls.txt_usuario.value:

        return False, "Debe ingresar un usuario."

    if not controls.txt_contraseña.value:

        return False, "Debe ingresar una contraseña."

    if not controls.txt_nombre.value:

        return False, "Debe ingresar el nombre."

    if not controls.dd_rol.value:

        return False, "Debe seleccionar un rol."

    return True, ""

def validar_usuario(state, controls):

    ok, mensaje = validar_campos(controls)

    if not ok:

        return ok, mensaje

    if state.id_edicion is None:

        if Usuario.existe_usuario(

            controls.txt_usuario.value

        ):

            return False,"Ese usuario ya existe."

    else:

        if Usuario.existe_usuario_otro(

            controls.txt_usuario.value,

            state.id_edicion

        ):

            return False,"Ese usuario ya existe."

    return True,""