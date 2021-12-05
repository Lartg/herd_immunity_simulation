import random, sys
from population import Population
# from logger import Logger
from virus import Virus

class Simulation():
  def __init__(self):
    self.logger = None
    self.population = None 
    self.virus = None
    self.herd_immunity = None
      
  def create_population(self, total_population, initial_infected, vaccinated):
    
    self.population = Population(total_population, initial_infected, vaccinated)

    return self.population
  
  def create_virus(self, virus_name, reproduction_rate, mortality_rate, recovery_time):
  
    self.virus = Virus(virus_name, reproduction_rate, mortality_rate, recovery_time)
    
    return self.virus

  def calculate_herd_immunity(self):
    
    R_0 = self.virus.reproduction_rate/(self.virus.recovery_rate)
    self.herd_immunity = 1 - (1/R_0)
    
    return self.herd_immunity

  def calculate_immune(self):

    self.population.immune = self.population.recovered + self.population.vaccinated
      
    return self.population.immune

  def calcualte_alive(self):
    self.population.alive_population = self.population.infected + self.population.suseptable + self.population.immune

  def simulation_end_check(self):
    
    if self.population.total_population - 5 == (self.population.dead + self.population.immune + self.population.suseptable)*total_population:
      print('simulation ended because there are no infected')
      return False

    # elif self.population.immune > 0:
    #   if self.population.immune/self.population.alive_population >= self.herd_immunity:
    #     print('simulation ended because herd immunity was reached')
        
    #     return False
    #   else:
    #     return True
    
    else:
      return True

# RATES ---------------------------------------------------------------------------------------------------

  def change(self):
    change_1 = self.virus.reproduction_rate*self.population.suseptable*self.population.infected
    change_2 = (self.population.infected*self.virus.recovery_rate)/(0.56*self.virus.recovery_time)
    change_3 = self.population.infected*self.virus.mortality_rate/(0.44*self.virus.recovery_time)

    if change_1 > self.population.suseptable:
      change_1 = self.population.suseptable

    for person in range(round(self.population.suseptable*self.population.total_population)):
      infection = [0,1]
      person = random.choices(infection, weights = [1-change_1, change_1], k = 1)
      self.population.suseptable -= person[0]/self.population.total_population
      self.population.infected += person[0]/self.population.total_population
    

    for person in range(round(self.population.infected*self.population.total_population)):
      recovery = [0,1]
      person = random.choices(recovery, weights = [1-change_2, change_2], k = 1)
      self.population.infected -= person[0]/self.population.total_population
      self.population.recovered += person[0]/self.population.total_population
    
    for person in range(round(self.population.infected*self.population.total_population)):
      death = [0,1]
      person = random.choices(death, weights = [1-change_3, change_3], k = 1)
      self.population.dead += person[0]/self.population.total_population
      self.population.infected -= person[0]/self.population.total_population

    pass


  

  def run(self):
    t = 0
    should_continue = True  
    while should_continue == True:
      t+=1
      self.calcualte_alive()
      self.calculate_immune()
      data = {
        'suseptable': round(self.population.suseptable*total_population),
        'infected': round(self.population.infected*total_population),
        'dead': round(self.population.dead*total_population),
        'immune': round(self.population.immune*total_population),
        'percent immune':round(100*self.population.immune/(self.population.suseptable+self.population.infected+self.population.immune)),
        'herd immunity': round(100*self.herd_immunity),
        'time': t
      }
      #log here
      print(data)
      
      should_continue = self.simulation_end_check()

      if t > 104:
        should_continue = False

      self.change()
      pass


if __name__ == "__main__":
  #------- get initial data from user in command line -------

  total_population = int(sys.argv[1])
  initial_infected = int(sys.argv[2])
  vaccinated = int(sys.argv[3])
  virus_name = sys.argv[4]
  reproduction_rate = float(sys.argv[5])
  mortality_rate = float(sys.argv[6])
  recovery_time = int(sys.argv[7])

  #-------- use data to init run -----------------------------

  simulation = Simulation()
  simulation.create_population(total_population, initial_infected, vaccinated)
  simulation.create_virus(virus_name, reproduction_rate, mortality_rate, recovery_time)
  simulation.calculate_herd_immunity()

  print(simulation.population.__dict__)
  print(simulation.virus.__dict__)

  simulation.run()