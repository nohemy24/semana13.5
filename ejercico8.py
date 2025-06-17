import random

def crear_archivo():
    """Genera un archivo 'libro.txt' con palabras aleatorias."""
    palabras = ["Python", "código", "archivo", "programación", "datos", "texto", "inteligencia", "computadora", "software", "desarrollo"]
    contenido = " ".join(random.choices(palabras, k=100))  # Genera 100 palabras aleatorias

    with open("libro.txt", "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

    print("Archivo 'libro.txt' creado con palabras aleatorias.")

def filtrarlineas(palabra):
    """Filtra líneas que contienen la palabra específica y las guarda en 'filtrado.txt'."""
    with open("libro.txt", "r", encoding="utf-8") as entrada, open("filtrado.txt", "w", encoding="utf-8") as salida:
        for linea in entrada:
            if palabra.lower() in linea.lower():
                salida.write(linea + "\n")

    print(f"Líneas con la palabra '{palabra}' guardadas en 'filtrado.txt'.")

# Crear el archivo con contenido inicial
crear_archivo()

# Solicitar palabra al usuario y filtrar líneas
palabraclave = input("Ingrese la palabra clave para filtrar: ")
filtrarlineas(palabraclave)