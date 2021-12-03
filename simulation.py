import random, sys
random.seed(42)
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
    
    R_0 = self.virus.reproduction_rate/self.virus.recovery_rate
    self.herd_immunity = 1 - (1/R_0)
    
    return self.herd_immunity

  def simulation_end_check(self):
    
    if self.population.total_population == self.population.dead + self.population.immune:
      return False

    elif self.population.immune >= self.herd_immunity:
      return False
    
    else:
      return True

































  def delta_suseptable(self):
    #randomize through for loop
    change = self.virus.reproduction_rate*self.population.suseptable*self.population.infected
    self.population.suseptable -= change
    self.population.infected += change
    
    pass

#-----------------------------------------------------------------------------------------------------------
  #add time element to delta recovery in run function
  # if t % virus recovery time == 0: then call delta_recovered
#-----------------------------------------------------------------------------------------------------------
  def delta_recovered(self):
    #randomize through for loop

    change = self.population.infected*self.virus.recovery_rate

    self.population.infected -= change
    self.population.recovered += change
    
    
    pass

  def delta_dead(self):
    #randomize through for loop
    change = self.population.infected*self.virus.mortality_rate
    self.population.dead += change
    self.population.infected -= change
    
    pass

  def calculate_immune(self):
    self.population.immune = self.population.recovered + self.population.vaccinated
    
    return self.population.immune


#-----------------------------------------------------------------------------------------------------------
 #multiply all outputs by total population to get stats
#-----------------------------------------------------------------------------------------------------------


















  



































 


  def run(self):
    t = 0
    print(5)
    should_continue = True  
    while should_continue == True:
      t+=1

      self.delta_suseptable()
      
      self.delta_dead()

      if t % self.virus.recovery_time == 0:
        self.delta_recovered()
      #   for person in range(self.population.infected*self.population.total_population):
          

      self.calculate_immune()

      data = {
        'suseptable': round(self.population.suseptable*total_population),
        'infected': round(self.population.infected*total_population),
        'dead': round(self.population.dead*total_population),
        'immune': round(self.population.immune*total_population),
        'time': t
      }

      print(data)
      should_continue = self.simulation_end_check()
      if t >20:
        should_continue = False
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