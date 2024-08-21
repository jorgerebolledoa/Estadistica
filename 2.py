import math
from scipy.stats import norm, t, f

# Intervalo de confianza para la diferencia de medias (varianzas poblacionales conocidas)
def IC_difMedias_1(n1, prom1, n2, prom2, var1, var2, NC):
    """
    Calcula el intervalo de confianza para la diferencia de medias con varianzas poblacionales conocidas.
    
    Parámetros:
    n1 (int): Tamaño de la muestra 1
    prom1 (float): Promedio muestral 1
    n2 (int): Tamaño de la muestra 2
    prom2 (float): Promedio muestral 2
    var1 (float): Varianza poblacional 1
    var2 (float): Varianza poblacional 2
    NC (float): Nivel de confianza (por ejemplo, 0.95)

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    Z = norm.ppf(aux)
    algo = Z * math.sqrt(var1 / n1 + var2 / n2)
    LI = (prom1 - prom2) - algo
    LS = (prom1 - prom2) + algo
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Intervalo de confianza para la diferencia de medias (varianzas desconocidas e iguales)
def IC_difMedias_2(n1, prom1, n2, prom2, S2_1, S2_2, NC):
    """
    Calcula el intervalo de confianza para la diferencia de medias con varianzas desconocidas e iguales.
    
    Parámetros:
    n1 (int): Tamaño de la muestra 1
    prom1 (float): Promedio muestral 1
    n2 (int): Tamaño de la muestra 2
    prom2 (float): Promedio muestral 2
    S2_1 (float): Varianza muestral 1
    S2_2 (float): Varianza muestral 2
    NC (float): Nivel de confianza (por ejemplo, 0.95)

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    T = t.ppf(aux, n1 + n2 - 2)
    Sp2 = ((n1 - 1) * S2_1 + (n2 - 1) * S2_2) / (n1 + n2 - 2)
    Sp = math.sqrt(Sp2)
    algo = T * Sp * math.sqrt(1 / n1 + 1 / n2)
    LI = (prom1 - prom2) - algo
    LS = (prom1 - prom2) + algo
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Intervalo de confianza para la diferencia de medias (varianzas desconocidas y diferentes)
def IC_difMedias_3(n1, prom1, n2, prom2, S2_1, S2_2, NC):
    """
    Calcula el intervalo de confianza para la diferencia de medias con varianzas desconocidas y diferentes.
    
    Parámetros:
    n1 (int): Tamaño de la muestra 1
    prom1 (float): Promedio muestral 1
    n2 (int): Tamaño de la muestra 2
    prom2 (float): Promedio muestral 2
    S2_1 (float): Varianza muestral 1
    S2_2 (float): Varianza muestral 2
    NC (float): Nivel de confianza (por ejemplo, 0.95)

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux = 1 - (1 - NC) / 2
    eta = (S2_1 / n1 + S2_2 / n2) ** 2 / ((S2_1 / n1) ** 2 / (n1 - 1) + (S2_2 / n2) ** 2 / (n2 - 1))
    T = t.ppf(aux, eta)
    algo = T * math.sqrt(S2_1 / n1 + S2_2 / n2)
    LI = (prom1 - prom2) - algo
    LS = (prom1 - prom2) + algo
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Intervalo de confianza para el cociente de varianzas
def IC_cuoVar(n1, S2_1, n2, S2_2, NC):
    """
    Calcula el intervalo de confianza para el cociente de varianzas.
    
    Parámetros:
    n1 (int): Tamaño muestral 1
    S2_1 (float): Varianza muestral 1
    n2 (int): Tamaño muestral 2
    S2_2 (float): Varianza muestral 2
    NC (float): Nivel de confianza (por ejemplo, 0.95)

    Retorna:
    dict: Limite Inferior y Limite Superior del intervalo de confianza
    """
    aux1 = (1 - NC) / 2
    aux2 = 1 - aux1
    f1 = f.ppf(aux1, n1 - 1, n2 - 1)
    f2 = f.ppf(aux2, n1 - 1, n2 - 1)
    cuo = S2_1 / S2_2
    LI = cuo / f2
    LS = cuo / f1
    return {"Limite Inferior": LI, "Limite Superior": LS}

# Ejemplo de uso 1: Intervalo de confianza para la diferencia de medias (varianzas conocidas)
resultado = IC_difMedias_1(n1=30, prom1=100, n2=30, prom2=90, var1=25, var2=30, NC=0.95)
print("Intervalo de confianza para la diferencia de medias (varianzas conocidas):", resultado)

# Ejemplo de uso 2: Intervalo de confianza para la diferencia de medias (varianzas desconocidas e iguales)
resultado = IC_difMedias_2(n1=30, prom1=100, n2=30, prom2=90, S2_1=25, S2_2=30, NC=0.95)
print("Intervalo de confianza para la diferencia de medias (varianzas desconocidas e iguales):", resultado)

# Ejemplo de uso 3: Intervalo de confianza para la diferencia de medias (varianzas desconocidas y diferentes)
resultado = IC_difMedias_3(n1=30, prom1=100, n2=30, prom2=90, S2_1=25, S2_2=30, NC=0.95)
print("Intervalo de confianza para la diferencia de medias (varianzas desconocidas y diferentes):", resultado)

# Ejemplo de uso 4: Intervalo de confianza para el cociente de varianzas
resultado = IC_cuoVar(n1=30, S2_1=25, n2=30, S2_2=30, NC=0.95)
print("Intervalo de confianza para el cociente de varianzas:", resultado)
