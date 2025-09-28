# Programa para contar palabras en un archivo de texto
# 1. Pedir al usuario la ruta de un archivo de texto.
# 2. Leer el contenido del archivo.
# 3. Separar en palabras.
# 4. Contar número total de palabras.
# 5. (Opcional) Mostrar las 10 palabras más frecuentes y su conteo.

# 1. Pedir al usuario la ruta de un archivo de texto.
ruta_archivo = input("Ingrese la ruta del archivo de texto: ")

# 2. Leer el contenido del archivo con manejo de errores detallado
import os

print(f"Intentando leer: {ruta_archivo}")
print(f"Archivo existe: {os.path.exists(ruta_archivo)}")

if os.path.exists(ruta_archivo):
    print(f"Es archivo: {os.path.isfile(ruta_archivo)}")
    print(f"Permisos de lectura: {os.access(ruta_archivo, os.R_OK)}")

try:
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    print("Archivo leído exitosamente!")
except FileNotFoundError:
    print("El archivo no existe. Por favor, ingrese una ruta válida.")
    exit()
except PermissionError as e:
    print(f"Error de permisos: {e}")
    print("Posibles soluciones:")
    print("1. Verificar que el archivo no esté abierto en otro programa")
    print("2. Ejecutar el programa como administrador")
    print("3. Verificar permisos del archivo (clic derecho → Propiedades → Seguridad)")
    print("4. Usar un archivo en una ubicación diferente")
    exit()
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    exit()

# Separar el contenido en palabras

import re

palabras = re.findall(r"\w+", contenido.lower())

total_palabras = len(palabras)

print(f"Total palabras: {total_palabras}")  

