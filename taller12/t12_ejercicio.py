"""
TALLER DE LABORATORIO: EXPLORANDO LAS MATRICES (35 MIN)
Red neuronal con 3 entradas, 4 neuronas ocultas y 1 salida
"""

import numpy as np

# ============================================================
# FUNCIÓN DE ACTIVACIÓN: SIGMOIDE
# ============================================================
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# ============================================================
# CÓDIGO DE REFERENCIA ORIGINAL (1 cliente)
# ============================================================
print("=" * 60)
print("CÓDIGO ORIGINAL: 1 CLIENTE")
print("=" * 60)

# 1. ENTRADA (X): 1 cliente con 3 características
X = np.array([0.5, 0.8, 0.2])

# 2. CAPA OCULTA (4 Neuronas)
# Matriz W1 de (3 entradas x 4 neuronas)
W1 = np.array([
    [0.1,  0.2, -0.3,  0.4],
    [-0.5, 0.6,  0.7, -0.8],
    [0.9, -0.1,  0.2,  0.3]
])
b1 = np.array([0.1, -0.2, 0.3, -0.4])  # 4 Sesgos

# --- PROCESO CAPA OCULTA ---
Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)  # Salida de la capa oculta

# 3. CAPA DE SALIDA (1 Neurona)
# Matriz W2 de (4 entradas ocultas x 1 neurona final)
W2 = np.array([0.5, -0.6, 0.7, 0.8])
b2 = np.array([-0.1])

# --- PROCESO CAPA FINAL ---
Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

print("Predicción de la Red (Probabilidad):", np.round(Salida_Final[0], 4))

# Mostrar Z1 y A1 para analizar la transformación sigmoide
print("\nAnálisis de la capa oculta:")
print(f"Z1 (valores puros): {Z1}")
print(f"A1 (después de sigmoide): {A1}")
print("Observa cómo la sigmoide comprime los valores de Z1 al rango (0, 1).")

# ============================================================
# RETO DIMENSIONAL: PROCESAMIENTO EN LOTE (2 CLIENTES)
# ============================================================
print("\n" + "=" * 60)
print("RETO DIMENSIONAL: 2 CLIENTES AL MISMO TIEMPO")
print("=" * 60)

# Matriz X de 2x3: 2 clientes, 3 características cada uno
X_batch = np.array([
    [0.5, 0.8, 0.2],
    [0.1, 0.9, 0.9]
])

print(f"X_batch (2 clientes x 3 características):\n{X_batch}")

# --- PROCESO CAPA OCULTA (BATCH) ---
Z1_batch = np.dot(X_batch, W1) + b1
A1_batch = sigmoide(Z1_batch)

print(f"\nZ1_batch (2x4):\n{Z1_batch}")
print(f"\nA1_batch (2x4):\n{A1_batch}")

# --- PROCESO CAPA DE SALIDA (BATCH) ---
Z2_batch = np.dot(A1_batch, W2) + b2
Salida_Batch = sigmoide(Z2_batch)

print(f"\nZ2_batch (2x1):\n{Z2_batch}")
print(f"\nPredicciones para los 2 clientes:\n{np.round(Salida_Batch, 4)}")

# ============================================================
# CONTEO DE PARÁMETROS ENTRENABLES
# ============================================================
print("\n" + "=" * 60)
print("CONTEO DE PARÁMETROS ENTRENABLES")
print("=" * 60)
print(f"W1 (3x4) = {W1.size} pesos")
print(f"b1       = {b1.size} sesgos")
print(f"W2 (4x1) = {W2.size} pesos")
print(f"b2       = {b2.size} sesgo")
print(f"TOTAL    = {W1.size + b1.size + W2.size + b2.size} parámetros")

print("=" * 60)
print("FIN DEL TALLER 12")
print("=" * 60)