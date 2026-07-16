from models.usuario import Usuario

def crear_admin():

    if Usuario.existe_usuario("admin"):
        return

    Usuario.guardar(
        usuario="admin",
        contraseña="admin123",
        nombre="Administrador",
        rol="Administrador"
    )
