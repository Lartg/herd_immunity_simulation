from population import Population

population = Population(100, 1, 0)

def calculate_immune(self):
      
      population.immune = population.recovered + population.vaccinated
      
      return self.population.immune