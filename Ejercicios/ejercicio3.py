# ==========================================
# Nombre del archivo: ejercicio3.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: José Daniel Martínez Rojas
# Fecha: 22 de noviembre de 2026
# Versión: 1.0
# Propósito: Sistema de consola para la administración de un 
#            estacionamiento privado con capacidad de 20 espacios, 
#            menú interactivo (while True), control de ingresos, 
#            salidas, cobro por horas (800 por hora) y consultas 
#            de ocupación y recaudación.
# ==========================================

# Constantes
CAPACIDAD_MAXIMA = 20  # Constante capacidad maxima
TARIFA_HORA = 800      # Constante de cobro por hora

# Variables iniciales del estacionamiento
espacios_ocupados = 0
salidas_registradas = 0
recaudacion_total = 0

# Ciclo principal del menú
while True:
    print("\n--- SISTEMA DE ESTACIONAMIENTO ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        # Validar que no rebase los 20 espacios
        if espacios_ocupados < CAPACIDAD_MAXIMA:
            espacios_ocupados += 1
            print(f"¡Ingreso registrado! Espacios ocupados: {espacios_ocupados}/20")
        else:
            print("Lo sentimos, el parqueo está lleno.")

    elif opcion == 2:
        # Verificar que haya al menos un carro adentro para poder sacarlo
        if espacios_ocupados > 0:
            espacios_ocupados -= 1
            salidas_registradas += 1

            # Pedir y validar que las horas sean mayores a 0
            horas = int(input("Ingrese la cantidad de horas que estuvo estacionado: "))
            while horas <= 0:
                print("Error: La cantidad de horas debe ser mayor a 0.")
                horas = int(input("Ingrese la cantidad de horas que estuvo estacionado: "))

            subtotal = horas * TARIFA_HORA
            recaudacion_total += subtotal
            print(f"¡Salida registrada! Total a pagar por este vehículo: ₡{subtotal}")
        else:
            print("Error: El estacionamiento está vacío, no hay vehículos que registrar.")

    elif opcion == 3:
        # Consultar ocupación actual
        espacios_libres = CAPACIDAD_MAXIMA - espacios_ocupados
        print("\n--- Estado de Ocupación ---")
        print(f"Vehículos estacionados actualmente: {espacios_ocupados}")
        print(f"Espacios libres disponibles: {espacios_libres}")

    elif opcion == 4:
        # Consultar recaudación total
        print("\n--- Reporte de Recaudación ---")
        print(f"Total de salidas procesadas: {salidas_registradas}")
        print(f"Recaudación total acumulada: ₡{recaudacion_total}")

    elif opcion == 5:
        # Salir del sistema
        print("\nSaliendo del sistema de estacionamiento. ¡Hasta luego!\n")
        break

    else:
        print("\nOpción inválida. Por favor seleccione un número entre 1 y 5.\n")