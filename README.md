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
