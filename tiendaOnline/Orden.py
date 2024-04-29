class Orden:
    def __init__(self, usuario, productos):
        self.usuario = usuario
        self.productos = productos

    def mostrar_detalle(self):
        print(f"Orden para: {self.usuario.nombre}")
        print("Productos en la orden:")
        for producto in self.productos:
            producto.mostrar_info()