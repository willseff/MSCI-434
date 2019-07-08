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