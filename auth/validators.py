def validar(usuario, contraseña):

    if usuario.strip() == "":

        return False, "Ingrese el usuario."

    if contraseña.strip() == "":

        return False, "Ingrese la contraseña."

    return True, ""