from gurobipy import *
import pandas as pd
import math

def distance(a,b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  return math.sqrt(dx*dx + dy*dy)


locations = [[15,13],[8,2],[12,6],[9,20], [12,2],[5,19], [6,14], [20,16], [8,16], [18,11]]
monthly_num_trips = [80,45,75,30,15,75,70,85,10,85]

num_locations = len(locations)

m = Model()

x={}
n={}
d={}

for j in range(num_locations):
  x[j] = m.addVar(vtype=GRB.BINARY)
  n[j] = monthly_num_trips[j]

for i in range(num_locations):
  for j in range(num_locations):
    d[(i,j)] = distance(locations[i], locations[j])

m.update()

m.addConstr(quicksum(x[i]for i in range(num_locations)) == 1)

m.setObjective(quicksum(x[i]*d[i,j]*n[j] for i in range(num_locations) for j in range(num_locations)))

m.optimize()

