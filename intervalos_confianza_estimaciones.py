import math
from scipy.stats import norm, t

# Intervalo de confianza para una media poblacional (varianza conocida)
def IC_MU_1(n, PROM, NC, SIGMA2):
    """
    Calcula el intervalo de confianza para una media poblacional con varianza conocida.
    
    Parámetros:
    n (int): Tamaño de la muestra
    PROM (float): Promedio muestral
    NC (float): Nivel de confianza (por ejemplo, 0.95)
    SIGMA2 (float): Varianza poblacional

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    Z = norm.ppf(aux)
    LI = PROM - Z * math.sqrt(SIGMA2 / n)
    LS = PROM + Z * math.sqrt(SIGMA2 / n)
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Intervalo de confianza para una media poblacional (varianza desconocida)
def IC_MU_2(n, PROM, NC, S2):
    """
    Calcula el intervalo de confianza para una media poblacional con varianza desconocida.
    
    Parámetros:
    n (int): Tamaño de la muestra
    PROM (float): Promedio muestral
    NC (float): Nivel de confianza (por ejemplo, 0.95)
    S2 (float): Varianza muestral

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    T = t.ppf(aux, n - 1)
    LI = PROM - T * math.sqrt(S2 / n)
    LS = PROM + T * math.sqrt(S2 / n)
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Intervalo de confianza para una proporción poblacional
def IC_PROP(n, P, NC):
    """
    Calcula el intervalo de confianza para una proporción poblacional.
    
    Parámetros:
    n (int): Tamaño de la muestra
    P (float): Proporción muestral
    NC (float): Nivel de confianza (por ejemplo, 0.95)

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    Z = norm.ppf(aux)
    LI = P - Z * math.sqrt(P * (1 - P) / n)
    LS = P + Z * math.sqrt(P * (1 - P) / n)
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Tamaño de la muestra para estimar una media poblacional
def n_Mu(EE, NC, SIGMA2):
    """
    Calcula el tamaño de la muestra necesario para estimar una media poblacional.
    
    Parámetros:
    EE (float): Error de estimación
    NC (float): Nivel de confianza (por ejemplo, 0.95)
    SIGMA2 (float): Varianza poblacional

    Retorna:
    dict: Tamaño de la muestra necesario
    """
    aux = 1 - (1 - NC) / 2
    Z = norm.ppf(aux)
    n = round((Z / EE) ** 2 * SIGMA2)
    return {"Tamaño Muestra": n}

# Tamaño de la muestra para estimar una proporción poblacional
def n_Prop(EE, NC, P):
    """
    Calcula el tamaño de la muestra necesario para estimar una proporción poblacional.
    
    Parámetros:
    EE (float): Error de estimación
    NC (float): Nivel de confianza (por ejemplo, 0.95)
    P (float): Proporción muestral

    Retorna:
    dict: Tamaño de la muestra necesario y el peor de los casos
    """
    aux = 1 - (1 - NC) / 2
    Z = norm.ppf(aux)
    n1 = round((Z / EE) ** 2 * P * (1 - P))
    n2 = round(1 / 4 * (Z / EE) ** 2)
    return {"Tamaño Muestra": n1, "Peor de los casos": n2}

# Ejemplo de uso 1: Intervalo de confianza para una media poblacional (varianza conocida)
resultado = IC_MU_1(n=30, PROM=50, NC=0.95, SIGMA2=25)
print("Intervalo de confianza para una media poblacional (varianza conocida):", resultado)

# Ejemplo de uso 2: Intervalo de confianza para una media poblacional (varianza desconocida)
resultado = IC_MU_2(n=30, PROM=50, NC=0.95, S2=25)
print("Intervalo de confianza para una media poblacional (varianza desconocida):", resultado)

# Ejemplo de uso 3: Intervalo de confianza para una proporción poblacional
resultado = IC_PROP(n=100, P=0.5, NC=0.95)
print("Intervalo de confianza para una proporción poblacional:", resultado)

# Ejemplo de uso 4: Tamaño de la muestra para estimar una media poblacional
resultado = n_Mu(EE=0.05, NC=0.95, SIGMA2=25)
print("Tamaño de la muestra para estimar una media poblacional:", resultado)

# Ejemplo de uso 5: Tamaño de la muestra para estimar una proporción poblacional
resultado = n_Prop(EE=0.05, NC=0.95, P=0.5)
print("Tamaño de la muestra para estimar una proporción poblacional:", resultado)


print("Fin del programa")