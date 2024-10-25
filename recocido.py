import math
import random

def funcion_objetivo(x):
    return x**2

def generar_vecino(x):
    return x + random.uniform(-1, 1)

def recocido_simulado(temperatura_inicial, enfriamiento, iteraciones):
    solucion_actual = random.uniform(-10, 10)
    mejor_solucion = solucion_actual
    temperatura = temperatura_inicial

    for i in range(iteraciones):
        vecino = generar_vecino(solucion_actual)
        delta_e = funcion_objetivo(vecino) - funcion_objetivo(solucion_actual)

        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / temperatura):
            solucion_actual = vecino

        if funcion_objetivo(solucion_actual) < funcion_objetivo(mejor_solucion):
            mejor_solucion = solucion_actual

        temperatura *= enfriamiento

    return mejor_solucion

# Parámetros del algoritmo
temperatura_inicial = 1000
enfriamiento = 0.99
iteraciones = 1000

mejor_solucion = recocido_simulado(temperatura_inicial, enfriamiento, iteraciones)
print(f"La mejor solución encontrada es: {mejor_solucion}")
