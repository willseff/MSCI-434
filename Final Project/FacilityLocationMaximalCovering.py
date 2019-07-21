from Data_Generation import *
from gurobipy import *

#This will model as a capaciated facility location problem
#The model aims to maximize the number of demands supplied while staying below budget

budget = 5000000
station_capacity = [13140,10950,8760,4380]
station_cost =[1018413,809150,704519,599887]
district_demand = demand(2000,500,100).getMatrix()
sites_covered = symm(30,70).getMatrix()

numR = len(sites_covered)
numK = len(station_capacity)

f = {} # Binary variables for each fire station
x = {} # Units shipped from i to j
c = {} # Fire station capacity
q = {} # Fire station cost

m=Model()

for k in range(numK):
	c[k] = station_capacity[k]
	q[k] = station_cost[k]

for i in range (numR):
	for k in range (numK):
		f[(i,k)] = m.addVar(vtype=GRB.INTEGER, name="fire station at location %d type %d " % (i,k))

for i in range(numR):
	for j in range(numR):
		x[(i,j)] = m.addVar(vtype=GRB.INTEGER, name="units from %d to %d" % (i,j))

m.update()

#station capacities
for i in range(numR):
	m.addConstr(quicksum(c[k]*f[(i,k)] for k in range(numK))>= quicksum(x[(i,j)]for j in range(numR)))

# 5 minute range constraint
for i in range(numR):
	for j in range(numR):
		m.addConstr(x[(i,j)] <= 9999999999*sites_covered[i][j])

#demand is met
for j in range(numR):
	m.addConstr(quicksum(x[(i,j)] for i in range(numR)) <= district_demand[j])

#only one fire station per region
for i in range(numR):
	m.addConstr(quicksum(f[(i,k)] for k in range(numK))<=1)

#budget constraint
m.addConstr(quicksum(f[(i,k)]*q[k] for i in range(numR) for k in range(numK)) <= budget)

#objective function
m.setObjective(quicksum(x[(i,j)] for i in range(numR) for j in range(numR)), GRB.MAXIMIZE)

m.optimize()

for v in m.getVars():
	if (v.x != 0):
		print('%s %g' % (v.varName, v.x))