#this is a program to simulate eigen
import math
import numpy as np
x=[[2,1],[0,1]]
y=[0,0]
for i in range(0,1): 
   y[i]= np.linalg.eigvals(x)
   print y[i]


