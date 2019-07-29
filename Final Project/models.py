from Data_Generation import *
from gurobipy import *

class models:
	def __init__ (self,sites_covered,station_capacity,station_cost,district_demand,budget,district_weight):

		self.sites_covered = sites_covered

	def set_covering(self):

		numR = len(self.sites_covered)
		m = Model()
		f = {} # Binary variables for each fire station
		r = {} # Binary variable for each region

		for i in range(numR):
			f[i] = m.addVar(vtype=GRB.BINARY, name="fire station %d" % i)

		for j in range(numR):
			r[j] = m.addVar(vtype=GRB.BINARY, name="region covered%d" % j)

		m.update()

		for j in range(numR):
			m.addConstr(quicksum(f[i] for i in range(numR) if self.sites_covered[i][j]==1) >= r[j])

		for j in range(numR):
			m.addConstr(r[j] == 1)

		m.setObjective(quicksum(f[i] for i in range(numR)), GRB.MINIMIZE)

		m.optimize()

		self.set_covering_model = m

	def maximal_covering(self):

		numR = len(self.sites_covered)

		m = Model()

		f = {} # Binary variables for each fire station
		r = {} # Binary variable for each region

		for i in range(numR):
			f[i] = m.addVar(vtype=GRB.BINARY, name="fire station %d" % i)

		for j in range(numR):
			r[j] = m.addVar(vtype=GRB.BINARY, name="region covered%d" % j)

		m.update()

		for j in range(numR):
			m.addConstr(quicksum(f[i] for i in range(numR) if self.sites_covered[i][j]==1) >= r[j])

		m.addConstr(quicksum(f[i] for i in range(numR))<=5)

		m.setObjective(quicksum(r[i] for i in range(numR)), GRB.MAXIMIZE)

		m.optimize()

		self.maximal_covering_model = m

	def facility_location_set_covering(self):

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
			m.addConstr(quicksum(x[(i,j)] for i in range(numR)) == district_demand[j])

		#only one fire station per region
		for i in range(numR):
			m.addConstr(quicksum(f[(i,k)] for k in range(numK))<=1)

		#objective function
		m.setObjective(quicksum(f[(i,k)]*q[k] for i in range(numR) for k in range(numK)), GRB.MINIMIZE)

		m.optimize()

		self.facility_location_set_covering_model = m

	def facility_location_maximal_covering(self):

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

		self.facility_location_maximal_covering_model = m

	def facility_location_maximal_covering_weighted(self):

		numR = len(sites_covered)
		numK = len(station_capacity)

		f = {} # Binary variables for each fire station
		x = {} # Units shipped from i to j
		c = {} # Fire station capacity
		q = {} # Fire station cost
		w = {} # District weights

		m=Model()

		for j in range(numR):
			w[j] = district_weight[j]

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
		m.setObjective(quicksum(x[(i,j)]*w[j] for i in range(numR) for j in range(numR)), GRB.MAXIMIZE)

		m.optimize()

		self.facility_location_maximal_covering_weighted_model = m


sites_covered = symm(100,80).getMatrix()
budget = 10000000
station_capacity = [1314000,1095000,876000,438000]
station_cost =[1018413,809150,704519,599887]
district_demand = demand(368000,184735,40).getMatrix()
sites_covered = symm(30,80).getMatrix()
district_weight = weightings(1,0.5,30).getMatrix()

m=models(sites_covered, station_capacity,station_cost,district_demand,budget,district_weight)
m.set_covering()
m.maximal_covering()
m.facility_location_set_covering()
m.facility_location_maximal_covering()
m.facility_location_maximal_covering_weighted()

