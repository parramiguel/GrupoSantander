import tkinter as tk
from tkinter import filedialog, messagebox

class VentanaConMenu:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Ventana con Menú Archivo")
        self.root.geometry("600x400")
        
        # Variable para almacenar el contenido del archivo
        self.contenido_archivo = ""
        self.archivo_actual = None
        
        # Crear el área de texto
        self.texto = tk.Text(self.root, wrap=tk.WORD, padx=10, pady=10)
        self.texto.pack(fill=tk.BOTH, expand=True)
        
        # Crear la barra de menú
        self.crear_menu()
        
    def crear_menu(self):
        """Crear la barra de menú con las opciones Archivo"""
        # Crear la barra de menú principal
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)
        
        # Crear el menú Archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        
        # Agregar opciones al menú Archivo
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo, accelerator="Ctrl+O")
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo, accelerator="Ctrl+S")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir, accelerator="Ctrl+Q")
        
        # Configurar atajos de teclado
        self.root.bind('<Control-o>', lambda e: self.abrir_archivo())
        self.root.bind('<Control-s>', lambda e: self.guardar_archivo())
        self.root.bind('<Control-q>', lambda e: self.salir())
        
    def abrir_archivo(self):
        """Función para abrir un archivo"""
        try:
            # Abrir el diálogo para seleccionar archivo
            archivo = filedialog.askopenfilename(
                title="Abrir archivo",
                filetypes=[
                    ("Archivos de texto", "*.txt"),
                    ("Archivos Python", "*.py"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            if archivo:
                # Leer el contenido del archivo
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                
                # Mostrar el contenido en el área de texto
                self.texto.delete(1.0, tk.END)
                self.texto.insert(1.0, contenido)
                
                # Guardar la ruta del archivo actual
                self.archivo_actual = archivo
                self.root.title(f"Ventana con Menú Archivo - {archivo}")
                
                messagebox.showinfo("Éxito", f"Archivo abierto: {archivo}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo: {str(e)}")
    
    def guardar_archivo(self):
        """Función para guardar un archivo"""
        try:
            # Obtener el contenido del área de texto
            contenido = self.texto.get(1.0, tk.END)
            
            # Si ya hay un archivo abierto, guardar en el mismo
            if self.archivo_actual:
                with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                messagebox.showinfo("Éxito", f"Archivo guardado: {self.archivo_actual}")
            else:
                # Si no hay archivo abierto, pedir dónde guardar
                archivo = filedialog.asksaveasfilename(
                    title="Guardar archivo",
                    defaultextension=".txt",
                    filetypes=[
                        ("Archivos de texto", "*.txt"),
                        ("Archivos Python", "*.py"),
                        ("Todos los archivos", "*.*")
                    ]
                )
                
                if archivo:
                    with open(archivo, 'w', encoding='utf-8') as f:
                        f.write(contenido)
                    
                    self.archivo_actual = archivo
                    self.root.title(f"Ventana con Menú Archivo - {archivo}")
                    messagebox.showinfo("Éxito", f"Archivo guardado: {archivo}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")
    
    def salir(self):
        """Función para salir de la aplicación"""
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()
    
    def ejecutar(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaConMenu()
    app.ejecutar()

