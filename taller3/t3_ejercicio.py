"""
TALLER DE LABORATORIO: LÓGICA DIFUSA COMERCIAL (40 MIN)
Evaluación de experiencia de conductores
"""

def membresia_triangular(x, a, b, c):
    """
    Calcula el grado de membresía para una función triangular
    Parámetros:
    x = valor a evaluar
    a = vértice izquierdo
    b = vértice central (pico)
    c = vértice derecho
    """
    if x <= a or x >= c:
        return 0.0
    elif x == b:
        return 1.0
    elif a < x < b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
    else:
        return 0.0

# ===== CONJUNTOS DIFUSOS PARA EXPERIENCIA =====
# Novato: triángulo (0, 0, 5)
# Intermedio: triángulo (2, 5, 8)
# Experto: triángulo (5, 10, 20)

# ===== CONDUCTORES A EVALUAR =====
conductores = [
    {"nombre": "Conductor A", "años": 3},
    {"nombre": "Conductor B", "años": 6},
    {"nombre": "Conductor C", "años": 12}
]

# ===== EVALUACIÓN =====
print("=" * 70)
print("SISTEMA DE EVALUACIÓN DE EXPERIENCIA - LÓGICA DIFUSA")
print("=" * 70)

for conductor in conductores:
    años = conductor["años"]
    nombre = conductor["nombre"]
    
    # Calcular grados de membresía
    novato = membresia_triangular(años, 0, 0, 5)
    intermedio = membresia_triangular(años, 2, 5, 8)
    experto = membresia_triangular(años, 5, 10, 20)
    
    # Mostrar resultados
    print(f"\n{nombre}: {años} años de experiencia")
    print(f"  Novato:     {novato:.2f}")
    print(f"  Intermedio: {intermedio:.2f}")
    print(f"  Experto:    {experto:.2f}")
    
    # Determinar categoría (la de mayor grado)
    categorias = {
        "Novato": novato,
        "Intermedio": intermedio,
        "Experto": experto
    }
    mejor_categoria = max(categorias, key=categorias.get)
    mayor_grado = categorias[mejor_categoria]
    
    print(f"  → Mejor categoría: {mejor_categoria} (grado {mayor_grado:.2f})")

# ===== ANÁLISIS ADICIONAL =====
print("\n" + "=" * 70)
print("ANÁLISIS DE RESULTADOS")
print("=" * 70)

# Probar más valores para ver el comportamiento
print("\nCOMPORTAMIENTO DE LA FUNCIÓN:")
for años in range(0, 21, 2):
    n = membresia_triangular(años, 0, 0, 5)
    i = membresia_triangular(años, 2, 5, 8)
    e = membresia_triangular(años, 5, 10, 20)
    print(f"Años: {años:2d} → Novato: {n:.2f}, Intermedio: {i:.2f}, Experto: {e:.2f}")

print("\n" + "=" * 70)
print("FIN DEL TALLER")
print("=" * 70)