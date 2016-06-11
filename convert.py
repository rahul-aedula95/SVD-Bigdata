import numpy as np
import sys

a = np.zeros(shape=(1000,1000))
a = np.loadtxt('con.txt')

with open('con2.txt','w') as f:
      np.savetxt(f,a,fmt='%0.2f')

print done
