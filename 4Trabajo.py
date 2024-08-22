import numpy as np
import pandas as pd
import statsmodels.api as sm

# Ejemplo de datos (reemplaza estos datos con los datos reales)
# Número de vuelos
vuelos = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50] * 10)  # Reemplazar con datos reales
# Ingreso en dólares
ingreso = np.array([30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000] * 10)  # Reemplazar con datos reales

# Crear DataFrame
data = pd.DataFrame({'Vuelos': vuelos, 'Ingreso': ingreso})

# Parte a) Modelo de regresión lineal
X = data['Vuelos']
y = data['Ingreso']

# Agregar una constante (intercepto) al modelo
X = sm.add_constant(X)

# Ajustar el modelo de regresión
modelo = sm.OLS(y, X).fit()

# Resumen del modelo
print(modelo.summary())

# Parte b) Determinar el valor-p
p_value = modelo.pvalues[1]  # Valor-p del coeficiente de la variable independiente
print(f'Valor-p del coeficiente: {p_value:.4f}')

# Parte c) Conclusión
if p_value < 0.01:
    print('Rechazamos la hipótesis nula: Hay una relación significativa entre el número de vuelos y el ingreso.')
else:
    print('No podemos rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que existe una relación significativa entre el número de vuelos y el ingreso.')
