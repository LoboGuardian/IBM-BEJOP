class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

        # Validaciones
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0")

    # Getters y setters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__precio = nuevo_precio

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0")
        self.__cantidad = nueva_cantidad

class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if producto in self.__productos:
            raise ValueError("El producto ya existe en el inventario")
        self.__productos.append(producto)

    def actualizar_producto(self, nombre, nuevo_precio, nueva_cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre:
                producto.precio = nuevo_precio
                producto.cantidad = nueva_cantidad
                return
        raise ValueError("Producto no encontrado")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.nombre == nombre:
                self.__productos.remove(producto)
                return
        raise ValueError("Producto no encontrado")

    def mostrar_inventario(self):
        for producto in self.__productos:
            print(f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.nombre == nombre:
                return producto
        return None

# Ejemplo de uso
if __name__ == "__main__":
    producto1 = Producto("Manzana", "Frutas", 1.5, 10)
    producto2 = Producto("Banana", "Frutas", 1.2, 20)

    inventario = Inventario()
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    inventario.mostrar_inventario()
    inventario.actualizar_producto("Manzana", 2.0, 15)
    inventario.mostrar_inventario()
