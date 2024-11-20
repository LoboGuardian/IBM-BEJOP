#!/bin/env python
# -*-coding:UTF-8-*-
# main.py

class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters
    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

    def __str__(self):
        return (
            f"Nombre: {self.__nombre},\n"
            f"Categoría: {self.__categoria},\n"
            f"Precio: {self.__precio},\n"
            f"Cantidad: {self.__cantidad},\n"
        )


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            print("El producto ya existe en el inventario.")
        else:
            self.__productos.append(producto)
            print("Producto agregado exitosamente.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                print("Producto actualizado exitosamente.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                return
        print("Producto no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Crear algunos productos
    producto1 = Producto("Laptop", "Electrónica", 900.00, 5)
    producto2 = Producto("Mouse", "Accesorios", 25.00, 15)

    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    # Mostrar inventario
    inventario.mostrar_inventario()

    # Actualizar un producto
    inventario.actualizar_producto("Laptop", nuevo_precio=850.00, nueva_cantidad=4)

    # Buscar un producto
    inventario.buscar_producto("Mouse")

    # Eliminar un producto
    inventario.eliminar_producto("Mouse")

    # Mostrar inventario de nuevo
    inventario.mostrar_inventario()
