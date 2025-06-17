#Programa que lea un archivo llamado "Articulo.txt"
import random

# Crear el archivo con palabras aleatorias
palabras = ["Python", "código", "archivo", "programación", "datos", "texto", "inteligencia", "computadora", "software", "desarrollo"]
contenido = " ".join(random.choices(palabras, k=100))  # Genera 100 palabras aleatorias

with open("articulo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("Archivo 'articulo.txt' creado con contenido aleatorio.")

# Contar la palabra ingresada por el usuario
palabra = input("Ingrese la palabra a contar: ").lower()
contador = 0

with open("articulo.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        contador += linea.lower().split().count(palabra)

print(f"La palabra '{palabra}' aparece {contador} veces en el archivo.")