import numpy as np

class ColoniaHormigas:
    def __init__(self, distancias, n_hormigas, n_mejores, n_iteraciones, evaporacion, alfa=1, beta=1):
        self.distancias = distancias
        self.feromonas = np.ones(self.distancias.shape) / len(distancias)
        self.todos_indices = range(len(distancias))
        self.n_hormigas = n_hormigas
        self.n_mejores = n_mejores
        self.n_iteraciones = n_iteraciones
        self.evaporacion = evaporacion
        self.alfa = alfa
        self.beta = beta

    def ejecutar(self):
        camino_mas_corto = None
        mejor_camino_todos_tiempos = ("placeholder", np.inf)
        for i in range(self.n_iteraciones):
            todos_caminos = self.generar_todos_caminos()
            self.esparcir_feromonas(todos_caminos, self.n_mejores, camino_mas_corto=camino_mas_corto)
            camino_mas_corto = min(todos_caminos, key=lambda x: x[1])
            if camino_mas_corto[1] < mejor_camino_todos_tiempos[1]:
                mejor_camino_todos_tiempos = camino_mas_corto            
            self.feromonas *= self.evaporacion            
        return mejor_camino_todos_tiempos

    def esparcir_feromonas(self, todos_caminos, n_mejores, camino_mas_corto):
        caminos_ordenados = sorted(todos_caminos, key=lambda x: x[1])
        for camino, dist in caminos_ordenados[:n_mejores]:
            for movimiento in camino:
                self.feromonas[movimiento] += 1.0 / self.distancias[movimiento]

    def generar_distancia_camino(self, camino):
        distancia_total = 0
        for ele in camino:
            distancia_total += self.distancias[ele]
        return distancia_total

    def generar_todos_caminos(self):
        todos_caminos = []
        for i in range(self.n_hormigas):
            camino = self.generar_camino(0)
            todos_caminos.append((camino, self.generar_distancia_camino(camino)))
        return todos_caminos

    def generar_camino(self, inicio):
        camino = []
        visitados = set()
        visitados.add(inicio)
        anterior = inicio
        for i in range(len(self.distancias) - 1):
            movimiento = self.elegir_movimiento(self.feromonas[anterior], self.distancias[anterior], visitados)
            camino.append((anterior, movimiento))
            anterior = movimiento
            visitados.add(movimiento)
        camino.append((anterior, inicio))  # regresa al inicio    
        return camino

    def elegir_movimiento(self, feromonas, dist, visitados):
        feromonas = np.copy(feromonas)
        feromonas[list(visitados)] = 0

        fila = feromonas ** self.alfa * (( 1.0 / dist) ** self.beta)

        fila_normalizada = fila / fila.sum()
        movimiento = np_choice(self.todos_indices, 1, p=fila_normalizada)[0]
        return movimiento

def np_choice(a, size, replace=True, p=None):
    return np.random.choice(a, size, replace, p)

# Matriz 
distancias = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])

colonia_hormigas = ColoniaHormigas(distancias, 3, 1, 100, 0.95, alfa=1, beta=2)
camino_mas_corto = colonia_hormigas.ejecutar()
print("Ruta más corta encontrada: {}".format(camino_mas_corto))
