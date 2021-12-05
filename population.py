class Population():
  def __init__(self, total_population, initial_infected, vaccinated):
    #raw----------------------------------------------------------------
    self.total_population = total_population
    self.initial_infected = initial_infected

    #percentages of total pop-------------------------------------------
    
    self.vaccinated = vaccinated/total_population
    self.infected = initial_infected/total_population
    self.recovered = 0/total_population
    self.suseptable = 1 - self.infected - self.vaccinated
    self.dead = 0/total_population
    self.immune = self.recovered + self.vaccinated
    self.alive_population = total_population