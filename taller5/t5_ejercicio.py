import numpy as np

# ===== FUNCIÓN DE DEFUZZIFICACIÓN (COG) =====
def centroide_cog(x, mu):
    """
    Calcula el Centro de Gravedad (Center of Gravity)
    Fórmula: COG = Σ(x · μ(x)) / Σ μ(x)
    """
    x = np.array(x, dtype=float)
    mu = np.array(mu, dtype=float)
    
    numerador = np.sum(x * mu)
    denominador = np.sum(mu)
    
    if denominador == 0:
        return 0.0
    
    return numerador / denominador

# ===== VALIDACIÓN CON DATOS DEL TALLER ANALÍTICO =====
print("=" * 70)
print("VALIDACIÓN CON DATOS DEL TALLER ANALÍTICO")
print("=" * 70)

x_validacion = [10, 20, 30, 40]
mu_validacion = [0.2, 0.8, 0.8, 0.0]

print(f"\nx = {x_validacion}")
print(f"μ = {mu_validacion}")

numerador = np.sum(np.array(x_validacion) * np.array(mu_validacion))
denominador = np.sum(mu_validacion)

print(f"\nNumerador Σ(x·μ) = {numerador}")
print(f"Denominador Σ(μ) = {denominador}")

resultado_validacion = centroide_cog(x_validacion, mu_validacion)
print(f"\nCOG = {resultado_validacion:.2f}%")
print(f"Resultado esperado: 23.33%")
print(f"✓ Coincide con el papel: {abs(resultado_validacion - 23.33) < 0.01}")

# ===== NUEVO ESCENARIO: FRENADO AUTOMÁTICO =====
print("\n" + "=" * 70)
print("ESCENARIO: SISTEMA DE FRENADO AUTOMÁTICO")
print("=" * 70)

# Eje X: fuerza de frenado de 0 a 100 Newtons (100 elementos)
x_frenado = np.linspace(0, 100, 100)

# Curva campana de Gauss centrada en 70
centro = 70
sigma = 15
curva_frenado = np.exp(-((x_frenado - centro) ** 2) / (2 * sigma ** 2))

print(f"\nCentro de la campana: {centro} N")
print(f"Desviación estándar (sigma): {sigma} N")
print(f"Rango de fuerza: 0 a 100 N")
print(f"Número de elementos: {len(x_frenado)}")

# Aplicar defuzzificación
fuerza_exacta = centroide_cog(x_frenado, curva_frenado)

print(f"\nFuerza de frenado exacta (crisp): {fuerza_exacta:.2f} Newtons")
print(f"Centro teórico: {centro} N")

# ===== PRUEBAS ADICIONALES =====
print("\n" + "=" * 70)
print("PRUEBAS CON DIFERENTES CENTROS")
print("=" * 70)

for c in [30, 50, 70, 90]:
    curva = np.exp(-((x_frenado - c) ** 2) / (2 * sigma ** 2))
    resultado = centroide_cog(x_frenado, curva)
    print(f"Centro teórico: {c} N → Fuerza calculada: {resultado:.2f} N")

# ===== VISUALIZACIÓN SIMPLE (TEXTO) =====
print("\n" + "=" * 70)
print("DISTRIBUCIÓN DE LA CURVA DE FRENADO")
print("=" * 70)

for i in range(0, len(x_frenado), 10):
    barra = "█" * int(curva_frenado[i] * 50)
    print(f"x={x_frenado[i]:6.1f} N | μ={curva_frenado[i]:.3f} {barra}")

print("\n" + "=" * 70)
print("FIN DEL TALLER")
print("=" * 70)