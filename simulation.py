#python3 simulation.py 10000 2 0 COVID 3 0.016 2
#run data for covid^

import random, sys
from population import Population
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
    
    if self.population.total_population == (self.population.dead + self.population.immune + self.population.suseptable)*total_population:
      print('simulation ended because there are no infected',file=open('logger.txt', 'a'))
      return False

    
    elif self.population.immune/self.population.alive_population >= self.herd_immunity:
      print('herd immunity has been reached, infected population will dwindle',file=open('logger.txt', 'a'))
      # if self.population.infected < 0.005:
      #   print('simulation ended because the infected population has become negligable',file=open('logger.txt', 'a'))
      #   return False
      return False
      
    
    else:
      return True

# RATES ---------------------------------------------------------------------------------------------------

  def change(self):

    for person in range(round(self.population.suseptable*self.population.total_population)):
      change_1 = (self.virus.reproduction_rate*self.population.suseptable*self.population.infected)/10

      #the quotient represents a time weighting
      if change_1 > self.population.suseptable:
        change_1 = self.population.suseptable
      infection = [0,1]
      person = random.choices(infection, weights = [1-change_1, change_1], k = 1)
      self.population.suseptable -= person[0]/self.population.total_population
      self.population.infected += person[0]/self.population.total_population
    

    for person in range(round(self.population.infected*self.population.total_population)):
      change_2 = (self.population.infected*self.virus.recovery_rate)/(self.virus.recovery_time)
      recovery = [0,1]
      person = random.choices(recovery, weights = [1-change_2, change_2], k = 1)
      self.population.infected -= person[0]/self.population.total_population
      self.population.recovered += person[0]/self.population.total_population
    
    for person in range(round(self.population.infected*self.population.total_population)):
      change_3 = self.population.infected*self.virus.mortality_rate/(0.9*self.virus.recovery_time)
      death = [0,1]
      person = random.choices(death, weights = [1-change_3, change_3], k = 1)
      self.population.dead += person[0]/self.population.total_population
      self.population.infected -= person[0]/self.population.total_population

    pass

  def run(self):
    t = 0
    while self.simulation_end_check() == True:
      t+=1
      self.calcualte_alive()
      self.calculate_immune()
      data = (
        f"---------------- week: {t} ----------------\n"
        f"suseptable: {round(self.population.suseptable*total_population)}\n"
        f"infected: {round(self.population.infected*total_population)}\n"
        f"dead: {round(self.population.dead*total_population)}\n"
        f"immune: {round(self.population.immune*total_population)}\n"
        f"percent immune: ~{round(100*self.population.immune/(self.population.suseptable+self.population.infected+self.population.immune))}% of people alive\n"
        f"herd immunity: ~{round(100*self.herd_immunity)}% of people alive\n"
      )
      
      #log data -----------------------------------------------------------------------------------------------
      print(data, file=open('logger.txt', 'a'))
      
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

  print("---------------- week: 0 ----------------\n"
  f"Total Population: {simulation.population.total_population}\n"
  f"Initial Infected: {simulation.population.initial_infected}\n"
  f"Vaccinated Individuals: {simulation.population.vaccinated*simulation.population.total_population}\n\n"
  f"Population is infected with {simulation.virus.name}\n"
  f"{simulation.virus.name} has a reproduction rate of {simulation.virus.reproduction_rate} and a mortality rate of {simulation.virus.mortality_rate*100}%\n",
  file=open('logger.txt', 'w')
  )
  

  simulation.run()

  print("---------To Reach This Point---------\n"
  f"{simulation.virus.name} killed {round(simulation.population.dead*1000)/10}% of the population, {round(simulation.population.dead/(simulation.population.dead+simulation.population.immune)*1000)/10}% of those who contracted the virus\n"
  f"{round(simulation.population.suseptable*100)}% of the population never contracted {simulation.virus.name}\n",
  file=open('logger.txt', 'a')
  )