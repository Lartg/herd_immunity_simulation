'''
need to rework so that all maths are based upon percentage of population, then applied to total poulation for output.
'''

class Population():
  def __init__(self, total_population, initial_infected, vaccinated):
    self.total_population = total_population
    self.initial_infected = initial_infected
    self.vaccinated = vaccinated
    self.infected = initial_infected/total_population
    self.recovered = 0
    #remove vaxxed in init from suseptable
    self.suseptable = 1 - self.infected
    self.immune = self.recovered + self.vaccinated
    self.dead = 0



