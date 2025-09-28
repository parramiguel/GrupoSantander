import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generar_datos_ventas_sinteticos(num_registros=1000, fecha_inicio='2023-01-01', fecha_fin='2024-12-31'):
    """
    Genera datos sintéticos de ventas con las columnas: fecha, producto, cantidad, precio
    
    Args:
        num_registros (int): Número de registros a generar
        fecha_inicio (str): Fecha de inicio en formato 'YYYY-MM-DD'
        fecha_fin (str): Fecha de fin en formato 'YYYY-MM-DD'
    
    Returns:
        pd.DataFrame: DataFrame con los datos de ventas generados
    """
    
    # Lista de productos con sus precios base
    productos = {
        'Laptop HP': 850.00,
        'Mouse Logitech': 25.50,
        'Teclado Mecánico': 89.99,
        'Monitor Samsung 24"': 199.99,
        'Auriculares Sony': 79.99,
        'Tablet iPad': 329.00,
        'Smartphone iPhone': 699.00,
        'Cámara Canon': 450.00,
        'Impresora Epson': 129.99,
        'Disco Duro 1TB': 65.00,
        'Memoria RAM 8GB': 45.99,
        'Tarjeta Gráfica RTX': 299.99,
        'Router WiFi': 89.99,
        'Cable HDMI': 12.99,
        'Webcam Logitech': 49.99,
        'Altavoces JBL': 99.99,
        'Micrófono Blue Yeti': 129.99,
        'Lámpara LED': 34.99,
        'Silla Gaming': 199.99,
        'Mesa Escritorio': 149.99
    }
    
    # Convertir fechas a datetime
    fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
    
    # Generar datos aleatorios
    datos = []
    
    for i in range(num_registros):
        # Generar fecha aleatoria
        dias_diferencia = (fecha_fin_dt - fecha_inicio_dt).days
        dias_aleatorios = random.randint(0, dias_diferencia)
        fecha = fecha_inicio_dt + timedelta(days=dias_aleatorios)
        
        # Seleccionar producto aleatorio
        producto = random.choice(list(productos.keys()))
        precio_base = productos[producto]
        
        # Generar cantidad (1-10 unidades)
        cantidad = random.randint(1, 10)
        
        # Calcular precio total con pequeñas variaciones
        variacion_precio = random.uniform(0.9, 1.1)  # ±10% de variación
        precio_total = round(precio_base * cantidad * variacion_precio, 2)
        
        datos.append({
            'fecha': fecha.strftime('%Y-%m-%d'),
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio_total
        })
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    # Ordenar por fecha
    df['fecha'] = pd.to_datetime(df['fecha'])
    df = df.sort_values('fecha').reset_index(drop=True)
    df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
    
    return df

def main():
    """Función principal para generar y guardar los datos"""
    
    print("Generando datos sintéticos de ventas...")
    
    # Generar datos
    df_ventas = generar_datos_ventas_sinteticos(
        num_registros=2000,  # 2000 registros
        fecha_inicio='2023-01-01',
        fecha_fin='2024-12-31'
    )
    
    # Mostrar información básica
    print(f"\nDatos generados: {len(df_ventas)} registros")
    print(f"Período: {df_ventas['fecha'].min()} a {df_ventas['fecha'].max()}")
    print(f"Productos únicos: {df_ventas['producto'].nunique()}")
    print(f"Ventas totales: ${df_ventas['precio'].sum():,.2f}")
    
    # Mostrar muestra de los datos
    print("\nPrimeras 10 filas:")
    print(df_ventas.head(10))
    
    # Guardar en CSV
    nombre_archivo = 'datos_ventas_sinteticos.csv'
    df_ventas.to_csv(nombre_archivo, index=False, encoding='utf-8')
    print(f"\nDatos guardados en: {nombre_archivo}")
    
    # Mostrar estadísticas por producto
    print("\nEstadísticas por producto:")
    stats_producto = df_ventas.groupby('producto').agg({
        'cantidad': ['count', 'sum'],
        'precio': ['sum', 'mean']
    }).round(2)
    stats_producto.columns = ['Ventas', 'Cantidad_Total', 'Ingresos_Total', 'Precio_Promedio']
    print(stats_producto)

if __name__ == "__main__":
    main()
