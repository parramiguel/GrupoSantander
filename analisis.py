import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 

# Generar datos aleatorios
np.random.seed(42)
x = np.arange(1, 101)
y = 2*x + 3 + np.random.normal(0, 5, 100)

# Crear DataFrame y guardar como CSV
df = pd.DataFrame({'x': x, 'y': y})
df.to_csv('mi_dataset.csv', index=False)
# Genera una gráfica de dispersión de una columna vs. la otra 
plt.scatter(df['x'], df['y'])
plt.show()
# Genera una gráfica de dispersión de una columna vs. la otra 
plt.scatter(df['x'], df['y'])
plt.show()
# Genera una gráfica de dispersión de una columna vs. la otra 
plt.scatter(df['x'], df['y'])
plt.show()
