# ==========================================
# Nombre del archivo: ejercicio1.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: José Daniel Martínez Rojas
# Fecha: 22 de noviembre de 2026
# Propósito: Simulación del control de temperatura de una 
#            cámara experimental utilizando ciclos while y 
#            validaciones de entrada.
# ==========================================

# Datos de entrada

print()

temperatura_inicial = float(input("Introduzca la temperatura inicial en grados Celsius: "))
temperatura_objetivo = float(input("Ingrese la temperatura mínima que se desea alcanzar: "))
incremento = float(input("Aumento fijo entre cada ciclo de calentamiento: "))

print()

# Contador de ciclos
contador_ciclos = 0

if temperatura_objetivo > temperatura_inicial and incremento > 0:
    while temperatura_inicial < temperatura_objetivo:
        contador_ciclos += 1
        temperatura_inicial = temperatura_inicial + incremento
        print(f"Temperatura actual: {temperatura_inicial}°C, Ciclo: {contador_ciclos}")
        
    # El resumen final
    print("\n--- Resumen Final ---")
    print(f"Temperatura final alcanzada: {temperatura_inicial}°C")
    print(f"Número total de ciclos necesarios: {contador_ciclos}")
        
else:
    print("Error: La temperatura objetivo debe ser mayor a la inicial y el incremento debe ser estrictamente positivo (> 0). No se simuló el calentamiento.")

print()
