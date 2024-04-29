from tiendaOnline.Orden import Orden
from tiendaOnline.Usuario import Usuario
from tiendaOnline.carrito import Carrito
from tiendaOnline.producto import Producto

if __name__ == "__main__":
    laptop = Producto("Laptop", 1000, 10)
    telefono = Producto("Teléfono", 500, 20)

    carrito = Carrito()
    carrito.agregar_producto(laptop)
    carrito.agregar_producto(telefono)

    print("Productos en el carrito:")
    for producto in carrito.productos:
        producto.mostrar_info()

    usuario = Usuario("Juan", "juan@example.com")

    orden = Orden(usuario, carrito.productos)
    orden.mostrar_detalle()