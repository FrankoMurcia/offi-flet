from models.usuario import Usuario


def iniciar_sesion(usuario, contraseña):

    return Usuario.autenticar(
        usuario,
        contraseña
    )