#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar permisos de archivos
"""

import os
import sys

def probar_archivo(ruta):
    print(f"\n=== Probando archivo: {ruta} ===")
    print(f"Archivo existe: {os.path.exists(ruta)}")
    
    if os.path.exists(ruta):
        print(f"Es archivo: {os.path.isfile(ruta)}")
        print(f"Es directorio: {os.path.isdir(ruta)}")
        print(f"Permisos de lectura: {os.access(ruta, os.R_OK)}")
        print(f"Permisos de escritura: {os.access(ruta, os.W_OK)}")
        
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                print(f"Archivo leído exitosamente! Tamaño: {len(contenido)} caracteres")
                return True
        except PermissionError as e:
            print(f"❌ Error de permisos: {e}")
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    else:
        print("❌ El archivo no existe")
        return False

if __name__ == "__main__":
    # Probar archivos locales
    archivos_locales = ["archivo.txt", "prueba.txt"]
    
    print("Probando archivos locales...")
    for archivo in archivos_locales:
        probar_archivo(archivo)
    
    # Si se proporciona un archivo como argumento
    if len(sys.argv) > 1:
        archivo_usuario = sys.argv[1]
        print(f"\nProbando archivo del usuario: {archivo_usuario}")
        probar_archivo(archivo_usuario)
