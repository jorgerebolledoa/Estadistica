import scipy.stats as stats

def prueba_var(n, s2, v0, H1="distinto", NS=0.05):
    """
    Realiza la prueba de hipótesis para una varianza poblacional.

    Parámetros:
    n (int): Tamaño de la muestra
    s2 (float): Varianza muestral
    v0 (float): Valor de la varianza en H0
    H1 (str): Hipótesis alternativa ("distinto", "menor", "mayor")
    NS (float): Nivel de significación (por ejemplo, 0.05)

    Retorna:
    dict: Resultado de la prueba con hipótesis, límites críticos, y decisión
    """
    E0 = (n - 1) * s2 / v0
    decision = ""
    c1, c2 = None, None

    if H1 == "distinto":
        c1 = stats.chi2.ppf(NS / 2, n - 1)
        c2 = stats.chi2.ppf(1 - NS / 2, n - 1)
        if E0 < c1 or E0 > c2:
            decision = "Rechazo H0"
        else:
            decision = "No Rechazo H0"
    elif H1 == "mayor":
        c2 = stats.chi2.ppf(1 - NS, n - 1)
        if E0 > c2:
            decision = "Rechazo H0"
        else:
            decision = "No Rechazo H0"
    elif H1 == "menor":
        c1 = stats.chi2.ppf(NS, n - 1)
        if E0 < c1:
            decision = "Rechazo H0"
        else:
            decision = "No Rechazo H0"
    
    return {
        "Hipótesis Alternativa": H1,
        "Estadístico de Prueba": E0,
        "Límite Inferior": c1,
        "Límite Superior": c2,
        "Decisión": decision
    }

# Ejemplo de uso:
resultado = prueba_var(n=30, s2=20, v0=15, H1="menor", NS=0.05)
print("Resultado de la prueba de hipótesis para varianza poblacional:", resultado)


