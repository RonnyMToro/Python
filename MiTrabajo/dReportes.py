from aDecorar import decorar
import json

# Funcion de reportes proincipal
def reportes():
    from bMenu import menu
    mostrar_menuR = True

    while True:
        if mostrar_menuR:
            decorar()
            print("""
            \t
            - 2) Gestión de Reportes -
            \t
                            Menú                    
            \t
            a) - Reporte de Productos por Categoría
            b) - Reporte de Productos por Origen (Nacional o Importado)
            c) - Volver al Menú Prinpipal
            """)
            decorar()
            print("\t") 

        opcion = input("Estimado usuario, por favor ingrese una opción: ").lower()
        print("\t")

        if opcion == 'a':
            print("a) - Reporte de Productos por Categoría")
            mostrar_menuR = False  
            PorCategoria()
            break
        elif opcion == 'b':
            print("b) - Reporte de Productos por Origen")
            mostrar_menuR = False  
            PorOrigen()
            break
        elif opcion == 'c':
            menu()
            break
        else:
            print("\t")
            print("\t")
            print("Opción inválida, por favor, ingrese una opción válida...")
            print("-"*80)
            mostrar_menuR = True 
        print("\t")
#Gestion()

def respaldo_json(datos, nombre_archivo):
    with open(nombre_archivo,'w') as archivo:
        json.dump(datos, archivo)

# Funcion de reporte por categoria
def PorCategoria():
    from cGestion import cargar_productos
    while True:
        productos = cargar_productos()
        print("\t")
        categoria = input("Ingrese la categoria: ")
        print("\t")
        print("Reporte de Productos por Categoría:")
        print("\t")

        productos_categoria = [producto for producto in productos.values() if producto['categoria'].lower() == categoria.lower()]

        if  productos_categoria:
            print("\t")
            print("Productos por categoria...")
            print("\t")
            
            for producto in productos_categoria:
                print(f"Categoría: {producto['categoria']}")
                print(f"Código: {producto['codigo']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
                print(f"Origen: {producto['origen']}")
                print("--------------------")
                print("\t")
            
            respaldo_json(productos_categoria, 'respaldo_catogoria.json')

        else:
            print("\t")
            print("\t")
            print("No se encontro ningún producto con esa categoría... ")
            print("-"*80)
            print("\t")

        otra_categoria = input("Desea generar otro reporte por categoría (S/N): ").lower()
        if otra_categoria == 's':
            PorCategoria()
        elif otra_categoria == 'n':
            reportes()
        else:
            print("\t")
            print("- Por favor, ingrese 'S' para eliminar otro producto o 'N' para finalizar -")
            print("\t")
#PorCategoria()

# Funcion de reporte por origen
def PorOrigen():
    from cGestion import cargar_productos
    while True:
        productos = cargar_productos()
        print("\t")
        origen = input("Ingrese el origen Nacional o Importado (N/I): ").lower()
        print("\t")
        print("Reporte de Productos Nacionales :")
        print("\t")

        origen = [producto for producto in productos.values() if producto['origen'].lower() == origen]

        if  origen:
            print("\t")
            print(f"Reporte de Productos por Origen :...")
            print("\t")
            
            for producto in origen:
                print(f"Origen: {producto['origen']}")
                print(f"Código: {producto['codigo']}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Precio: {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
                print("--------------------")
                print("\t")

            respaldo_json(origen, 'respaldo_origen.json')

        else:
            print("\t")
            print("\t")
            print("No se encontro ningún producto con ese codigo... ")
            print("-"*80)
            print("\t")

        otro_reporte = input("Desea generar otro reporte por origen (S/N): ").lower()
        if otro_reporte == 's':
            PorOrigen
        elif otro_reporte == 'n':
            reportes()
        else:
            print("\t")
            print("- Por favor, ingrese 'S' para eliminar otro producto o 'N' para finalizar -")
            print("\t")
#PorOrigen()