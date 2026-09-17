
import numpy as np

# ============================================================
# 1. FUNCIÓN DE ACTIVACIÓN (ESCALÓN)
# ============================================================
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0

# ============================================================
# 2. ESTRUCTURA DEL PERCEPTRÓN
# ============================================================
def perceptron(X, W, b):
    # Producto punto (combinación lineal)
    Z = np.dot(X, W) + b
    # Activación
    salida = funcion_escalon(Z)
    return salida

# ============================================================
# 3. VERIFICACIÓN DE LA COMPUERTA AND
# ============================================================
print("=" * 60)
print("VERIFICACIÓN COMPUERTA AND")
print("=" * 60)

pesos_and = np.array([0.5, 0.5])
sesgo_and = -0.8

entradas_and = [[0, 0], [0, 1], [1, 0], [1, 1]]

for e in entradas_and:
    r = perceptron(np.array(e), pesos_and, sesgo_and)
    print(f"  Entrada {e} → Salida {r}")

# ============================================================
# 4. RETO: ENCONTRAR LOS PESOS PARA LA COMPUERTA OR
# ============================================================
print("\n" + "=" * 60)
print("RETO: COMPUERTA OR")
print("=" * 60)

# Solución encontrada manualmente:
pesos_or = np.array([1.0, 1.0])
sesgo_or = -0.5

print(f"Pesos propuestos: W = {pesos_or}")
print(f"Sesgo propuesto: b = {sesgo_or}")
print()

entradas_or = [[0, 0], [0, 1], [1, 0], [1, 1]]

for e in entradas_or:
    r = perceptron(np.array(e), pesos_or, sesgo_or)
    print(f"  Entrada {e} → Salida {r}")

# ============================================================
# 5. ANÁLISIS MATEMÁTICO DE LA SOLUCIÓN
# ============================================================
print("\n" + "=" * 60)
print("ANÁLISIS MATEMÁTICO")
print("=" * 60)
print("""
Con W = [1, 1] y b = -0.5:
Z = 1·X1 + 1·X2 - 0.5

- [0,0]: Z = 0 + 0 - 0.5 = -0.5 < 0 → 0 ✓
- [0,1]: Z = 0 + 1 - 0.5 =  0.5 ≥ 0 → 1 ✓
- [1,0]: Z = 1 + 0 - 0.5 =  0.5 ≥ 0 → 1 ✓
- [1,1]: Z = 1 + 1 - 0.5 =  1.5 ≥ 0 → 1 ✓

Estos pesos resuelven la compuerta OR correctamente.
Lo que un humano acaba de hacer manualmente, una red neuronal
lo hará automáticamente en la próxima clase mediante el
algoritmo de retropropagación (Backpropagation).
""")

print("=" * 60)
print("FIN DEL TALLER 11")
print("=" * 60)