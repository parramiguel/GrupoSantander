from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Archivo para persistencia
ARCHIVO_TAREAS = 'tareas.json'

# Lista global de tareas
tareas = []
contador_id = 1

def cargar_tareas():
    """Carga las tareas desde el archivo JSON"""
    global tareas, contador_id
    try:
        if os.path.exists(ARCHIVO_TAREAS):
            with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                tareas = datos.get('tareas', [])
                contador_id = datos.get('contador_id', 1)
                print(f"[OK] Cargadas {len(tareas)} tareas desde {ARCHIVO_TAREAS}")
        else:
            print(f"[INFO] Archivo {ARCHIVO_TAREAS} no existe, iniciando con lista vacia")
    except Exception as e:
        print(f"[ERROR] Error al cargar tareas: {e}")
        tareas = []
        contador_id = 1

def guardar_tareas():
    """Guarda las tareas en el archivo JSON"""
    try:
        datos = {
            'tareas': tareas,
            'contador_id': contador_id
        }
        with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
        print(f"[OK] Tareas guardadas en {ARCHIVO_TAREAS}")
    except Exception as e:
        print(f"[ERROR] Error al guardar tareas: {e}")

def agregar_tarea(texto):
    """Agrega una nueva tarea a la lista global"""
    global contador_id
    tarea = {
        'id': contador_id,
        'texto': texto,
        'completada': False
    }
    tareas.append(tarea)
    contador_id += 1
    guardar_tareas()  # Guardar después de agregar
    return tarea

def completar_tarea(id):
    """Marca una tarea como completada por su ID"""
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            guardar_tareas()  # Guardar después de completar
            return tarea
    return None

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto = request.form['texto']
    agregar_tarea(texto)
    return redirect(url_for('index'))

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Cargar tareas al iniciar la aplicación
    cargar_tareas()
    app.run(debug=True)