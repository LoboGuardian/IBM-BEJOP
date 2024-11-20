Explicación:

    Clases: Se definen las clases Producto e Inventario según el enunciado.
    Atributos: Los atributos son privados y se accede a ellos mediante getters y setters.
    Validaciones: Se realizan validaciones en los setters para garantizar que los precios y cantidades sean válidos.
    Métodos: Se implementan los métodos para agregar, actualizar, eliminar, mostrar y buscar productos.
    Ejemplo de uso: Se muestra un ejemplo básico de cómo utilizar las clases.

Puntos clave:

    Encapsulación: Los atributos son privados para proteger la integridad de los datos.
    Validación: Se incluyen validaciones para evitar errores comunes.
    Manejo de excepciones: Se utilizan excepciones para indicar errores como producto no encontrado o valores inválidos.
    Legibilidad: El código está bien estructurado y comentado para facilitar la comprensión.

Ampliaciones posibles:

    Persistencia de datos: Guardar el inventario en un archivo o base de datos.
    Interfaz de usuario: Crear una interfaz gráfica o de línea de comandos más amigable.
    Informes: Generar reportes sobre el inventario (productos más vendidos, stock bajo, etc.).
    Categorías: Implementar una jerarquía de categorías para los productos.

<!-- Main V1 -->

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


<!-- Main V2 -->

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
        return f"Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


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


<!-- Main V3 -->

