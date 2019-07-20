import numpy as np

N = 760
b = np.random.random_integers(0,100,size=(N,N))
b_symm = (b + b.T)/2

for x in np.nditer(b_symm, op_flags = ['readwrite']):
	if x < 80:
		x[...] = 0
	else:
		x[...] = 1

for x in range(N):
	b_symm[x][x] = 1
print(b_symm)
