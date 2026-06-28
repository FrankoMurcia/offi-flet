from database.conexion import conectar

class Producto:

    @staticmethod
    def guardar(nombre, cantidad, precio):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO producto(nombre,cantidad,precio)
        VALUES(?,?,?)
        """,(nombre,cantidad,precio))

        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM producto")

        datos = cursor.fetchall()

        conn.close()

        return datos

    @staticmethod
    def editar(id_producto, nombre, cantidad, precio):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE producto
        SET nombre=?,
            cantidad=?,
            precio=?
        WHERE id=?
        """,(nombre,cantidad,precio,id_producto))

        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id_producto):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM producto WHERE id=?",
            (id_producto,)
        )

        conn.commit()
        conn.close()