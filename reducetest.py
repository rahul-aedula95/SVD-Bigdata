#!/usr/bin/python
import sys
import numpy as np
a = np.zeros(shape=(1000,1001))
a = np.loadtxt(sys.stdin)
x = np.zeros(shape=(1000,1000),dtype=complex)
u = np.zeros(shape=(1000,1000),dtype=complex)
s = np.zeros(shape=(1000,1000))#,dtype=complex)
v = np.zeros(shape=(1000,1000),dtype=complex)
for i in range(0,1000):
    for j in range(0,1000):
        x[i][j]=a[i][j+1]


u,s,v =  np.linalg.svd(x)
np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)
#np.savetext(sys.stdout.write(),u,fmt='%0.2f')
#print u
    
print
print
print s
print
print  
#print v

