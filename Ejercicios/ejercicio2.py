# ==========================================
# Nombre del archivo: ejercicio2.py
# Curso: Principios de Programación 1 (SOFT-01)
# Autor: José Daniel Martínez Rojas
# Fecha: 22 de noviembre de 2026
# Propósito: Programa para registrar y procesar el consumo diario 
#            de agua durante 7 días consecutivos utilizando un ciclo for, 
#            calculando el total, el promedio, el consumo máximo y 
#            las jornadas que superan el umbral de 150 litros.[cite: 4, 7]
# ==========================================

# Variables acumuladoras

consumo_total = 0
mayor_consumo = 0
dias_mayor_150 = 0

print("\n")

for dia in range(1, 8):

    # Consumo del día actual
    consumo_dia = float(input(f"Ingrese el consumo de agua del día {dia} (en litros): "))
    consumo_total += consumo_dia
    
    # Evaluar si es el mayor consumo registrado hasta el momento
    if consumo_dia > mayor_consumo:
        mayor_consumo = consumo_dia
        
    # Verificar si supera estrictamente el umbral de 150 litros
    if consumo_dia > 150:
        dias_mayor_150 += 1

# Calculo del promedio en 7 dias 

promedio_diario = consumo_total / 7

# Resumen final del consumo
print("\n--- Resumen Semanal de Consumo de Agua ---")
print(f"Consumo total: {consumo_total} litros")
print(f"Promedio diario: {promedio_diario:.2f} litros")
print(f"Mayor consumo registrado: {mayor_consumo} litros")
print(f"Jornadas que superaron los 150 litros: {dias_mayor_150}\n")
    