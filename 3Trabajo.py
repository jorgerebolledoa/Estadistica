import numpy as np
from scipy import stats

# Datos proporcionados
n1 = 300  # Tamaño de la muestra de la máquina 1
n2 = 300  # Tamaño de la muestra de la máquina 2
defectuosos1 = 15  # Número de defectuosos en la máquina 1
defectuosos2 = 8   # Número de defectuosos en la máquina 2
alpha = 0.02  # Nivel de significación

# Proporciones de defectuosos
p1 = defectuosos1 / n1
p2 = defectuosos2 / n2

# Pooled proportion
p_pool = (defectuosos1 + defectuosos2) / (n1 + n2)

# Estadístico z
z_stat = (p1 - p2) / np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))

# p-valor para una prueba de una cola (menor)
p_value = stats.norm.cdf(z_stat)

# Imprimir los resultados
print(f'Estadístico z: {z_stat:.4f}')
print(f'P-valor: {p_value:.4f}')

# Determinar si rechazamos la hipótesis nula
if p_value < alpha:
    print('Rechazamos la hipótesis nula: La proporción de piezas defectuosas producidas por la máquina 2 es significativamente menor que la producida por la máquina 1.')
else:
    print('No podemos rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que la proporción de piezas defectuosas producidas por la máquina 2 es menor que la producida por la máquina 1.')

