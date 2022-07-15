import matplotlib as plt
import random
import numpy as np

POPULATION_SIZE = 10

class Individual:
    '''
    Class representing individual in population
    '''
    def _init_(self,gene):
        self.gene = int(gene)
        self.fitness =int(-((gene)//10 + (gene)%10))

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        # global GENES
        gene = int(10*random.randint(1,95)+random.randint(1,5))
        return gene
    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        return self.mutated_genes()
    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
  
        prob = random.random()

        if prob < 0.20:
            child_chromosome=self.gene//10+par2.gene%10
        elif prob < 0.40:
            child_chromosome=par2.gene//10+self.gene%10
        elif prob < 0.60:
            child_chromosome=self.gene//10+self.gene%10
        elif prob < 0.80 :
            child_chromosome=par2.gene//10+par2.gene%10
        else:
            return Individual(self.mutated_genes())
        return Individual(child_chromosome)
    
generation = 1

found = False
population = []

# g=Genes(random.randint(0,95),random.randint(0,5))
# create initial population
for _ in range(POPULATION_SIZE):
            gnome = Individual.create_gnome();
            population.append(Individual(gnome))
# print(type([population[0]]))
while not found:

    population = sorted(population, key = lambda x : x.fitness, reverse=False)

    if population[0].fitness ==-100 :
        found = True
        break

    new_generation = []

    s = int((10*POPULATION_SIZE)/100)
    new_generation.extend(population[:s])

    s = int((90*POPULATION_SIZE)/100)
    for _ in range(s):
        parent1 = random.choice(population[:50])
        parent2 = random.choice(population[:50])
        child = parent1.mate(parent2)
        new_generation.append(child)

    population = new_generation

   
    print("Generation: {}\tSkill: {}\tLuck: {}\tFitness: {}".\
    format(generation,(population[0].gene//10),population[0].gene%10,
    -population[0].fitness))


    generation += 1

    
print("Generation: {}\tSkill: {}\tLuck: {}\tFitness: {}".\
    format(generation,population[0].gene//10,population[0].gene%10,-population[0].fitness))
