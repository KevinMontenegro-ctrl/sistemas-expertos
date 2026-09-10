"""
TALLER DE LABORATORIO FINAL: EL EXPERTO AUTOMÁTICO (45 MIN)
Proyecto Integrador del Módulo 1 - Árbol de Decisión con scikit-learn
"""

# Instalar si es necesario: pip install scikit-learn numpy
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

# ===== DATASET SIMULADO PARA MARKETING =====
# Columnas: [Edad, Horas_Online, Compras_Previas]
# Etiqueta: 1 = Hizo clic en el anuncio, 0 = Lo ignoró

X = np.array([
    [25, 10, 2],   # 1
    [30,  8, 3],   # 1
    [22,  6, 1],   # 1
    [35, 12, 4],   # 1
    [28,  5, 1],   # 1
    [40,  9, 2],   # 1
    [45,  2, 0],   # 0
    [50,  1, 1],   # 0
    [55,  3, 0],   # 0
    [60,  0, 2],   # 0
    [33,  4, 2],   # 0
    [38,  3, 3],   # 0
])

y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

nombres_columnas = ["Edad", "Horas_Online", "Compras_Previas"]

# ===== ENTRENAR ÁRBOL DE DECISIÓN =====
print("=" * 70)
print("ENTRENANDO ÁRBOL DE DECISIÓN - MARKETING")
print("=" * 70)

modelo = DecisionTreeClassifier(criterion="entropy", random_state=42)
modelo.fit(X, y)

# ===== IMPRIMIR ÁRBOL EN TEXTO =====
print("\nÁRBOL DE DECISIÓN APRENDIDO:\n")
arbol_texto = export_text(modelo, feature_names=nombres_columnas)
print(arbol_texto)

# ===== PREDICCIONES DE EJEMPLO =====
print("=" * 70)
print("PREDICCIONES CON NUEVOS CLIENTES")
print("=" * 70)

nuevos_clientes = np.array([
    [26, 7, 2],   # Joven, muchas horas online, compras previas
    [48, 1, 0],   # Mayor, pocas horas online, sin compras previas
    [32, 4, 3],   # Horas medias-bajas
])

predicciones = modelo.predict(nuevos_clientes)

for cliente, pred in zip(nuevos_clientes, predicciones):
    etiqueta = "HIZO CLIC" if pred == 1 else "IGNORÓ"
    print(f"Cliente {cliente} → {etiqueta}")

# ===== DISCUSIÓN GRUPAL =====
print("\n" + "=" * 70)
print("DISCUSIÓN GRUPAL")
print("=" * 70)

print("""
1. ¿Tienen sentido comercial las reglas?
   Sí. El árbol descubrió que 'Horas_Online' es la variable más importante.
   Clientes con más de 4 horas online tienden a hacer clic; los que pasan
   menos de 4 horas, ignoran el anuncio. Esto es lógico: mayor interacción
   digital = mayor probabilidad de respuesta al marketing.

2. ¿Es capaz la IA de crear la Base de Conocimientos de un Sistema Experto
   mejor y más rápido que un humano?
   La IA es más rápida y puede analizar muchas variables sin sesgos.
   Sin embargo, el humano aporta contexto, ética y sentido común.
   Lo ideal es un enfoque híbrido: la IA extrae reglas de los datos y el
   experto humano las valida y enriquece.
""")

print("=" * 70)
print("FIN DEL TALLER FINAL")
print("=" * 70)