import random

# (Funcion) Definir la función de aptitud
def fitness(individual):
    return sum(individual)

# (Funcion) Crear la población inicial
# Lo hace por medio de la lib "random" 
def create_population(size, length):
    return [[random.randint(0, 1) for _ in range(length)] for _ in range(size)]
    

# (Funcion) Selección por torneo
# De la población, se hace una selección por torneo y seleccionan las mejores 
def selection(population):
    return random.choices(population, k=2)

# (Funcion) Cruzamiento de un punto
# Se seleccionan los dos padres para mezclar sus genes 
def crossover(padre1, padre2):
    point = random.randint(1, len(padre1) - 1)
    return padre1[:point] + padre2[point:], padre2[:point] + padre1[point:]

# (Funcion) Mutación
def mutate(individual, mutation_rate):
    return [gen if random.random() > mutation_rate else 1 - gen for gen in individual]

# (Funcion) Algoritmo genético
def genetic_algorithm(pop_size, gene_length, generations, mutation_rate):
    
    population = create_population(pop_size, gene_length)
    
    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        next_generation = population[:pop_size // 2]
        while len(next_generation) < pop_size:
            parent1, parent2 = selection(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            next_generation.extend([mutate(offspring1, mutation_rate), mutate(offspring2, mutation_rate)])
        population = next_generation
    return max(population, key=fitness)

# Parámetros
population_size = 40    #Tamaño de la población
gene_length = 5        #N° de "bits" de cada individuo
generations = 3         #N° de generaciones para trabajar
mutation_rate = 0.01    #N°

# Ejecutar el algoritmo genético
best_individual = genetic_algorithm(population_size, gene_length, generations, mutation_rate)

print("Mejor individuo:", best_individual)
print("Aptitud:", fitness(best_individual))
