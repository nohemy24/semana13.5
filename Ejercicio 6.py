import random

# Crear el archivo con palabras aleatorias
palabras = ["Python", "código", "archivo", "programación", "datos", "texto", "inteligencia", "computadora", "software", "desarrollo"]
contenidoinicial = " ".join(random.choices(palabras, k=100))  # Genera 100 palabras aleatorias

with open("documento.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenidoinicial)

print("Archivo 'documento.txt' creado con palabras aleatorias.")

# Búsqueda y reemplazo de palabra
palabraoriginal = input("Palabra a buscar: ")
palabranueva = input("Palabra nueva: ")

with open("documento.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read().replace(palabraoriginal, palabranueva)

with open("modificado.txt", "w", encoding="utf-8") as archivo_modificado:
    archivo_modificado.write(contenido)

print("Reemplazo completado. Se ha creado 'modificado.txt' con los cambios.")