# Crea una ventana de Tkinter con un menú Archivo que tenga opciones Abrir y Guardar
import tkinter as tk
from tkinter import filedialog, messagebox

class VentanaConMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana con Menú Archivo")
        self.root.geometry("600x400")

        self.crear_menu()

    def crear_menu(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo) 

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            self.texto.delete(1.0, tk.END)      
            self.texto.insert(1.0, contenido)   

    def guardar_archivo(self):      
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if archivo:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(self.texto.get(1.0, tk.END))        
                self.root.title(f"Ventana con Menú Archivo - {archivo}")        
                messagebox.showinfo("Éxito", f"Archivo guardado: {archivo}")    

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()

    def ejecutar(self):
        self.root.mainloop()    

if __name__ == "__main__":
    app = VentanaConMenu()
    app.ejecutar()  
    messagebox.showinfo("Información", "Ventana creada con éxito")
    print("Ventana creada con éxito")   
    