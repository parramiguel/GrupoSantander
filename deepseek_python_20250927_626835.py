import matplotlib.pyplot as plt
import pandas as pd
import io

# Datos CSV de ejemplo
csv_data = """x,y
1,3.2
2,5.1
3,7.8
4,10.2
5,12.5
6,15.1
7,17.8
8,20.3
9,22.9
10,25.4"""

# Leer los datos
df = pd.read_csv(io.StringIO(csv_data))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['x'], df['y'], 'ro-', linewidth=2, markersize=8)
plt.title('Gráfico de X vs Y')
plt.xlabel('Valores X')
plt.ylabel('Valores Y')
plt.grid(True)
plt.show()