import os 
#Se importa el modulo os para usar la funcion: os.path.exists(ruta)
ARCHIVO="estudiantes.txt"


def cargar_estudiantes():
    estudiantes=[]
    #La funcion os.path.exists() verifica si el archivo o carpeta existe en una ruta determinada 
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                #Linea.strip() Elimina espacios y saltos de linea (\n) al principio o al final 
                #split(",") Divide la cadena en una lista usando la coma como separador
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for estudiante in estudiantes:
            linea = f"{estudiante['codigo']},{estudiante['nombre']},{estudiante['apellido']},{estudiante['carrera']}\n"
            archivo.write(linea)
            
def crear_estudiante(estudiantes):
    codigo = input("Ingrese el código del estudiante: ")
    # Verificar si el código ya existe
    #La funcion any() devuelve True si al menos un elemento del iterable es verdadero.
    if any(estudiante["codigo"] == codigo for estudiante in estudiantes):
        print("El código ya existe\n")
        return
    
    
nombre = input("Nombre: ")
apellido = input("Apellido: ")
carrera = input("Carrera: ")

estudiantes.append({
     "codigo": codigo,
     "nombre": nombre,
     "apellido": apellido,
     "carrera": carrera
})
guardar_estudiantes(estudiantes)
print("Estudiante creado exitosamente.\n")
 
 
def listar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    
    print("Lista de estudiantes:")
    for estudiante in estudiantes:
        print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Carrera: {estudiante['carrera']}")
    print()  
    

def actualizar_estudiante(estudiantes):
    codigo = input("Ingrese el código del estudiante a actualizar: ")
    for estudiante in estudiantes:
        if estudiante["codigo"] == codigo:
            estudiante["nombre"] = input("Nuevo nombre: ")
            estudiante["apellido"] = input("Nuevo apellido: ")
            estudiante["carrera"] = input("Nueva carrera: ")
            guardar_estudiantes(estudiantes)
            print("Estudiante actualizado exitosamente.\n")
            return
    print("Código no encontrado.\n")
    
    
def eliminar_estudiante(estudiantes):
    codigo = input("Ingrese el código del estudiante a eliminar: ")
    for i, estudiante in enumerate(estudiantes):
        if estudiante["codigo"] == codigo:
            del estudiantes[i]
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado exitosamente.\n")
            return
    print("Código no encontrado.\n")
    
    
# Función principal del menú
def menu():
    estudiantes = cargar_estudiantes()
    
    while True:
        print("1. Crear estudiante")
        print("2. Listar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            listar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
        
#Instrucción para ejecutar el menú
menu()
# Fin del código
