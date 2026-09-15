"""
CODIGO DE REFERENCIA ORIGINAL:
--------------------------------------------------
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 1. Dataset de Entrenamiento: [Característica 1, Característica 2]
X_entrenamiento = np.array([
    [20, 30],  # Punto A
    [40, 50],  # Punto B
    [35, 45]   # Punto C
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1])

# 2. Instanciar el modelo con K = 3
modelo_knn = KNeighborsClassifier(n_neighbors=3)

# 3. "Entrenar" (Memorizar los datos)
modelo_knn.fit(X_entrenamiento, Y_entrenamiento)

# 4. Predecir un nuevo punto
nuevo_cliente = np.array([[30, 40]])
prediccion = modelo_knn.predict(nuevo_cliente)

print("Clase predicha:", prediccion[0])
--------------------------------------------------
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# ============================================================
# 1. DATASET AMPLIADO CON 3 COLUMNAS
# Columnas: [Edad, Salario, Número de Hijos]
# ============================================================
X_entrenamiento = np.array([
    [20, 30, 0],   # A
    [40, 50, 1],   # B
    [35, 45, 2],   # C
    [25, 35, 1],
    [30, 40, 0],
    [45, 55, 3],
    [50, 60, 2],
    [22, 28, 0],
    [28, 32, 1],
    [55, 65, 4],
    [60, 70, 2],
    [18, 25, 0]
])

# Etiquetas: 0 = NO COMPRA, 1 = COMPRA
Y_entrenamiento = np.array([0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0])

# Punto nuevo a predecir: [Edad, Salario, Hijos]
nuevo_cliente = np.array([[30, 40, 1]])

# ============================================================
# 2. EXPERIMENTO CON K = 1
# ============================================================
modelo_k1 = KNeighborsClassifier(n_neighbors=1)
modelo_k1.fit(X_entrenamiento, Y_entrenamiento)
pred_k1 = modelo_k1.predict(nuevo_cliente)

print("=" * 60)
print("RESULTADOS CON K = 1")
print("=" * 60)
print(f"Punto nuevo: {nuevo_cliente[0]}")
print(f"Clase predicha: {'COMPRA' if pred_k1[0] == 1 else 'NO COMPRA'}")

# ============================================================
# 3. EXPERIMENTO CON K = 5
# ============================================================
modelo_k5 = KNeighborsClassifier(n_neighbors=5)
modelo_k5.fit(X_entrenamiento, Y_entrenamiento)
pred_k5 = modelo_k5.predict(nuevo_cliente)

print("\n" + "=" * 60)
print("RESULTADOS CON K = 5")
print("=" * 60)
print(f"Punto nuevo: {nuevo_cliente[0]}")
print(f"Clase predicha: {'COMPRA' if pred_k5[0] == 1 else 'NO COMPRA'}")

# ============================================================
# 4. PREGUNTA DE ANÁLISIS: MALDICIÓN DE LA DIMENSIONALIDAD
# ============================================================
print("\n" + "=" * 60)
print("PREGUNTA DE ANÁLISIS: MALDICIÓN DE LA DIMENSIONALIDAD")
print("=" * 60)
print("""
Si en lugar de 3 columnas tuviéramos 1,000 columnas (como los píxeles
de una imagen), la Distancia Euclidiana entre los puntos tendería a
hacerse casi igual para todos.

Matemáticamente:
- La distancia promedio entre puntos crece con la dimensión.
- Pero la diferencia entre la distancia más cercana y la más lejana
  se vuelve muy pequeña.
- Todos los puntos parecen estar "casi a la misma distancia".

Consecuencia:
El algoritmo KNN pierde capacidad de discriminación porque ya no puede
distinguir claramente quién es el vecino más cercano. Además, los datos
se vuelven extremadamente dispersos: para mantener la misma densidad
de puntos, el número de datos necesarios crece de forma exponencial.

Solución típica:
Reducción de dimensionalidad (PCA, selección de características) o usar
métricas de distancia más adecuadas.
""")

print("=" * 60)
print("FIN DEL TALLER 9")
print("=" * 60)