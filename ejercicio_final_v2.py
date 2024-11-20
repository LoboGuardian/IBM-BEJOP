#!/bin/env python
# -*-coding:UTF-8-*-
# main.py

import json
import logging
import os

def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def pausar():
    input("Presione cualquier tecla para continuar...")

# Configuración del logging
logging.basicConfig(level=logging.INFO, filename='inventario.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
        # if precio <= 0:
            # raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio

    def set_cantidad(self, cantidad):
        # if cantidad < 0:
            # raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

    '''
    def __str__(self):
        return (
            f"Nombre: {self.__nombre},\n"
            f"Categoría: {self.__categoria},\n"
            f"Precio: {self.__precio},\n"
            f"Cantidad: {self.__cantidad},\n"
        )

    '''

    def to_dict(self):
        """Convierte el objeto a un diccionario para facilitar el uso con JSON."""
        return {
            'nombre': self.__nombre,
            'categoria': self.__categoria,
            'precio': self.__precio,
            'cantidad': self.__cantidad
        }

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto desde un diccionario."""
        return Producto(data['nombre'], data['categoria'], data['precio'], data['cantidad'])

    def __str__(self):
        return f"Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.__productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo JSON."""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                productos_data = json.load(f)
                self.__productos = [Producto.from_dict(data) for data in productos_data]
            logging.info("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            logging.warning("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            logging.error("Error al decodificar el archivo JSON. No se puede cargar el inventario.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo JSON."""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump([producto.to_dict() for producto in self.__productos], f, indent=4, ensure_ascii=False)
        logging.info("Inventario guardado en el archivo.")
    
    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            logging.warning("El producto ya existe en el inventario: %s", producto.get_nombre())
            print("El producto ya existe en el inventario.")
        else:
            self.__productos.append(producto)
            self.guardar_inventario()
            logging.info("Producto agregado: %s", producto.get_nombre())
            print("Producto agregado exitosamente.")

        if not producto.get_nombre():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if producto.get_precio() <= 0:
            raise ValueError("El precio debe ser un número positivo, mayor que 0.")
        # if producto.get_cantidad() < 0:
            # raise ValueError("La cantidad debe ser mayor o igual a 0.")
        if not isinstance(producto.get_cantidad(), int) or producto.get_cantidad() < 0:
            raise ValueError("La cantidad debe ser un número entero positivo o cero.")
    
    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                self.guardar_inventario()
                logging.info("Producto actualizado: %s", producto.get_nombre())
                print("Producto actualizado exitosamente.")
                return
        logging.warning("Producto no encontrado para actualización: %s", nombre)
        print("Producto no encontrado.")
    
    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                self.guardar_inventario()
                logging.info("Producto eliminado: %s", nombre)
                print("Producto eliminado exitosamente.")
                return
        logging.warning("Producto no encontrado para eliminación: %s", nombre)
        print("Producto no encontrado.")
    
    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
            logging.info("Se intentó mostrar el inventario, pero está vacío.")
        else:
            for producto in self.__productos:
                print(producto)
            logging.info("Inventario mostrado exitosamente.")

    def mostrar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(producto)
                return
        print(f"Producto '{nombre}' no encontrado.")
    
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                logging.info("Producto encontrado: %s", nombre)
                return
        logging.warning("Producto no encontrado: %s", nombre)
        print("Producto no encontrado.")

def mostrar_menu():
    print("Menú de opciones:")
    print("1. Mostrar inventario completo")
    print("2. Buscar producto")
    print("3. Agregar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")

def menu_principal():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            limpiar_pantalla()
            inventario.mostrar_inventario()

        elif opcion == '2':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        
        elif opcion == '3':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría: ")
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
            nuevo_producto = Producto(nombre, categoria, precio, cantidad)
            inventario.agregar_producto(nuevo_producto)
            # print("Producto agregado exitosamente.")
        
        elif opcion == '4':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nuevo_precio = float(input("Ingrese el nuevo precio (deje en blanco si no desea cambiar): "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad (deje en blanco si no desea cambiar): "))
            inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)
        
        elif opcion == '5':
            limpiar_pantalla()
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        
        elif opcion == '6':
            limpiar_pantalla()
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

        pausar()
        limpiar_pantalla()

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    menu_principal()
    
    '''
    # Crear algunos productos
    producto1 = Producto("Laptop", "Electrónica", 900.00, 5)
    producto2 = Producto("Mouse", "Accesorios", 25.00, 15)
    producto3 = Producto("Teclado", "Accesorios", 50.00, 10)
    producto4 = Producto("Monitor", "Electrónica", 300.00, 7)
    producto5 = Producto("Impresora", "Oficina", 120.00, 3)
    producto6 = Producto("Smartphone", "Electrónica", 600.00, 8)
    producto7 = Producto("Cargador", "Accesorios", 20.00, 12)
    producto8 = Producto("Tablet", "Electrónica", 350.00, 6)

    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)
    inventario.agregar_producto(producto4)
    inventario.agregar_producto(producto5)
    inventario.agregar_producto(producto6)
    inventario.agregar_producto(producto7)
    inventario.agregar_producto(producto8)

    pausar()
    limpiar_pantalla()

    # Mostrar inventario
    inventario.mostrar_inventario()

    pausar()
    limpiar_pantalla()

    # Actualizar un producto
    inventario.actualizar_producto("Laptop", nuevo_precio=850.00, nueva_cantidad=4)

    pausar()
    limpiar_pantalla()

    # Buscar un producto
    inventario.buscar_producto("Mouse")

    pausar()
    limpiar_pantalla()

    # Mostrar un producto
    inventario.mostrar_producto("Mouse")

    pausar()
    limpiar_pantalla()

    # Eliminar un producto
    inventario.eliminar_producto("Mouse")

    pausar()
    limpiar_pantalla()

    # Mostrar inventario de nuevo
    inventario.mostrar_inventario()

    pausar()
    limpiar_pantalla()
    '''


# Implementar exportacion a csv
'''
import csv

def exportar_a_csv(self):
    with open('inventario.csv', 'w', newline='') as csvfile:
        fieldnames = ['Nombre', 'Categoría', 'Precio', 'Cantidad']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for producto in self.__productos:
            writer.writerow(producto.to_dict())
'''

# Añadir interfaz grafica
# Tkinter o PyQt
# O tal vez una web

# Sustituir el json por SQLite o PostgreSQL

# Evitar duplicados
