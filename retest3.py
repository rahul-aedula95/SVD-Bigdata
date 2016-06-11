#!/usr/bin/python
import sys
import numpy as np
from subprocess import call
from StringIO import StringIO
a = np.zeros(shape=(1000,1001))
a = np.loadtxt(sys.stdin)
x = np.zeros(shape=(1000,1000))#,dtype=complex)
y = np.zeros(shape=(1000,1000))#,dtype=complex)
z = np.zeros(shape=(1000,1000))#,dtype=complex)
f = np.zeros(shape=(1000,1000))#,dtype=complex)
b = np.zeros(shape=(1000,4000))#,dtype=complex)
for i in range(0,1000):
    for j in range(0,1000):

        x[i][j]=a[i][j+1]

np.set_printoptions(threshold=np.nan)
np.set_printoptions(suppress=True)
#np.set_printoptions(linewidth=1000)
u,s,v = np.linalg.svd(x)
for m in range(0,1000):
    for n in range(0,1000):
        if(m==n):
          y[m][n]=s[m]

k = np.dot(u,y)
z = np.dot(x,np.transpose(v))
f = np.dot(np.linalg.inv(u),z)

for p in range(0,1000):
    tot1=0
    tot2=1
    tot3=2
    tot4=3
    for q in range(0,1000):
        b[p][tot1]=y[p][q]   
        b[p][tot2]=k[p][q]   
        b[p][tot3]=z[p][q]   
        b[p][tot4]=f[p][q]   
        tot1=tot1+4
        tot2=tot2+4
        tot3=tot3+4
        tot4=tot4+4
with open('conmat.txt','w') as f:
      np.savetxt(f, b,fmt='%f')

print "done"
              
