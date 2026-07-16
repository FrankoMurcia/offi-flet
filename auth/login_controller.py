from auth.login_service import iniciar_sesion


class LoginController:

    def login(self, usuario, contraseña):

        return iniciar_sesion(
            usuario,
            contraseña
        )