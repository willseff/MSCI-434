from gurobipy import *
import pandas as pd
import math

def euclidean_distance(a,b):
  dx = a[0] - b[0]
  dy = a[1] - b[1]
  return math.sqrt(dx*dx + dy*dy)


locations = [[15,13],[8,2],[12,6],[9,20], [12,2],[5,19], [6,14], [20,16], [8,16], [18,11]]
monthly_num_trips = [80,45,75,30,15,75,70,85,10,85]
dc_locations = []

for x in range(20):
	for y in range(20):
		dc_locations.append([x+1,y+1])

num_locations = len(locations)
num_dc_locations = len(dc_locations)
print(num_dc_locations)

m = Model()

x={}
n={}
d={}

for j in range(num_locations):
	n[j] = monthly_num_trips[j]

for i in range(num_dc_locations):
	x[i] = m.addVar(vtype=GRB.BINARY,name="facility location %d,%d" % (dc_locations[i][0],dc_locations[i][1]))

for i in range(num_dc_locations):
  for j in range(num_locations):
    d[(i,j)] = euclidean_distance(dc_locations[i], locations[j])

m.update()

m.addConstr(quicksum(x[i]for i in range(num_dc_locations)) == 1)

m.setObjective(quicksum(x[i]*d[i,j]*n[j] for i in range(num_dc_locations) for j in range(num_locations)),GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
	if v.x == 1:
		print('%s' % (v.varName))
