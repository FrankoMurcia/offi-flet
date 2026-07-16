import hashlib


def encriptar(contraseña):

    return hashlib.sha256(
        contraseña.encode()
    ).hexdigest()


def verificar(contraseña, hash_guardado):

    return encriptar(contraseña) == hash_guardado