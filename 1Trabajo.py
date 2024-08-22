import scipy.stats as stats

# Datos proporcionados
mu_0 = 82000  # Ingreso medio en 1980
x_bar = 80500  # Ingreso medio en 1981
s = 10000  # Desviación estándar de la muestra
n = 100  # Tamaño de la muestra
alpha = 0.01  # Nivel de significancia

# Calcular el estadístico t
t_stat = (x_bar - mu_0) / (s / (n ** 0.5))

# Calcular el p-valor para una prueba de una cola (menor)
p_value = stats.t.cdf(t_stat, df=n-1)

# Imprimir los resultados
print(f'Estadístico t: {t_stat:.4f}')
print(f'P-valor: {p_value:.4f}')

# Determinar si rechazamos la hipótesis nula
if p_value < alpha:
    print('Rechazamos la hipótesis nula: El ingreso medio anual por familia disminuyó en 1981.')
else:
    print('No podemos rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que el ingreso medio anual por familia disminuyó en 1981.')
