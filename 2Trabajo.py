import scipy.stats as stats

# Datos proporcionados
n_m = 152  # Tamaño de la muestra masculina
n_f = 86   # Tamaño de la muestra femenina
mean_m = 5.5  # Media muestral masculina
mean_f = 3.8  # Media muestral femenina
std_m = 0.3  # Desviación estándar muestral masculina
std_f = 0.2  # Desviación estándar muestral femenina
alpha = 0.05  # Nivel de significación

# Calcular el estadístico t y el p-valor
t_stat, p_value = stats.ttest_ind_from_stats(mean1=mean_m, std1=std_m, nobs1=n_m,
                                             mean2=mean_f, std2=std_f, nobs2=n_f,
                                             equal_var=False, alternative='greater')

# Imprimir los resultados
print(f'Estadístico t: {t_stat:.4f}')
print(f'P-valor: {p_value:.4f}')

# Determinar si rechazamos la hipótesis nula
if p_value < alpha:
    print('Rechazamos la hipótesis nula: La concentración media de plomo en los hombres es significativamente mayor que en las mujeres.')
else:
    print('No podemos rechazar la hipótesis nula: No hay suficiente evidencia para afirmar que la concentración media de plomo en los hombres es mayor que en las mujeres.')
