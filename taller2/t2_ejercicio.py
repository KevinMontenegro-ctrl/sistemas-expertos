"""
TALLER DE LABORATORIO: MOTOR DE FRAUDE BANCARIO
Sistema de Detección de Fraude con Forward Chaining
"""

# ===== HECHOS INICIALES =====
hechos = {
    "monto_transaccion": 7500,
    "pais_extranjero": True,
    "tarjeta_activa": True,
    "intentos_fallidos": 2,
    "dispositivo_confiable": False
}

# ===== REGLAS =====
reglas = [
    {
        "id": "R1",
        "condiciones": {"monto_transaccion": lambda x: x > 5000},
        "conclusion": {"transaccion_inusual": True}
    },
    {
        "id": "R2",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
        "conclusion": {"bloquear_tarjeta": True}
    },
    {
        "id": "R3",
        "condiciones": {"intentos_fallidos": lambda x: x >= 3, "dispositivo_confiable": False},
        "conclusion": {"posible_fraude": True}
    },
    {
        "id": "R4",
        "condiciones": {"bloquear_tarjeta": True, "tarjeta_activa": True},
        "conclusion": {"notificar_seguridad": True}
    }
]

# ===== MOTOR DE INFERENCIA =====
def evaluar_condicion(condicion, valor_hecho):
    if callable(condicion):
        return condicion(valor_hecho)
    return valor_hecho == condicion

def forward_chaining(hechos_iniciales, reglas):
    hechos = hechos_iniciales.copy()
    nuevos_hechos = True
    reglas_disparadas = []
    
    print("=" * 70)
    print("MOTOR DE INFERENCIA - DETECCIÓN DE FRAUDE")
    print("=" * 70)
    print(f"Hechos iniciales: {hechos}\n")
    
    ciclo = 1
    while nuevos_hechos:
        nuevos_hechos = False
        print(f"\n--- CICLO {ciclo} ---")
        
        for regla in reglas:
            condiciones_cumplidas = all(
                evaluar_condicion(condicion, hechos.get(clave))
                for clave, condicion in regla["condiciones"].items()
                if clave in hechos
            )
            
            if condiciones_cumplidas:
                for clave, valor in regla["conclusion"].items():
                    if clave not in hechos:
                        hechos[clave] = valor
                        nuevos_hechos = True
                        reglas_disparadas.append(regla["id"])
                        print(f"✅ R{regla['id']} → {clave} = {valor}")
        
        print(f"Memoria: {hechos}")
        ciclo += 1
    
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    print(f"Reglas disparadas: {reglas_disparadas}")
    print(f"Ciclos: {ciclo-1}")
    print("\nMemoria final:")
    for clave, valor in sorted(hechos.items()):
        print(f"  {clave}: {valor}")
    
    return hechos

# ===== PRUEBAS =====
def probar_escenario(nombre, hechos_prueba):
    print(f"\n{'='*70}")
    print(f"ESCENARIO: {nombre}")
    print(f"{'='*70}")
    resultado = forward_chaining(hechos_prueba, reglas)
    
    if resultado.get("bloquear_tarjeta", False):
        print("\n🔒 TARJETA BLOQUEADA - FRAUDE")
        if resultado.get("notificar_seguridad", False):
            print("📢 Notificación enviada")
    elif resultado.get("posible_fraude", False):
        print("\n⚠️ POSIBLE FRAUDE - VERIFICAR")
    elif resultado.get("transaccion_inusual", False):
        print("\nℹ️ TRANSACCIÓN INUSUAL - MONITOREAR")
    else:
        print("\n✅ TRANSACCIÓN NORMAL")
    
    return resultado

# ===== EJECUCIÓN =====
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("SISTEMA DE DETECCIÓN DE FRAUDE")
    print("=" * 70)
    
    # Escenario 1
    escenario1 = {
        "monto_transaccion": 7500,
        "pais_extranjero": True,
        "tarjeta_activa": True,
        "intentos_fallidos": 1,
        "dispositivo_confiable": True
    }
    probar_escenario("Alto monto + extranjero", escenario1)
    
    # Escenario 2
    escenario2 = {
        "monto_transaccion": 100,
        "pais_extranjero": False,
        "tarjeta_activa": True,
        "intentos_fallidos": 4,
        "dispositivo_confiable": False
    }
    probar_escenario("Intentos fallidos", escenario2)
    
    # Escenario 3
    escenario3 = {
        "monto_transaccion": 50,
        "pais_extranjero": False,
        "tarjeta_activa": True,
        "intentos_fallidos": 0,
        "dispositivo_confiable": True
    }
    probar_escenario("Transacción normal", escenario3)
    
    # Escenario 4
    escenario4 = {
        "monto_transaccion": 8000,
        "pais_extranjero": True,
        "tarjeta_activa": True,
        "intentos_fallidos": 0,
        "dispositivo_confiable": True
    }
    probar_escenario("Alto monto + extranjero (encadenamiento)", escenario4)
    
    print("\n" + "=" * 70)
    print("FIN")
    print("=" * 70)