# 1. Cargar datos del CSV
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas.csv')

print(df.head())

# 2. Calcular ventas totales por mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['precio'].sum()

print(ventas_por_mes)

# 3. Determinar producto más vendido y con mayor ingresos
ventas_prod = df.groupby('producto')['precio'].sum().reset_index()
ventas_prod.columns = ['producto', 'ingreso']
ventas_prod = ventas_prod.set_index('producto')

print(ventas_prod)  

# 4. Graficar ventas por mes
# Si ventas_por_mes es index Period, convertir a str para mejor manejo
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6,4))

ventas_por_mes.plot(kind='bar')

plt.title("Ventas por Mes")

plt.xlabel("Mes")

plt.ylabel("Ventas (€)")
plt.tight_layout()

plt.savefig("ventas_por_mes.png")

plt.show()

# 5. Graficar top 5 productos por ingresos      
# print(df.groupby('producto')['precio'].sum().plot(kind='bar'))  
top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6,4))

plt.bar(top5.index, top5['ingreso'])

plt.title("Top 5 Productos por Ingresos")

plt.ylabel("Ingresos (€)")

plt.xlabel("Producto")

plt.tight_layout()

plt.savefig("top5_productos.png")

plt.show()