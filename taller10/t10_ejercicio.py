
import numpy as np
from sklearn.svm import SVC

# ============================================================
# CÓDIGO DE REFERENCIA ORIGINAL
# ============================================================
print("=" * 70)
print("CODIGO DE REFERENCIA ORIGINAL")
print("=" * 70)

X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])
Y = np.array([0, 0, 0, 1, 1, 1])

modelo_svm = SVC(kernel='linear')
modelo_svm.fit(X, Y)

vectores = modelo_svm.support_vectors_
print("Los Vectores de Soporte son:\n", vectores)

nuevo_punto = np.array([[5, 4]])
pred = modelo_svm.predict(nuevo_punto)
print("El punto [5,4] pertenece a la clase:", pred[0])

# ============================================================
# 1. AGREGAR NUEVO PUNTO [5,5] CON ETIQUETA 0 (CLASE A)
# ============================================================
print("\n" + "=" * 70)
print("DATASET AMPLIADO CON [5,5] ETIQUETA 0")
print("=" * 70)

X2 = np.vstack([X, [5, 5]])
Y2 = np.append(Y, 0)

print("X ampliado:\n", X2)
print("Y ampliado:\n", Y2)

# ============================================================
# 2. ENTRENAR MODELO LINEAL CON EL NUEVO DATASET
# ============================================================
modelo_lineal = SVC(kernel='linear')
modelo_lineal.fit(X2, Y2)

print("\nVectores de soporte (kernel lineal):")
print(modelo_lineal.support_vectors_)

print("\nPredicciones con kernel lineal:")
print("  [5,4] → clase", modelo_lineal.predict([[5, 4]])[0])
print("  [5,5] → clase", modelo_lineal.predict([[5, 5]])[0])

# ============================================================
# 3. ENTRENAR MODELO RBF
# ============================================================
modelo_rbf = SVC(kernel='rbf')
modelo_rbf.fit(X2, Y2)

print("\n" + "=" * 70)
print("MODELO CON KERNEL RBF")
print("=" * 70)

print("Vectores de soporte (RBF):")
print(modelo_rbf.support_vectors_)

print("\nPredicciones con kernel RBF:")
print("  [5,4] → clase", modelo_rbf.predict([[5, 4]])[0])
print("  [5,5] → clase", modelo_rbf.predict([[5, 5]])[0])

# ============================================================
# 4. REFLEXIÓN
# ============================================================
print("\n" + "=" * 70)
print("REFLEXIÓN: KERNEL LINEAL VS RBF")
print("=" * 70)
print("""
En este caso, el kernel lineal todavía logra separar las clases porque
el punto [5,5] no está rodeado por la Clase B; solo reduce el margen.
La recta x + y = 11 separa Clase A de Clase B.

Sin embargo, un kernel lineal falla completamente cuando las clases
no son linealmente separables. Escenarios reales:

- Medicina: diferenciar tumores benignos y malignos según textura,
  forma y tamaño. La frontera suele ser irregular y no lineal.
- Reconocimiento facial: distinguir una cara de otra con variaciones
  de iluminación, pose y expresión. No hay un plano simple que separe.
- Detección de fraudes complejos: patrones de comportamiento que se
  entrelazan y no se separan con una sola recta.

El Kernel Trick (RBF) permite proyectar los datos a una dimensión mayor
donde sí se pueden separar con un hiperplano, creando fronteras curvas.
""")

print("=" * 70)
print("FIN DEL TALLER 10")
print("=" * 70)