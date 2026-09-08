# Diccionario con el estado del servidor (4 métricas técnicas)
servidor_estado = {
    "cpu_uso": 75,          # Porcentaje de uso de CPU
    "memoria_libre": 512,   # Memoria libre en MB
    "ping_respuesta": True, # True si responde al ping
    "temperatura": 82,      # Temperatura en grados Celsius
    "ventilador_encendido": False  # (extra para regla crítica)
}

def diagnosticar_servidor(hechos):
    """
    Función que aplica reglas lógicas anidadas para diagnosticar el servidor.
    """
    # Extraer valores del diccionario
    cpu = hechos.get("cpu_uso", 0)
    memoria = hechos.get("memoria_libre", 0)
    ping = hechos.get("ping_respuesta", False)
    temp = hechos.get("temperatura", 0)
    ventilador = hechos.get("ventilador_encendido", True)

    # ---- REGLA 1: Estado CRÍTICO ----
    if temp > 80 and not ventilador:
        diagnostico = "⚠️ CRÍTICO: Temperatura muy alta ({}°C) y ventilador apagado. ¡Apagar servidor inmediatamente!".format(temp)
        # Además, se puede agregar una subregla interna (anidada)
        if cpu > 90:
            diagnostico += " Además, la CPU está al {}%, posible sobrecarga térmica.".format(cpu)
        elif cpu > 70:
            diagnostico += " La CPU está alta ({}%), revisar procesos.".format(cpu)
        # Fin de anidación

    # ---- REGLA 2: Estado de ADVERTENCIA ----
    elif cpu > 80 and memoria < 300:
        diagnostico = "⚠️ ADVERTENCIA: CPU alta ({}%) y poca memoria libre ({} MB). Considere ampliar RAM o revisar procesos.".format(cpu, memoria)
        # Anidación: verificar si el ping también falla
        if not ping:
            diagnostico += " Además, el servidor no responde al ping, puede estar sobrecargado."

    elif temp > 70 and memoria < 200:
        diagnostico = "⚠️ ADVERTENCIA: Temperatura elevada ({}°C) y memoria muy baja. Revise refrigeración y cierre aplicaciones.".format(temp)

    # ---- REGLA 3: Estado NORMAL con posible revisión ----
    elif ping and cpu < 60 and memoria > 500:
        diagnostico = "✅ NORMAL: El servidor funciona correctamente (CPU {}%, Memoria {} MB libre, ping OK).".format(cpu, memoria)
        # Anidación: si la temperatura está entre 50 y 70, sugerir revisión preventiva
        if 50 <= temp <= 70:
            diagnostico += " Sugerencia: Temperatura en rango medio ({}°C), revise ventilación preventiva.".format(temp)

    # ---- REGLA 4: Otros casos (fallo de ping o valores atípicos) ----
    else:
        diagnostico = "🔍 REVISIÓN: El servidor presenta condiciones no críticas pero anormales. "
        if not ping:
            diagnostico += "No responde al ping. "
        if cpu > 70:
            diagnostico += "CPU alta ({}%). ".format(cpu)
        if memoria < 400:
            diagnostico += "Memoria baja ({} MB). ".format(memoria)
        if temp > 60:
            diagnostico += "Temperatura elevada ({}°C).".format(temp)
        if diagnostico.endswith(". "):  # Si no se agregó nada, poner mensaje genérico
            diagnostico = "ℹ️ INFORMATIVO: Todos los valores dentro de rangos aceptables, pero sin coincidir con reglas específicas."

    return diagnostico

# ---- PROBANDO EL SISTEMA CON DIFERENTES ESCENARIOS ----

print("=== DIAGNÓSTICO INICIAL (estado crítico) ===")
print(diagnosticar_servidor(servidor_estado))
print("\n" + "="*50 + "\n")

# Caso 1: Cambiar a estado de advertencia (CPU alta y poca memoria)
servidor_estado2 = {
    "cpu_uso": 85,
    "memoria_libre": 250,
    "ping_respuesta": True,
    "temperatura": 60,
    "ventilador_encendido": True
}
print("=== CASO 1: ADVERTENCIA (CPU alta, poca memoria) ===")
print(diagnosticar_servidor(servidor_estado2))
print("\n" + "="*50 + "\n")

# Caso 2: Estado normal con sugerencia de ventilación (temperatura media)
servidor_estado3 = {
    "cpu_uso": 45,
    "memoria_libre": 1024,
    "ping_respuesta": True,
    "temperatura": 65,
    "ventilador_encendido": True
}
print("=== CASO 2: NORMAL con sugerencia preventiva ===")
print(diagnosticar_servidor(servidor_estado3))
print("\n" + "="*50 + "\n")

# Caso 3: Sin ping y valores mixtos (entra al else)
servidor_estado4 = {
    "cpu_uso": 30,
    "memoria_libre": 600,
    "ping_respuesta": False,
    "temperatura": 55,
    "ventilador_encendido": True
}
print("=== CASO 3: REVISIÓN (falla de ping) ===")
print(diagnosticar_servidor(servidor_estado4))
print("\n" + "="*50 + "\n")

# Caso 4: Otro crítico (temperatura > 80 y ventilador apagado, con CPU alta)
servidor_estado5 = {
    "cpu_uso": 92,
    "memoria_libre": 800,
    "ping_respuesta": True,
    "temperatura": 88,
    "ventilador_encendido": False
}
print("=== CASO 4: CRÍTICO (temperatura muy alta, ventilador apagado, CPU alta) ===")
print(diagnosticar_servidor(servidor_estado5))