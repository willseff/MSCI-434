from Data_Generation import *
from gurobipy import *

# this model will model the problem as a facility location problem with normally generated demands and facility costs
# no station capacities

station_data = [[1018413,13140],[809150,10950],[704519,8760],[599887,4380]]
district_demand = demand(2000,500,100).getMatrix()
sites_covered = symm(100,70).getMatrix()

numR = len(sites_covered)

f = {} # Binary variables for each fire station
x = {} # Units shipped from i to j

m=Model()

for i in range (numR):
	f[i] = m.addVar(vtype=GRB.BINARY, name="fire station %d" % i)

for i in range(numR):
	for j in range(numR):
		x[(i,j)] = m.addVar(vtype=GRB.INTEGER, name="units from %d to %d" % (i,j))

m.update()

for i in range(numR):
	m.addConstr(quicksum(x[(i,j)]for j in range(numR))<= 9999999999*f[i])

for i in range(numR):
	for j in range(numR):
		m.addConstr(x[(i,j)] <= 9999999999*sites_covered[i][j])

for j in range(numR):
	m.addConstr(quicksum(x[(i,j)] for i in range(numR)) == district_demand[j])

m.setObjective(quicksum(f[i] for i in range(numR)), GRB.MINIMIZE)

m.optimize()

for v in m.getVars():
	if (v.x != 0):	
		print('%s %g' % (v.varName, v.x))