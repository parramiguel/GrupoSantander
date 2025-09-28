<<<<<<< HEAD
# Proyectos Python - Grupo Santander

Este repositorio contiene una colección de proyectos y ejercicios de programación en Python desarrollados como parte del Grupo Santander.

## 📁 Contenido del Proyecto

### 🧮 Calculadoras
- **CalculadoraBasica.py** - Calculadora básica con operaciones fundamentales
- **AplicacionCalculadora-SegundoRenglon (2).py** - Aplicación de calculadora con interfaz mejorada

### 🎯 Ejercicios de Programación
- **FizzBuzz.py** - Implementación clásica del juego FizzBuzz
- **Factorial.py** - Cálculo de factorial de un número
- **Primo.py** - Verificación de números primos
- **CuadradoNro.py** - Cálculo del cuadrado de un número
- **HolaMundo.py** - Programa básico "Hola Mundo"

### 📊 Análisis de Datos
- **analisis.py** - Scripts de análisis de datos
- **deepseek_python_20250927_626835.py** - Análisis con DeepSeek
- **mi_dataset.csv** - Dataset para análisis

### 📝 Contador de Palabras
- **contador_palabras/** - Directorio con herramientas para contar palabras
  - `contador.py` - Script principal del contador
  - `test_permisos.py` - Pruebas de permisos
  - `archivo.txt` y `prueba.txt` - Archivos de ejemplo

## 🚀 Cómo usar

### Requisitos
- Python 3.7 o superior
- Librerías: pandas, numpy (para análisis de datos)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/parramiguel/GrupoSantander.git
cd GrupoSantander

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install pandas numpy
```

### Ejecución
```bash
# Ejecutar cualquier script
python FizzBuzz.py
python CalculadoraBasica.py
python Factorial.py
```

## 📋 Ejemplos de Uso

### FizzBuzz
```python
python FizzBuzz.py
# Imprime números del 1 al 100, reemplazando:
# - Múltiplos de 3 con "Fizz"
# - Múltiplos de 5 con "Buzz"  
# - Múltiplos de ambos con "FizzBuzz"
```

### Calculadora
```python
python CalculadoraBasica.py
# Interfaz de calculadora con operaciones básicas
```

### Análisis de Datos
```python
python analisis.py
# Ejecuta análisis sobre el dataset
```

## 🛠️ Estructura del Proyecto

```
GrupoSantander/
├── README.md
├── .gitignore
├── CalculadoraBasica.py
├── AplicacionCalculadora-SegundoRenglon (2).py
├── FizzBuzz.py
├── Factorial.py
├── Primo.py
├── CuadradoNro.py
├── HolaMundo.py
├── analisis.py
├── mi_dataset.csv
├── contador_palabras/
│   ├── contador.py
│   ├── test_permisos.py
│   ├── archivo.txt
│   └── prueba.txt
└── venv/ (excluido del control de versiones)
```

## 📈 Características

- ✅ Código limpio y bien documentado
- ✅ Ejercicios de programación clásicos
- ✅ Herramientas de análisis de datos
- ✅ Aplicaciones interactivas
- ✅ Entornos virtuales configurados
- ✅ Control de versiones con Git

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es parte del Grupo Santander y está disponible para fines educativos.

## 👥 Autor

**parramiguel** - [GitHub](https://github.com/parramiguel)

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella al repositorio!
=======
# Gestor de Tareas

Una aplicación web simple para gestionar tareas personales, desarrollada con Flask y Python.

## Características

- ✅ Agregar nuevas tareas
- ✅ Marcar tareas como completadas
- ✅ Persistencia de datos en archivo JSON
- ✅ Interfaz web moderna y responsive
- ✅ Contador de tareas (total, completadas, pendientes)

## Tecnologías utilizadas

- **Backend**: Python 3.11, Flask
- **Frontend**: HTML5, CSS3, Jinja2
- **Persistencia**: JSON
- **Estilo**: CSS moderno con gradientes y animaciones

## Instalación y uso

### Requisitos previos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos para ejecutar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/gestor-tareas.git
   cd gestor-tareas
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install flask
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   - Ve a: `http://localhost:5000`

## Estructura del proyecto

```
gestor_tareas/
├── app.py              # Aplicación principal Flask
├── templates/          # Plantillas HTML
│   ├── base.html       # Plantilla base
│   └── index.html      # Página principal
├── tareas.json         # Archivo de persistencia (se crea automáticamente)
├── .gitignore          # Archivos ignorados por Git
└── README.md           # Este archivo
```

## Funcionalidades

### Agregar tarea
- Escribe el texto de la tarea en el formulario
- Haz clic en "Agregar Tarea"
- La tarea se guarda automáticamente en `tareas.json`

### Completar tarea
- Haz clic en el botón "✓ Completar" junto a cualquier tarea pendiente
- La tarea se marcará como completada visualmente
- El estado se guarda automáticamente

### Persistencia
- Todas las tareas se guardan en `tareas.json`
- Los datos se cargan automáticamente al iniciar la aplicación
- El contador de ID se mantiene entre sesiones

## Desarrollo

### Estructura de datos
```json
{
  "tareas": [
    {
      "id": 1,
      "texto": "Tarea de ejemplo",
      "completada": false
    }
  ],
  "contador_id": 2
}
```

### Funciones principales
- `agregar_tarea(texto)`: Agrega una nueva tarea
- `completar_tarea(id)`: Marca una tarea como completada
- `cargar_tareas()`: Carga tareas desde JSON
- `guardar_tareas()`: Guarda tareas en JSON

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Autor

**Miguel Parra**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
>>>>>>> a7393a600782416798cf3cb598046292fd1bc2bf
