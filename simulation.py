import random, sys
random.seed(42)
from population import Population
from logger import Logger
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
  
  def create_virus(self, name, reproduction_rate, mortality_rate, recovery_time):
    
    self.virus = Virus(name, reproduction_rate, mortality_rate, recovery_time)
    
    return self.virus

  def calculate_herd_immunity(self):
    
    R_0 = self.virus.reproduction_rate/self.virus.recovery_rate
    self.herd_immunity = 1 - (1/R_0)
    
    return self.herd_immunity

  

































  def delta_suseptable(self):
    self.population.suseptable += -self.virus.reproduction_rate*self.population.suseptable*self.population.infected

  def delta_infected(self):
    self.population.infected += self.virus.reproduction_rate*self.population.suseptable*self.population.infected  
    '''- self.population.infected*virus.mortality_rate'''


  #add time element to delta recovery in run function
  def delta_recovered(self):
    #randomize through for loop
    self.population.recovered += self.population.infected*self.virus.recovery_rate
    self.population.infected -= self.population.infected*self.virus.recovery_rate
    # if t % virus recovery time == 0: then implement recovery
    pass

  def delta_dead(self):
     #randomize through for loop
    self.population.dead += self.population.infected*self.virus.mortality_rate
    pass

  def delta_immune(self):
    # test.immune += test.recovered + test.vaccinated
    pass





















  def simulation_end_check(self):
    
    if self.population.total_population == self.population.dead + self.population.immune:
      return False

    elif self.population.immune >= self.herd_immunity:
      return False
    
    else:
      return True

  def run(self):
    ''' This method should run the simulation until all requirements for ending
    the simulation are met.
    '''
    # TODO: Finish this method.  To simplify the logic here, use the helper method
    # _simulation_should_continue() to tell us whether or not we should continue
    # the simulation and run at least 1 more time_ste 
    # TODO: Keep track of the number of time steps that have passed.
    # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
    # TODO: Set this variable using a helper
    time_step_counter = 0
    should_continue = True  
    while should_continue == True:
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
        print(f'The simulation has ended after {time_step_counter} turns.')
        pass




























# if __name__ == "__main__":
#     params = sys.argv[1:]
#     virus_name = str(params[0])
#     repro_num = float(params[1])
#     mortality_rate = float(params[2])

#     pop_size = int(params[3])
#     vacc_percentage = float(params[4])

#     if len(params) == 6:
#         initial_infected = int(params[5])
#     else:
#         initial_infected = 1

    # virus = Virus(name, repro_rate, mortality_rate)
    # sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()




