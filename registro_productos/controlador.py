from model import Producto
from vista import registroVista

class RegistroController:
    def __init__(self):
        self.productos = []
        self.vista = registroVista(self)

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                nombre, cantidad, precio = self.vista.obtener_datos_producto()
                self.agregar_producto()

            elif opcion == '2':
                self.mostrar_productos()
            elif opcion == '3':
                self.vista.mostrar_mensaje("Saliendo del programa.")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente nuevamente.")