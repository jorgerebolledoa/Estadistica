import math
import scipy.stats as stats

def IC_difProporciones(n1, p1, n2, p2, NC=0.95):
    """
    Calcula el intervalo de confianza para la diferencia de proporciones entre dos muestras.

    Parámetros:
    n1 (int): Tamaño de la muestra 1 (hombres)
    p1 (float): Proporción muestral 1 (proporción de hombres que opinan que el sexo no importa)
    n2 (int): Tamaño de la muestra 2 (mujeres)
    p2 (float): Proporción muestral 2 (proporción de mujeres que opinan que el sexo no importa)
    NC (float): Nivel de confianza (por defecto es 0.95)

    Retorna:
    dict: Intervalo de confianza con límite inferior, límite superior y la diferencia de proporciones observada
    """
    z = stats.norm.ppf(1 - (1 - NC) / 2)
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    margin_of_error = z * se
    lower_bound = diff - margin_of_error
    upper_bound = diff + margin_of_error

    return {
        "Diferencia de proporciones": diff,
        "Límite Inferior": lower_bound,
        "Límite Superior": upper_bound,
        "Nivel de Confianza": NC
    }

# Ejemplo de uso para el problema planteado
n1 = 300  # Número de hombres entrevistados
p1 = 0.03  # Proporción de hombres que opinan que el sexo no importa
n2 = 300  # Número de mujeres entrevistados
p2 = 0.02666  # Proporción de mujeres que opinan que el sexo no importa
NC = 0.95  # Nivel de confianza

resultado = IC_difProporciones(n1, p1, n2, p2, NC)
print("Intervalo de confianza para la diferencia de proporciones:", resultado)
