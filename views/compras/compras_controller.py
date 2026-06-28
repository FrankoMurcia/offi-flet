from views.compras.state import ComprasState
from views.compras.control_factory import crear_controles

class ComprasController:

    def __init__(self, page, abrir_proveedor):
        self.page = page
        self.abrir_proveedor = abrir_proveedor

        self.state = ComprasState()
        self.controls = None

    def crear_controles(self, sugerencias):

        self.controls = crear_controles(
            self.page,
            self.state,
            sugerencias
        )
