from aDecorar import decorar
import json

#Función de gestión principal
def gestion():
    from bMenu import menu
    mostrar_menuG = True

    while True:
        if mostrar_menuG:
            decorar()
            print("""
            \t
            - 1) Gestión de Productos -
            \t
                            Menú                    
            \t
            a) - Ingresar producto
            b) - Modificar producto
            c) - Eliminar producto
            d) - Volver al Menú Prinpipal
            """)
            decorar()
            print("\t") 

        opcion = input("Estimado usuario, por favor ingrese una opción: ").lower()
        print("\t")

        if opcion == 'a':
            print("a) - Ingresar productos")
            mostrar_menuG = False  
            agregar()
            break
        elif opcion == 'b':
            print("b) - Modificar producto")
            mostrar_menuG = False  
            modificar()
            break
        elif opcion == 'c':
            print("c) - Eliminar producto")
            mostrar_menuG = False  
            eliminar()
            break
        elif opcion == 'd':
            menu()
            break
        else:
            print("\t")
            print("\t")
            print("Opción inválida, por favor, ingrese una opción válida...")
            print("-"*80)
            mostrar_menuG = True  
        print("\t")
#gestion()

# Función para cargar los productos desde un archivo JSON
def cargar_productos():
    try:
        with open('productos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Función para respaldar los productos en un archivo JSON
def respaldo_json(datos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

#Diccionario de los productos
#productos = {}

# Cargar los productos existentes desde el archivo JSON
#productos = cargar_productos()

# Funcion para agregar productos
def agregar():
    # Cargar los productos existentes desde el archivo JSON
    productos = cargar_productos()
    while True:
        print("\t")
        print("Agregar Nuevo Producto: ")
        print("\t")
        codigo = input("Código: ")

        if codigo in productos:
            print("\t")
            print("\t")
            print("Disculpe ! El código de producto ya existe...")
            print("-"*80)
            print("\t")
            continue
        
        nombre = input("Nombre: ")
        categoria = input("Categoria: ")

        while True:
            try:
                precio = float(input("Precio: "))
                break
            except ValueError:
                print("- El precio debe ser un valor númerico -")

        while True:
            try:
                cantidad = int(input("Cantidad: "))
                break
            except ValueError:
                print("- La cantidad debe ser un valor númerico -")

        while True:
                origen = input("Nacional (N) o Importado (I): ").upper()
                if origen == 'N' or origen == 'I':
                    break
                else:
                    print("- El origen debe ser 'N' (Nacional) o 'I' (Importado) -")
                    
        producto = {
            'codigo': codigo,
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'cantidad': cantidad,
            'origen': origen
        }
        #Agregar el producto al diccionario
        productos[codigo] = producto
        respaldo_json(productos, 'productos.json')
        print("\t")
        print("Producto agregado exitosamente !!!")
        print("-"*80)
        print("\t")
        print("\t")

        while True:
            otro_producto = input("Desea agregar otro producto (S/N): ").lower()
            if otro_producto == 's':
                agregar()
            elif otro_producto == 'n':
                gestion()
            else:
                print("\t")
                print("- Por favor, ingrese 'S' para agregar otro producto o 'N' para finalizar -")
                print("\t")

        #Mostrar los productos agregados
        print("\t")
        print("\t")
        print("Productos :")
        for codigo, producto in productos.items():
            print("\t")
            print(f"Codigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Origen: {producto['origen']}")      
            print("--------------------")
            print("\t")
        gestion()
#agregar()

# Funcion para modificar productos       
def modificar():
    # Cargar los productos existentes desde el archivo JSON
    productos = cargar_productos()
    while True:
        print("\t")
        print("Modificar Producto: ")
        print("-"*80)
        print("\t")
        codigo = input("Por favor, ingrese el código del producto que desea modificar: ")
        if codigo in productos:
            producto = productos[codigo]
            print("\t")
            print("El producto existe: ")
            print("\t")
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Origen: {producto['origen']}")

            print("\t")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_categoria = input("Ingrese la nueva categoria: ")

            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    break
                except ValueError:
                    print("- El precio debe ser un valor númerico -")

            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    break
                except ValueError:
                    print("- La cantidad debe ser un valor númerico -")

            while True:
                nuevo_origen = input("Nacional (N) o Importado (I): ").upper()
                if nuevo_origen == 'N' or nuevo_origen == 'I':
                    break
                else:
                    print("- El origen debe ser 'N' (Nacional) o 'I' (Importado) -")
                    
            print("\t")

            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre

            if nueva_categoria:
                producto['categoria'] = nueva_categoria

            if nuevo_precio:
                producto['precio'] = float(nuevo_precio)

            if nueva_cantidad:
                producto['cantidad'] = int(nueva_cantidad)

            if nuevo_origen:
                producto['origen'] = (nuevo_origen)

            #Agregar el producto al diccionario
            productos[codigo] = producto
            respaldo_json(productos, 'productos.json')
            print("\t")
            print("\t")
            print("El producto se modificó exitosamente !!! ")
            print("-"*80)
            print("\t")
        
        else:
            print("\t")
            print("\t")
            print("No se encontro ningún producto con ese codigo... ")
            print("-"*80)
            print("\t")

        while True:
            otro_producto = input("Desea modificar otro producto (S/N): ").lower()
            if otro_producto == 's':
                modificar()
            elif otro_producto == 'n':
                gestion()
            else:
                print("\t")
                print("- Por favor, ingrese 'S' para agregar otro producto o 'N' para finalizar -")
                print("\t")

        # Mostrar los productos agregados
        print("\t")
        print("\t")
        print("Productos :")
        for codigo, producto in productos.items():
            print("\t")
            print(f"Codigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Origen: {producto['origen']}")      
            print("--------------------")
            print("\t")
        gestion()
#modificar()

# Funcion para eliminar productos
def eliminar():
    # Cargar los productos existentes desde el archivo JSON
    productos = cargar_productos()  
    while True:      
        print("\t")
        codigo = input("Ingrese el codigo que desea eliminar: ")
        print("\t")

        if codigo in productos:
            producto = productos[codigo]
            print("Confirmación:")
            print(f"Va a eliminar el producto:")
            print("\t")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Origen: {producto['origen']}")
            print("\t")

            while True:
                confirmacion = input("Usted esta seguro de eliminar el producto (S/N): ").lower()
                if confirmacion == 's':
                    del productos[codigo]
                    respaldo_json(productos, 'productos.json')
                    print("\t")
                    print("\t")
                    print("El producto se eliminó exitosamente !!!")
                    print("-"*80)
                    print("\t")
                    break
                elif confirmacion == 'n':
                    print("\t")
                    print("\t")
                    print("Cancelado, El producto no se eliminará...")
                    print("-"*80)
                    print("\t")
                    break
                else:
                    print("\t")
                    print("\t")
                    print("- Por favor, ingrese 'S' para confirmar la eliminación o 'N' para cancelar -")
                    print("\t")

        else:
            print("\t")
            print("\t")
            print("No se encontro ningún producto con ese código... ")
            print("-"*80)
            print("\t")

        while True:
            otro_producto = input("Desea eliminar otro producto (S/N): ").lower()
            if otro_producto == 's':
                eliminar()
            elif otro_producto == 'n':
                gestion()
            else:
                print("\t")
                print("- Por favor, ingrese 'S' para eliminar otro producto o 'N' para finalizar -")
                print("\t")

        # Mostrar los productos agregados
        print("\t")
        print("\t")
        print("Productos :")
        for codigo, producto in productos.items():
            print("\t")
            print(f"Codigo: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Origen: {producto['origen']}")      
            print("--------------------")
            print("\t")
        gestion()
#eliminar()