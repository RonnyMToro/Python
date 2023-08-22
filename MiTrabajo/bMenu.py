from aDecorar import decorar
import sys

#Función del menú principal
def menu():
    from aLogin import login
    from cGestion import gestion
    from dReportes import reportes
    mostrar_menu = True 

    while True:
        if mostrar_menu:
            decorar()
            print("""
            \t
            - Sistema de Gestión de Stock -
            \t
                        Menú Principal                   
            \t
            1) - Gestión de Productos
            2) - Gestión de Reportes
            0) - Salir
            """)
            decorar()

        print("\t") 
        opcion = input("Estimado usuario, por favor ingrese una opción: ")
        print("\t")

        if opcion == '1':
            #print("1) - Gestión de productos")
            mostrar_menu = False 
            gestion()
            break
        elif opcion == '2':
            print("2) - Gestión de reportes")
            mostrar_menu = False  
            reportes()
            break
        elif opcion == '0':
            print("\t")
            print("Hasta luego, salio del programa...")
            print("-"*80)
            print("\t")
            sys.exit()
        else:
            print("\t")
            print("\t")
            print("Opción inválida, por favor, ingrese una opción válida...")
            print("-"*80)
            mostrar_menu = True
        print("\t")
#Menu()