class Virus():
  def __init__(self, name, reproduction_rate, mortality_rate, recovery_time):
    self.name = name
    self.reproduction_rate = reproduction_rate
    self.mortality_rate = mortality_rate
    self.recovery_time = recovery_time
    self.recovery_rate = (1-mortality_rate)