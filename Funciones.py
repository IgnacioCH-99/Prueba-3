import csv
import Funciones

def menu():
    op = "0"
    while op != "4":
        print ("*** Menú de Gestión de Inventario ***")
        print("[1].... Agregar Producto")
        print("[2].... Leer Inventario")
        print("[3].... Clasificar y Exportar Productos")
        print("[4].... Salir")
        op = input("Seleccione una opción del 1 al 4:")

        if op == "1":
            agregar_producto()
        elif op == "2":
            leer_inventario()
        elif op == "3":
            clasificar_y_exportar()
        elif op == "4":
            print("Salir")
        else:
            print ("Opción no válida")

def agregar_producto():
    id_producto = input("Ingrese el ID del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    categoria_producto = input("Ingrese la categoría del producto (Electrónica, Textil, Calzado): ")
    precio_producto = input("Ingrese el precio del producto: ")

    with open('inventario.csv', 'a', newline='') as archivo_inventario:
        escribir = csv.writer(archivo_inventario)
        escribir.writerow([id_producto, nombre_producto, categoria_producto, precio_producto])

    print(f"Producto '{nombre_producto}' agregado al inventario.")

def leer_inventario():
    print("\nInventario Actual:")
    with open('inventario.csv', 'r', newline='') as archivo_inventario:
            leer = csv.reader(archivo_inventario)
            for producto in leer:
                print(producto)
    print("El inventario está vacío.")

def clasificar_y_exportar():
    categorias = {
        'Electrónica': [],
        'Textil': [],
        'Calzado': []
        }

    with open('inventario.csv', 'r', newline='') as archivo_inventario:
            leer = csv.reader(archivo_inventario)
            for id_producto, nombre_producto, categoria_producto, precio_producto in leer:
                if categoria_producto in categorias:
                    categorias[categoria_producto].append((id_producto, nombre_producto, precio_producto))
                else:
                    print(f"Error: Categoría '{categoria_producto}' no válida.")

    with open('clasificacion_productos.txt', 'w') as archivo_clasificacion:
            for categoria, productos in categorias.items():
                if productos:
                    archivo_clasificacion.write(f"{categoria}:\n")
                    for producto in productos:
                        archivo_clasificacion.write(f"{producto}\n")
                    archivo_clasificacion.write("\n")
            print("Clasificación de productos exportada a 'clasificacion_productos..txt'.")
