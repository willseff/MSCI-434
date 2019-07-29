import numpy as np
import pandas as pd

#this class create a square symmetric matrix of ones and zeroes with the size and p(0) as parameters
class symm:
	def __init__(self, size,rate):
		N = size
		b = np.random.random_integers(0,100,size=(N,N))
		self.b_symm = (b + b.T)/2

		for x in np.nditer(self.b_symm, op_flags = ['readwrite']):
			if x < rate:
				x[...] = 0
			else:
				x[...] = 1

		for x in range(N):
			self.b_symm[x][x] = 1


	def getMatrix(self):
		return self.b_symm

#creates random demand
class demand:
	def __init__(self,mu,sigma,size):
		self.demand = np.random.normal(mu, sigma, size)
		self.demand =np.ceil(self.demand)

	def getMatrix(self):
		return self.demand

#creates random weightings
class weightings:
	def __init__(self,mu,sigma,size):
		self.weights = np.random.normal(mu,sigma,size)

	def getMatrix(self):
		return self.weights


class data:
	def __init__ (self,size,rate,demand_mu,demand_sigma,weight_mu,weight_sigma):
		#create symmetrical matrix
		N = size
		b = np.random.random_integers(0,100,size=(N,N))
		self.b_symm = (b + b.T)/2

		for x in np.nditer(self.b_symm, op_flags = ['readwrite']):
			if x < rate:
				x[...] = 0
			else:
				x[...] = 1

		for x in range(N):
			self.b_symm[x][x] = 1

		#create random demand
		self.demand = np.random.normal(demand_mu, demand_sigma, size)
		self.demand =np.ceil(self.demand)

		#create random weights
		self.weights = np.random.normal(weight_mu,demand_sigma,size)

