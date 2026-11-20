# ==========================================
# Nombre del archivo: ejercicio4.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: José Daniel Martínez Rojas
# Fecha: 22 de noviembre de 2026
# Versión: 1.0
# Propósito: Simulación de recursos de una expedición (150L de agua 
#            y 100 unidades de alimento) a lo largo de jornadas 
#            planificadas (1 a 30 días), validación de consumos diarios, 
#            descuento de existencias, interrupción anticipada 
#            con break si los recursos llegan a cero, y presentación 
#            de saldos restantes.
# ==========================================

# Variables de recursos iniciales (cambian conforme avanza la expedición)
agua_restante = 150
alimento_restante = 100

# Variable para la cantidad de jornadas
cantidad_jornadas = 0

# Solicitar y validar que las jornadas estén entre 1 y 30
while cantidad_jornadas < 1 or cantidad_jornadas > 30:
    cantidad_jornadas = int(input("Digite la cantidad de jornadas de la expedición (1-30): "))

# Ciclo principal para recorrer cada día de la expedición
for dia in range(1, cantidad_jornadas + 1):
    
    # Comprobar al iniciar el día si los recursos ya se habían agotado
    if agua_restante <= 0 or alimento_restante <= 0:
        print("\n¡Atención! Los suministros se han agotado por completo. La expedición termina anticipadamente.")
        break

    print(f"\n--- Día {dia} de {cantidad_jornadas} ---")
    print(f"Agua disponible: {agua_restante} L")
    print(f"Alimento disponible: {alimento_restante} u")

    # Validar el consumo de agua del día (debe ser mayor a 0 y no superar lo disponible)
    consumo_agua = int(input(f"Ingrese el consumo de agua para el día {dia}: "))
    while consumo_agua <= 0 or consumo_agua > agua_restante:
        print("Error: Consumo de agua inválido (debe ser mayor a 0 y menor o igual al agua actual).")
        consumo_agua = int(input(f"Ingrese el consumo de agua para el día {dia}: "))

    # Validar el consumo de alimento del día (debe ser mayor a 0 y no superar lo disponible)
    consumo_alimento = int(input(f"Ingrese el consumo de alimento para el día {dia}: "))
    while consumo_alimento <= 0 or consumo_alimento > alimento_restante:
        print("Error: Consumo de alimento inválido (debe ser mayor a 0 y menor o igual al alimento actual).")
        consumo_alimento = int(input(f"Ingrese el consumo de alimento para el día {dia}: "))

    # Descontar los consumos de los recursos actuales
    agua_restante -= consumo_agua
    alimento_restante -= consumo_alimento

    print(f"Saldo restante -> Agua: {agua_restante} L | Alimento: {alimento_restante} u")

    #Interrumpir anticipadamente con break si algún recurso llega exactamente a cero
    if agua_restante == 0 or alimento_restante == 0:
        print("\nLos recursos han llegado a exactamente cero. Interrupción anticipada de la expedición.")
        break

# Informe final de cierre de la expedición
print("\n==========================================")
print("          INFORME FINAL DE EXPEDICIÓN     ")
print("==========================================")
print(f"Jornadas totales planificadas: {cantidad_jornadas}")
print(f"Agua final restante: {agua_restante} L")
print(f"Alimento final restante: {alimento_restante} u")
print("¡Simulación finalizada con éxito!")
