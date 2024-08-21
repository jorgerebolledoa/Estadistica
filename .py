import math
import scipy.stats as stats
from scipy.stats import norm
def diferencia_proporciones(n1, x1, n2, x2, alpha=0.05):    
    # Calcular proporciones muestrales
    p1 = x1 / n1
    p2 = x2 / n2
    
    # Calcular proporción combinada
    p_comb = (x1 + x2) / (n1 + n2)
    
    # Calcular error estándar
    SE = math.sqrt(p_comb * (1 - p_comb) * (1/n1 + 1/n2))
    
    # Calcular valor de z
    z = (p1 - p2) / SE
    
    # Valor crítico para una prueba bilateral
    z_critico = norm.ppf(1 - alpha/2)
    
    # Calcular valor p para una prueba bilateral
    p_value = 2 * (1 - norm.cdf(abs(z)))
    
    # Determinar si se rechaza la hipótesis nula
    rechazo_hipotesis_nula = abs(z) >= z_critico
    
    return {
        "p1": p1,
        "p2": p2,
        "p_comb": p_comb,
        "p_value": p_value,
        "SE": SE,
        "z": z,
        "z_critico": z_critico,
        "rechazo_hipotesis_nula": rechazo_hipotesis_nula
    }

# Datos del ejercicio
n1 = 152
x1 = 5.5
n2 = 86
x2 = 3.8
alpha = 0.05

# Llamar a la función con los datos proporcionados
resultado = diferencia_proporciones(n1, x1, n2, x2, alpha)

# Mostrar los resultados
print("Proporción hombres (p1):", resultado["p1"])
print("Proporción mujeres (p2):", resultado["p2"])
print("Proporción combinada (p_comb):", resultado["p_comb"])
print("Error estándar (SE):", resultado["SE"])
print("Valor de z:", resultado["z"])
print("Valor crítico (z_critico):", resultado["z_critico"])
print("Valor p:", resultado["p_value"])
print("¿Rechazo de la hipótesis nula?:", resultado["rechazo_hipotesis_nula"])