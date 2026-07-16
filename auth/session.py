usuario_actual = None


def iniciar(usuario):

    global usuario_actual

    usuario_actual = usuario


def cerrar():

    global usuario_actual

    usuario_actual = None


def obtener():

    return usuario_actual


def autenticado():

    return usuario_actual is not None


def id():

    if usuario_actual is None:
        return None

    return usuario_actual[0]


def nombre():

    if usuario_actual is None:
        return ""

    return usuario_actual[3]


def rol():

    if usuario_actual is None:
        return ""

    return usuario_actual[4]


def es_admin():

    return rol() == "Administrador"