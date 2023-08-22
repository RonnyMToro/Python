from aDecorar import decorar

decorar()
print("""
\t
     - Sistema de Gestión de Stock -
\t
                    Bienvenido                    
\t
 """)
print("Trabajo Final Integrador")
print("Estudiante: Ronny Toro")
print("\t")
decorar()

print("""
\t
     - Creación de usuario -                    
\t
 """)
print("-"*80)

usuarios = {}

#Función para crear el usuario
def crear_usuario():
    while True:
        print("\t")
        print("\t")
        print("Estimado usuario, por favor...")
        print("\t")
        nombre = input("Ingrese su Usuario: ")
        contrasena = input("Ingrese su Contraseña: ")

        if not nombre or not contrasena:
            print("\t")
            print("\t")
            print("Estimado usuario, el usuario y contraseña no pueden estar vacios...")
            print("-"*80)
            print("\t")
            continue

        usuarios[nombre] = contrasena

        print("\t")
        print("\t")
        print("Estimado usuario, a creado su usuario y contraseña exitosamente !!!")
        print("-"*80)
        print("\t")
        break

    if not usuarios:
        print("\t")
        print("\t")
        print("Usted, no ha creado aun el usuario ni contraseña...")
        print("-"*80)
        print("\t")
        return
#crear_usuario()

#Función de login
def login():
    from bMenu import menu

    if not usuarios:
        print("\t")
        print("\t")
        print("Usted, no ha creado aun el usuario ni contraseña...")
        print("-"*80)
        print("\t")
        return

    while True:
        print("\t")
        print("\t")
        print("Por favor, para ingresar el sistema...")
        print("\t")
        nombre = input("Ingrese su Usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if nombre in usuarios and usuarios[nombre] == contrasena:
            print("\t")
            print("\t")
            print("-"*80)
            print("Estimado usuario, login exitoso... Bienvenido !!!")
            print("-"*80)
            print("\t")
            menu()
            break
        else:
            print("\t")
            print("\t")
            print("Estimado usuario, usted a ingresado un usuario o/y contraseña incorrecto...")
            print("-"*80)
            print("\t")
#login()