import json
import logging

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
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio
    
    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

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
            with open(self.archivo, 'r') as f:
                productos_data = json.load(f)
                self.__productos = [Producto.from_dict(data) for data in productos_data]
            logging.info("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            logging.warning("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            logging.error("Error al decodificar el archivo JSON. No se puede cargar el inventario.")
    
    def guardar_inventario(self):
        """Guarda los productos en el archivo JSON."""
        with open(self.archivo, 'w') as f:
            json.dump([producto.to_dict() for producto in self.__productos], f, indent=4)
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
    
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                logging.info("Producto encontrado: %s", nombre)
                return
        logging.warning("Producto no encontrado: %s", nombre)
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

<!-- main v3 -->

Para añadir un sistema de log y una pseudo base de datos utilizando JSON, vamos a modificar el código anterior de varias maneras. Estableceremos un sistema de logging para registrar las acciones realizadas en el inventario y utilizaremos un archivo JSON para almacenar y recuperar los productos.

A continuación, te muestro el código actualizado:

```python
import json
import logging

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
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio
    
    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

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
            with open(self.archivo, 'r') as f:
                productos_data = json.load(f)
                self.__productos = [Producto.from_dict(data) for data in productos_data]
            logging.info("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            logging.warning("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            logging.error("Error al decodificar el archivo JSON. No se puede cargar el inventario.")
    
    def guardar_inventario(self):
        """Guarda los productos en el archivo JSON."""
        with open(self.archivo, 'w') as f:
            json.dump([producto.to_dict() for producto in self.__productos], f, indent=4)
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
    
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                logging.info("Producto encontrado: %s", nombre)
                return
        logging.warning("Producto no encontrado: %s", nombre)
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
```

### Descripción de las Modificaciones:

1. **Logging**:
   - Se ha configurado el logging en el archivo `inventario.log` para registrar acciones importantes, como adiciones, actualizaciones, eliminaciones y errores.
   - Se utilizan diferentes niveles de logging (`INFO`, `WARNING`, y `ERROR`) para identificar la gravedad de cada mensaje.

2. **Gestión de Archivos JSON**:
   - Se han añadido métodos para guardar (`guardar_inventario`) y cargar (`cargar_inventario`) el inventario desde un archivo JSON llamado `inventario.json`.
   - `to_dict` y `from_dict` en la clase `Producto` se utilizan para convertir objetos a diccionarios y viceversa, facilitando la serialización y deserialización en JSON.

3. **Manejo de Errores**:
   - Se gestionan errores al intentar cargar el archivo JSON (archivo no encontrado o error de decodificación).

### Ejemplo de Uso:
El código inicializamos `Inventario`, creamos productos y demostramos cómo agregar, mostrar, actualizar, buscar y eliminar productos, además de que esto queda registrado en el archivo de log y en el archivo JSON.

Puedes ejecutar este código y ver cómo se comporta. Necesitarás tener permisos de escritura para crear el archivo JSON y el archivo de log en el directorio donde esté ubicado tu script. Si tienes dudas o necesitas más funcionalidades, ¡hazmelo saber! 

<!--  -->

<!-- Gemini  -->

Análisis del Código y Solución al Problema

Problema:

El código proporcionado define una clase Producto y una clase Inventario para gestionar un inventario de productos. Sin embargo, la función mostrar_producto no está implementada correctamente para mostrar la información detallada de un producto específico.

Análisis:

    Falta de implementación: La función mostrar_producto está definida pero su cuerpo está vacío.
    Lógica necesaria: Para mostrar un producto, se debe buscar el producto en el inventario por su nombre y luego imprimir sus detalles.

Solución:
Python

def mostrar_producto(self, nombre):
    for producto in self.__productos:
        if producto.get_nombre() == nombre:
            print(producto)
            return
    print(f"Producto '{nombre}' no encontrado.")

Use code with caution.

Explicación:

    Iteración: Recorre la lista de productos en el inventario.
    Comparación: Compara el nombre del producto buscado con el nombre de cada producto en la lista.
    Impresión: Si se encuentra el producto, imprime sus detalles utilizando el método __str__ de la clase Producto.
    No encontrado: Si no se encuentra el producto, imprime un mensaje indicando que no existe.

Código Completo con la Solución:
Python

# ... (resto del código)

class Inventario:
    # ... (resto de los métodos)

    def mostrar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(producto)
                return
        print(f"Producto '{nombre}' no encontrado.")

# ... (resto del código)

Use code with caution.

Ejemplo de Uso:
Python

# ... (resto del código)

# Mostrar el producto "Mouse"
inventario.mostrar_producto("Mouse")

Use code with caution.

Consideraciones Adicionales:

    Optimización: Si el inventario es muy grande, se podría considerar implementar una estructura de datos más eficiente para buscar productos por nombre, como un diccionario.
    Formateado: Se puede personalizar la forma en que se muestran los detalles del producto utilizando f-strings o el método format de los strings.
    Manejo de errores: Se podría agregar un manejo de errores más robusto para casos como nombres de productos inválidos o errores al cargar el inventario.

Respuesta al Prompt:

Para mostrar el producto "Mouse" en el código proporcionado, debes agregar la siguiente función a la clase Inventario:
Python

def mostrar_producto(self, nombre):
    # ... (código explicado anteriormente)

Use code with caution.

Esta función buscará el producto en el inventario por su nombre y lo mostrará si lo encuentra. Si no encuentra el producto, mostrará un mensaje indicando que no existe.

Ejemplo de uso:
Python

inventario.mostrar_producto("Mouse")

Use code with caution.

Al ejecutar este código, se imprimirá la información del producto "Mouse" si existe en el inventario.

Con esta solución, la función mostrar_producto funciona correctamente y proporciona la funcionalidad solicitada en el prompt.

¿Deseas realizar alguna otra consulta sobre este código o tienes alguna otra pregunta?


<!-- AWA -->

Que actividad debo hacer de acuerdo al pdf adjunto

Ejercicio+Fin...

De acuerdo al PDF titulado "Ejercicio Final - Curso iniciación a Python", debes desarrollar una aplicación en Python destinada a la gestión de un inventario de productos, aplicando la programación orientada a objetos (POO). A continuación, te detallo las actividades que debes realizar, basándome en los requisitos y el enunciado proporcionados en el documento:

Actividades a Realizar:
Implementación de Clases:

Crea una clase llamada Producto con los siguientes atributos:
nombre: Nombre del producto.
categoria: Categoría del producto.
precio: Precio del producto (debe ser mayor que 0).
cantidad: Cantidad en stock (debe ser mayor o igual a 0).
Asegúrate de que todos los atributos sean privados y utiliza getters y setters para acceder y modificar los valores.
Clase Inventario:

Crea una segunda clase llamada Inventario, que maneje una lista de objetos de la clase Producto. Esta clase debe permitir las siguientes operaciones:
Agregar un producto: Verifica que el producto no exista previamente en el inventario antes de añadirlo.
Actualizar un producto: Modifica el precio o la cantidad en stock de un producto existente.
Eliminar un producto: Permite quitar un producto del inventario.
Mostrar inventario: Lista todos los productos disponibles.
Buscar un producto: Permite buscar un producto por su nombre.
Validaciones:

Asegúrate de implementar validaciones para:
Que el precio siempre sea mayor a 0.
Que la cantidad sea mayor o igual a 0.
Manejo adecuado de excepciones y validación de entradas, para evitar que el usuario ingrese datos no válidos.
Estructura y Comentarios:

Organiza tu código para que sea legible y modular. Cada funcionalidad debe estar en un método de la clase correspondiente.
Comenta tu código para explicar la funcionalidad y el propósito de cada sección.
Requisitos de Entrega:

El archivo final deberás entregarlo como un script en Python que contenga las clases Producto e Inventario correctamente implementadas, según las pautas dadas.
Consejos:
Es recomendable probar cada funcionalidad a medida que la desarrollas para asegurarte de que todo funcione como se espera.
Si necesitas ayuda sobre POO en Python, hay numerosos recursos y tutoriales disponibles que pueden orientarte.
Con estas indicaciones, estarás bien encaminado para completar tu ejercicio final. ¡Buena suerte!

Pudieras generarlo en Python? por favor


Claro, puedo ayudarte a generar un código en Python que implemente las clases Producto e Inventario según los requisitos establecidos en el ejercicio final. A continuación, te muestro un ejemplo básico que cumple con todos los requisitos mencionados:

python

Copy
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
        return f"Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"


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
Descripción del Código:
Clase Producto: Representa un producto con atributos privados y métodos para acceder y modificar esos atributos. Incluye validaciones en los setters.
Clase Inventario: Maneja una lista de productos e incluye métodos para agregar, actualizar, eliminar, mostrar y buscar productos.
Ejemplo de Uso: Un bloque if __name__ == "__main__": que crea instancias de productos y muestra cómo usar las funcionalidades de la clase Inventario.
Puedes copiar este código e ejecutarlo en tu entorno de desarrollo de Python. Asegúrate de probar cada funcionalidad para verificar que funcione según lo esperado. Si necesitas hacer ajustes o tienes más preguntas, ¡no dudes en preguntar!

Añadir un log, y una pseudo base de datos con json o algo parecido


Para añadir un sistema de log y una pseudo base de datos utilizando JSON, vamos a modificar el código anterior de varias maneras. Estableceremos un sistema de logging para registrar las acciones realizadas en el inventario y utilizaremos un archivo JSON para almacenar y recuperar los productos.

A continuación, te muestro el código actualizado:

python

Copy
import json
import logging

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
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio
    
    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

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
            with open(self.archivo, 'r') as f:
                productos_data = json.load(f)
                self.__productos = [Producto.from_dict(data) for data in productos_data]
            logging.info("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            logging.warning("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            logging.error("Error al decodificar el archivo JSON. No se puede cargar el inventario.")
    
    def guardar_inventario(self):
        """Guarda los productos en el archivo JSON."""
        with open(self.archivo, 'w') as f:
            json.dump([producto.to_dict() for producto in self.__productos], f, indent=4)
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
    
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                logging.info("Producto encontrado: %s", nombre)
                return
        logging.warning("Producto no encontrado: %s", nombre)
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
Descripción de las Modificaciones:
Logging:

Se ha configurado el logging en el archivo inventario.log para registrar acciones importantes, como adiciones, actualizaciones, eliminaciones y errores.
Se utilizan diferentes niveles de logging (INFO, WARNING, y ERROR) para identificar la gravedad de cada mensaje.
Gestión de Archivos JSON:

Se han añadido métodos para guardar (guardar_inventario) y cargar (cargar_inventario) el inventario desde un archivo JSON llamado inventario.json.
to_dict y from_dict en la clase Producto se utilizan para convertir objetos a diccionarios y viceversa, facilitando la serialización y deserialización en JSON.
Manejo de Errores:

Se gestionan errores al intentar cargar el archivo JSON (archivo no encontrado o error de decodificación).
Ejemplo de Uso:
El código inicializamos Inventario, creamos productos y demostramos cómo agregar, mostrar, actualizar, buscar y eliminar productos, además de que esto queda registrado en el archivo de log y en el archivo JSON.

Puedes ejecutar este código y ver cómo se comporta. Necesitarás tener permisos de escritura para crear el archivo JSON y el archivo de log en el directorio donde esté ubicado tu script. Si tienes dudas o necesitas más funcionalidades, ¡hazmelo saber!

Inventario json aparece asi [

text

Copy
{

    "nombre": "Laptop",

    "categoria": "Electr\u00f3nica",

    "precio": 850.0,

    "cantidad": 4

}
] como arregla el electronica


El carácter Unicode \u00e9 representa una "e" acentuada (é) en JSON. Cuando este formato JSON se imprime, algunas aplicaciones o visualizadores traducen automáticamente estos caracteres Unicode a su forma legible. Sin embargo, si deseas que el JSON se guarde directamente con caracteres legibles evitando estos caracteres Unicode, puedes modificar el método que guarda el archivo JSON.

Para hacer esto, puedes utilizar el parámetro ensure_ascii=False al llamar a json.dump(). Esta modificación permitirá que los caracteres no ASCII, tales como "é", se guarden como son en lugar de su representación Unicode.

Aquí está el código actualizado en el método guardar_inventario dentro de la clase Inventario:

python

Copy
def guardar_inventario(self):
    """Guarda los productos en el archivo JSON."""
    with open(self.archivo, 'w', encoding='utf-8') as f:
        json.dump([producto.to_dict() for producto in self.__productos], f, indent=4, ensure_ascii=False)
    logging.info("Inventario guardado en el archivo.")
Explicación del Cambio:
ensure_ascii=False: Este parámetro asegura que los caracteres se guarden como están, permitiendo que caracteres como "é", "á", etc., se guarden en su forma legible en el archivo JSON, en lugar de convertidos a su representación Unicode.

encoding='utf-8': Asegura que el archivo se abra con codificación UTF-8, que es compatible con la mayoría de los caracteres en idiomas que usan acentos.

Ejemplo Completo Actualizado:
Aquí tienes la implementación completa de la clase Inventario, con la modificación para guardar el JSON sin Unicode:

python

Copy
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
Usar el Código
Con estas modificaciones, cuando guardes tu inventario en el archivo inventario.json, los caracteres acentuados deberán aparecer correctamente, así:

json

Copy
[
    {
        "nombre": "Laptop",
        "categoria": "Electrónica",
        "precio": 850.0,
        "cantidad": 4
    }
]
Esto hará que trabajar con el JSON sea más intuitivo, especialmente si necesitas leer el contenido manualmente. Si necesitas más ayuda o tienes más consultas, ¡no dudes en preguntar!

Agregar mas productos # Crear algunos productos

text

Copy
producto1 = Producto("Laptop", "Electrónica", 900.00, 5)

producto2 = Producto("Mouse", "Accesorios", 25.00, 15)

Claro, aquí tienes el código completo que incluye la creación de más productos. He añadido varios productos adicionales de diferentes categorías. Esto ofrece un mejor ejemplo de cómo se puede utilizar la clase Inventario para manejar un conjunto diverso de productos.

Código Completo Actualizado
python

Copy
import json
import logging

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
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio
    
    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

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
    
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print(f"Producto encontrado: {producto}")
                logging.info("Producto encontrado: %s", nombre)
                return
        logging.warning("Producto no encontrado: %s", nombre)
        print("Producto no encontrado.")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

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
Explicación de los Productos Agregados
En este código:

productos adicionales: He creado cinco productos diferentes:
Teclado
Monitor
Impresora
Smartphone
Cargador
Tablet
Esto te proporciona un inventario más representativo con varios artículos en diferentes categorías.

Ejemplo de Salida
Cuando ejecutes el programa, el inventario se mostrará en la consola y se guardará en el archivo JSON. Aquí está un ejemplo simplificado de cómo se verá la salida en la consola después de mostrar el inventario:

text

Copy
Nombre: Laptop, Categoría: Electrónica, Precio: 900.0, Cantidad: 5
Nombre: Mouse, Categoría: Accesorios, Precio: 25.0, Cantidad: 15
Nombre: Teclado, Categoría: Accesorios, Precio: 50.0, Cantidad: 10
Nombre: Monitor, Categoría: Electrónica, Precio: 300.0, Cantidad: 7
Nombre: Impresora, Categoría: Oficina, Precio: 120.0, Cantidad: 3
Nombre: Smartphone, Categoría: Electrónica, Precio: 600.0, Cantidad: 8
Nombre: Cargador, Categoría: Accesorios, Precio: 20.0, Cantidad: 12
Nombre: Tablet, Categoría: Electrónica, Precio: 350.0, Cantidad: 6
Las operaciones de actualización, búsqueda y eliminación también se procesarán de acuerdo con estas adiciones.

Si tienes más preguntas o necesitas otra funcionalidad, ¡hazmelo saber!