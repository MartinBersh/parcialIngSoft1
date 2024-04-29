class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al carrito.")

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print(f"Producto {producto.nombre} eliminado del carrito.")
        else:
            print("El producto no está en el carrito.")
