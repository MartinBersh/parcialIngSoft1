class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.productos:
            print(f"El producto {nombre} ya existe en el inventario.")
        else:
            self.productos[nombre] = cantidad
            print(f"Producto {nombre} agregado al inventario.")

    def actualizar_cantidad(self, nombre, cantidad):
        if nombre in self.productos:
            self.productos[nombre] = cantidad
            print(f"Cantidad de {nombre} actualizada en el inventario.")
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto {nombre} eliminado del inventario.")
        else:
            print(f"El producto {nombre} no existe en el inventario.")

    def generar_informe(self):
        print("Inventario:")
        for producto, cantidad in self.productos.items():
            print(f"{producto}: {cantidad}")



if __name__ == "__main__":
    inventario = Inventario()

    inventario.agregar_producto("PC", 10)
    inventario.agregar_producto("Teclado", 20)
    inventario.actualizar_cantidad("PC", 8)
    inventario.eliminar_producto("Mouse")
    inventario.eliminar_producto("Teclado")
    inventario.generar_informe()
