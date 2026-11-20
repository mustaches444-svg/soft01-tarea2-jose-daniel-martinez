# soft01-tarea2-jose-daniel-martinez
Tarea 2 del curso Principios de Programación 1 (SOFT-01) en Universidad CENFOTEC: estructuras iterativas en Python, laboratorios guiados y documentación

# Tarea 2 — Estructuras iterativas en Python (`SOFT-01`)

## Descripción
Solución de la Tarea 2 del curso **Principios de Programación 1 (SOFT-01)** en **Universidad CENFOTEC**, enfocada en el uso de estructuras iterativas (`while`, `for` con `range()`, menús con `while True`), validaciones de entrada, acumuladores, contadores e interrupción anticipada con `break`, junto con la documentación técnica, diagramas de flujo y laboratorios guiados de clase[cite: 6, 7, 14].

## Objetivos
* Seleccionar adecuadamente entre ciclos `while` y `for` según la naturaleza de la repetición[cite: 6].
* Diseñar ciclos con inicialización, condición de control, actualización y salida correctas, evitando ciclos infinitos o errores de límites[cite: 6, 7].
* Emplear acumuladores, contadores, validaciones de entrada y control de flujo (`break`) para obtener resultados verificables[cite: 6, 7].
* Documentar y comprobar cada algoritmo mediante tablas de variables, diagramas de flujo y casos de prueba con evidencias[cite: 6, 7, 10, 14].

## Funcionalidades
* **Ejercicio 1 (`ejercicio1.py`):** Simulación de control de temperatura en una cámara experimental mediante ciclo `while`, validando temperatura objetivo mayor que la inicial e incremento estrictamente positivo, mostrando cada ciclo, total de ciclos y temperatura final.
* **Ejercicio 2 (`ejercicio2.py`):** Registro de consumo diario de agua durante 7 días con ciclo `for` y `range()`, validando valores mayores o iguales a cero y calculando total, promedio diario, consumo máximo y cantidad de días que superan los 150 litros[cite: 7, 8].
* **Ejercicio 3 (`ejercicio3.py`):** Sistema de consola para administrar un estacionamiento de 20 espacios a ₡800 por hora mediante menú con `while True`, controlando ingresos, salidas, validación de horas (> 0), consulta de ocupación, consulta de recaudación y salida con resumen[cite: 7, 9].
* **Ejercicio 4 (`ejercicio4.py`):** Simulación de abastecimiento de una expedición (150 L de agua y 100 u de alimento) para 1 a 30 jornadas, validando consumos positivos sin exceder existencias, actualizando saldos e interrumpiendo anticipadamente con `break` si algún recurso llega a cero[cite: 7, 10].
* **Laboratorios guiados:** Inclusión de los seis laboratorios desarrollados en clase en directorios independientes[cite: 7, 14].

## Requisitos previos
* **Python 3.x** instalado y configurado en el sistema (ejecución desde terminal o Visual Studio Code)[cite: 11].
* Lector de archivos **PDF** para consultar la documentación.
* *(Opcional)* **draw.io / diagrams.net** para abrir los diagramas en formato editable.

## Instrucciones de ejecución
1. Clonar o descargar este repositorio en tu equipo.
2. Abrir una terminal o **Visual Studio Code** dentro de la carpeta del proyecto[cite: 11].
3. Ejecutar cada ejercicio de forma independiente mediante consola:
   ```bash
   python ejercicio1.py
   python ejercicio2.py
   python ejercicio3.py
   python ejercicio4.py