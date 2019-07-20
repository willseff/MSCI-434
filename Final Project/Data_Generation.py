import numpy as np

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


class demand:
	def __init__(self,mu,sigma,size):
		self.demand = np.random.normal(mu, sigma, size)

	def getMatrix(self):
		return self.demand