import matplotlib.pyplot as plt
import numpy as np

def graph(data):
  infected = []
  suseptable = []
  immune = []
  dead = []

  for datum in data:
    infected.append(datum['infected'])
    suseptable.append(datum['suseptable'])
    immune.append(datum['immune'])
    dead.append(datum['dead'])




  plt.plot(infected, label='Infected', color='r')
  plt.plot(suseptable, label='Suseptable', color='b')
  plt.plot(immune, label='Immune', color='g')
  plt.plot(dead, label='Dead', color='k')
  plt.legend(loc="upper left")
  plt.ylabel('People')
  plt.xlabel('Time')
  plt.title('Disease Progression')
  

  plt.show()