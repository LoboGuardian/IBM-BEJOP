import json
import logging
import os
import signal


def limpiar_pantalla():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)


def pausar():
    input("Presione Enter para continuar...")


def signal_handler(sig, frame):
    limpiar_pantalla()
    print('\nSaliendo del programa...')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    filename='inventario.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero positivo o cero.")

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio': self.precio,
            'cantidad': self.cantidad
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['categoria'], data['precio'], data['cantidad'])

    def __str__(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                productos_data = json.load(f)
                self.productos = [Producto.from_dict(data) for data in productos_data]
            logging.info("Inventario cargado correctamente.")
        except FileNotFoundError:
            logging.warning("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            logging.error("Error al leer el archivo JSON. No se pudo cargar el inventario.")

    def guardar_inventario(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump([producto.to_dict() for producto in self.productos], f, indent=4, ensure_ascii=False)
        logging.info("Inventario guardado correctamente.")

    def agregar_producto(self, producto):
        if any(p.nombre == producto.nombre for p in self.productos):
            raise ValueError(f"El producto '{producto.nombre}' ya existe en el inventario.")
        self.productos.append(producto)
        self.guardar_inventario()
        logging.info("Producto agregado: %s", producto.nombre)

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        producto = self._buscar_producto_por_nombre(nombre)
        if nuevo_precio is not None:
            if nuevo_precio <= 0:
                raise ValueError("El precio debe ser mayor que 0.")
            producto.precio = nuevo_precio
        if nueva_cantidad is not None:
            if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
                raise ValueError("La cantidad debe ser un número entero positivo o cero.")
            producto.cantidad = nueva_cantidad
        self.guardar_inventario()
        logging.info("Producto actualizado: %s", nombre)

    def eliminar_producto(self, nombre):
        producto = self._buscar_producto_por_nombre(nombre)
        self.productos.remove(producto)
        self.guardar_inventario()
        logging.info("Producto eliminado: %s", nombre)

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre):
        producto = self._buscar_producto_por_nombre(nombre)
        print(f"Producto encontrado: {producto}")

    def _buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        raise ValueError(f"Producto '{nombre}' no encontrado.")

def mostrar_menu():
    opciones = [
        "Mostrar inventario completo",
        "Buscar producto",
        "Agregar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Salir"
    ]
    print("\nMenú de opciones:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")


def menu_principal():
    inventario = Inventario()
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                inventario.mostrar_inventario()
            elif opcion == '2':
                nombre = input("Ingrese el nombre del producto a buscar: ")
                inventario.buscar_producto(nombre)
            elif opcion == '3':
                nombre = input("Ingrese el nombre del producto: ")
                categoria = input("Ingrese la categoría: ")
                precio = float(input("Ingrese el precio: "))
                cantidad = int(input("Ingrese la cantidad: "))
                inventario.agregar_producto(Producto(nombre, categoria, precio, cantidad))
            elif opcion == '4':
                nombre = input("Ingrese el nombre del producto a actualizar: ")
                nuevo_precio = input("Ingrese el nuevo precio (o deje en blanco): ")
                nueva_cantidad = input("Ingrese la nueva cantidad (o deje en blanco): ")
                inventario.actualizar_producto(
                    nombre,
                    float(nuevo_precio) if nuevo_precio else None,
                    int(nueva_cantidad) if nueva_cantidad else None
                )
            elif opcion == '5':
                nombre = input("Ingrese el nombre del producto a eliminar: ")
                inventario.eliminar_producto(nombre)
            elif opcion == '6':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError as e:
            logging.error(e)
            print(f"Error: {e}")
        pausar()


if __name__ == "__main__":
    menu_principal()
