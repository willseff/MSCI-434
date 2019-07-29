from Data_Generation import *
from gurobipy import *

#model maximizes the number of districts covered with a constrained number of fire stations

data=symm(100,80)
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

m.addConstr(quicksum(f[i] for i in range(numR))<=5)

m.setObjective(quicksum(r[i] for i in range(numR)), GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
	if('fire station' in v.varName and v.x == 1):
		print('%s' % (v.varName))