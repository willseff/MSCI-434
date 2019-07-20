import numpy as np

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

