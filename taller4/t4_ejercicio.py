"""Agregación Mamdani:
Si dos reglas concluyen lo mismo, se usa max() (T-Conorma)

Línea de código: fuerza_final = max(0.4, 0.7) → 0.7"""

# ===== VARIABLES DIFUSAS (GRADOS DE MEMBRESÍA) =====
variables_difusas = {
    # Desempeño
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    
    # Antigüedad
    "antiguedad_corta": 0.3,
    "antiguedad_media": 0.6,
    "antiguedad_larga": 0.6
}

print("=" * 70)
print("MOTOR LÓGICO DE RECURSOS HUMANOS - BONOS ANUALES")
print("=" * 70)
print("\nVariables difusas de entrada:")
for clave, valor in variables_difusas.items():
    print(f"  {clave}: {valor}")

# ===== MOTOR DE INFERENCIA DIFUSA =====
def motor_bonos(variables):
    """
    Motor de inferencia difusa para calcular bonos
    Retorna diccionario con niveles de activación
    """
    # Extraer valores
    d_pobre = variables.get("desempeno_pobre", 0)
    d_promedio = variables.get("desempeno_promedio", 0)
    d_excelente = variables.get("desempeno_excelente", 0)
    
    a_corta = variables.get("antiguedad_corta", 0)
    a_media = variables.get("antiguedad_media", 0)
    a_larga = variables.get("antiguedad_larga", 0)
    
    # ===== REGLAS DIFUSAS =====
    
    # R1: Si Desempeño es Pobre O Antigüedad es Corta → Bono Bajo
    # OR = max()
    fuerza_r1 = max(d_pobre, a_corta)
    
    # R2: Si Desempeño es Promedio → Bono Medio
    fuerza_r2 = d_promedio
    
    # R3: Si Desempeño es Excelente Y Antigüedad es Larga → Bono Alto
    # AND = min()
    fuerza_r3 = min(d_excelente, a_larga)
    
    # ===== AGREGACIÓN (Mamdani) =====
    # Para cada conclusión, usar T-Conorma (OR = max) si hay múltiples reglas
    bono_bajo = fuerza_r1
    bono_medio = fuerza_r2
    bono_alto = fuerza_r3
    
    # ===== RESULTADO =====
    resultado = {
        "Bono Bajo": round(bono_bajo, 2),
        "Bono Medio": round(bono_medio, 2),
        "Bono Alto": round(bono_alto, 2)
    }
    
    return resultado

# ===== EJECUCIÓN PRINCIPAL =====
print("\n" + "=" * 70)
print("EVALUACIÓN DEL EMPLEADO")
print("=" * 70)

resultado = motor_bonos(variables_difusas)

print("\nNiveles de activación:")
for nivel, fuerza in resultado.items():
    print(f"  {nivel}: {fuerza}")

# Determinar bono final
mejor_bono = max(resultado, key=resultado.get)
mayor_fuerza = resultado[mejor_bono]

print(f"\n→ Bono asignado: {mejor_bono} (fuerza {mayor_fuerza})")

# ===== PREGUNTA TEÓRICA: AGREGACIÓN CON MAMDANI =====
print("\n" + "=" * 70)
print("PREGUNTA TEÓRICA: AGREGACIÓN DE MAMDANI")
print("=" * 70)

# Si dos reglas concluyen en "Bono Alto" con fuerzas 0.4 y 0.7
fuerza_regla_a = 0.4
fuerza_regla_b = 0.7

# T-Conorma (OR) = max()
fuerza_final = max(fuerza_regla_a, fuerza_regla_b)

print(f"\nRegla A concluye 'Bono Alto' con fuerza: {fuerza_regla_a}")
print(f"Regla B concluye 'Bono Alto' con fuerza: {fuerza_regla_b}")
print(f"\nLínea de código para agregación:")
print(f"  fuerza_final = max(0.4, 0.7)")
print(f"\nResultado: fuerza_final = {fuerza_final}")
print(f"\nLa fuerza final para 'Bono Alto' es {fuerza_final}")

# ===== PRUEBAS CON DIFERENTES EMPLEADOS =====
print("\n" + "=" * 70)
print("PRUEBAS CON DIFERENTES EMPLEADOS")
print("=" * 70)

empleados = [
    {
        "nombre": "Empleado 1 (Pobre y Corta)",
        "datos": {
            "desempeno_pobre": 0.9,
            "desempeno_promedio": 0.1,
            "desempeno_excelente": 0.0,
            "antiguedad_corta": 0.8,
            "antiguedad_media": 0.2,
            "antiguedad_larga": 0.0
        }
    },
    {
        "nombre": "Empleado 2 (Promedio)",
        "datos": {
            "desempeno_pobre": 0.1,
            "desempeno_promedio": 0.8,
            "desempeno_excelente": 0.1,
            "antiguedad_corta": 0.2,
            "antiguedad_media": 0.7,
            "antiguedad_larga": 0.1
        }
    },
    {
        "nombre": "Empleado 3 (Excelente y Larga)",
        "datos": {
            "desempeno_pobre": 0.0,
            "desempeno_promedio": 0.1,
            "desempeno_excelente": 0.9,
            "antiguedad_corta": 0.0,
            "antiguedad_media": 0.2,
            "antiguedad_larga": 0.85
        }
    }
]

for empleado in empleados:
    print(f"\n{empleado['nombre']}:")
    res = motor_bonos(empleado["datos"])
    for nivel, fuerza in res.items():
        print(f"  {nivel}: {fuerza}")
    mejor = max(res, key=res.get)
    print(f"  → Bono: {mejor}")

print("\n" + "=" * 70)
print("FIN DEL TALLER")
print("=" * 70)


