import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

# Datos proporcionados
sedimentos_lago = np.array([2.4, 1.8, 3.1, 2.4, 1.5, 2.2, 2.7, 3.8, 1.9, 2.8, 1.7, 3.2, 2.1, 3.5])
sedimentos_planta = np.array([120, 70, 270, 121, 54, 100, 200, 300, 79, 215, 64, 285, 92, 250])

# Parte a) Análisis de correlación
correlacion, p_value_corr = stats.pearsonr(sedimentos_lago, sedimentos_planta)
print(f'Coeficiente de correlación de Pearson: {correlacion:.4f}')
print(f'P-valor de la correlación: {p_value_corr:.4f}')

# Gráfico de dispersión
plt.scatter(sedimentos_planta, sedimentos_lago)
plt.xlabel('Sedimentos desechados por la planta (ppm)')
plt.ylabel('Sedimentos hallados en el lago (ppm)')
plt.title('Gráfico de dispersión de sedimentos')
plt.show()

# Parte b) Modelo de regresión lineal
X = sm.add_constant(sedimentos_planta)  # Agregar término constante para la intercepción
modelo = sm.OLS(sedimentos_lago, X).fit()

# Coeficientes estimados
print(modelo.summary())

# Parte c) Tabla ANOVA
anova_table = sm.stats.anova_lm(modelo, typ=2)
print(anova_table)

# Parte d) Prueba de significancia de los parámetros
print(f"P-valor para el coeficiente de pendiente: {modelo.pvalues[1]:.4f}")
print(f"P-valor para la intersección: {modelo.pvalues[0]:.4f}")

# Parte e) Conclusiones
if modelo.pvalues[1] < 0.05:
    print("El coeficiente de pendiente es significativo, lo que sugiere una relación entre los sedimentos desechados por la planta y los encontrados en el lago.")
else:
    print("El coeficiente de pendiente no es significativo, por lo que no se puede establecer una relación clara entre los sedimentos desechados por la planta y los encontrados en el lago.")
