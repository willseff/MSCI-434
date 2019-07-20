from Data_Generation import *
from gurobipy import *

#creates a model where every region is covered with the minimum number of fire stations
#modeled as a set covering problem

data=symm(100,70)
demand_data = demand(3000,1000,70).getMatrix()
print(demand_data)
sites_covered = data.getMatrix()

numR = len(sites_covered)

m = Model()

f = {} # Binary variables for each fire station
r = {} # Binary variable for each region


for i in range(numR):
	f[i] = m.addVar(vtype=GRB.BINARY, name="fire station %d" % i)

for j in range(numR):
	r[j] = m.addVar(vtype=GRB.BINARY, name="region covered%d" % j)

m.update()

for j in range(numR):
	m.addConstr(quicksum(f[i] for i in range(numR) if sites_covered[i][j]==1) >= r[j])

for j in range(numR):
	m.addConstr(r[j] == 1)

m.setObjective(quicksum(f[i] for i in range(numR)), GRB.MINIMIZE)

m.optimize()

#for v in m.getVars():
	#if('fire station' in v.varName and v.x == 1):
		#print('%s %g' % (v.varName, v.x))