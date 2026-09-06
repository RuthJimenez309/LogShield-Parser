# Definimos el límite: si una IP falla 5 o más veces, disparamos la alerta
UMBRAL_FALLOS = 5

def analizar_logs():
    print("==================================================")
    print(" LOGSHIELD-PARSER: MONITOREO DE SEGURIDAD ACTIVO")
    print("==================================================")
    
    # Diccionario para contar los fallos por cada dirección IP
    historial_fallos = {}

    # Abrimos el archivo de logs en modo lectura ('r' de read)
    with open("auth.log", "r") as archivo:
        for linea in archivo:
            # Si la línea registra un acceso fallido (STATUS: FAILED)
            if "STATUS: FAILED" in linea:
                # Extraemos la IP cortando el texto de la línea
                partes = linea.split(" ")
                ip = partes[3]  # La posición 3 corresponde a la dirección IP
                
                # Sumamos 1 al contador de esa IP específica
                historial_fallos[ip] = historial_fallos.get(ip, 0) + 1

    # Revisamos si alguna IP superó nuestro umbral de seguridad
    ataques_detectados = 0
    for ip, conteo in historial_fallos.items():
        if conteo >= UMBRAL_FALLOS:
            print(f"\n [ALERTA CRÍTICA] ¡Posible ataque de Fuerza Bruta detectado!")
            print(f" Origen sospechoso IP: {ip}")
            print(f" Intentos fallidos registrados: {conteo}")
            ataques_detectados += 1

    if ataques_detectados == 0:
        print("\n Análisis completado: No se detectaron patrones de ataque.")
    print("\n==================================================")

if __name__ == "__main__":
    analizar_logs()
