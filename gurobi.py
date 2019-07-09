from gurobipy import *
import pandas as pd
import math

df = pd.read_csv('Assignment 3 Data.csv')

df.x = df.x.astype('float')
df.y = df.y.astype('float')

def eculidian_distance(c,d):
    a=int(c)-1
    b=int(d)-1
    answer = math.sqrt((df.iloc[a,1]-df.iloc[b,1])**2 + (df.iloc[a,2]-df.iloc[b,2])**2)
    return answer

print(eculidian_distance(2,3))

trans_distances=[]
	
for a in range(9):
	single_distances = []
	for b in range(9):
		single_distances.append([eculidian_distance(a,b)])
	trans_distances =  trans_distances.append(single_distances)

#df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(trans_distances)


m = Model()

x=m.addVars(location,vtype=GRB.BINARY)

#m.setObjective(quicksum(cost[j]*x[j]for j infood),GRB.MINIMIZE)


nut_infood={('Nutrient1','Food1'):2,('Nutrient1','Food2'):0,('Nutrient1','Food3'):3,('Nutrient1','Food4'):1,('Nutrient1','Food5'):2,('Nutrient2','Food1'):0,('Nutrient2','Food2'):1,('Nutrient2','Food3'):2,('Nutrient2','Food4'):2,('Nutrient2','Food5'):1,}
print(nut_infood[('Nutrient1','Food1')])