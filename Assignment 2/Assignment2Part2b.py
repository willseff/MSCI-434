from gurobipy import *
import pandas as pd
import math

def euclidean_distance(a,b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  return math.sqrt(dx*dx + dy*dy)


locations = [[15,13],[8,2],[12,6],[9,20], [12,2],[5,19], [6,14], [20,16], [8,16], [18,11]]
monthly_num_trips = [80,45,75,30,15,75,70,85,10,85]
cost_per_km = [4.2,4.7,4.8,3.1,3.3,3.3,5.0,4.8,4.4,3.9]

num_locations = len(locations)

m = Model()

x={}
n={}
d={}
c={}

for j in range(num_locations):
  x[j] = m.addVar(vtype=GRB.BINARY,name="facility location %d" % (j+1))
  n[j] = monthly_num_trips[j]
  c[j] = cost_per_km[j]

for i in range(num_locations):
  for j in range(num_locations):
    d[(i,j)] = euclidean_distance(locations[i], locations[j])

m.update()

m.addConstr(quicksum(x[i]for i in range(num_locations)) == 1)

m.setObjective(quicksum(x[i]*d[i,j]*n[j]*c[j] for i in range(num_locations) for j in range(num_locations)))

m.optimize()

for v in m.getVars():
	print('%s %g' % (v.varName, v.x))