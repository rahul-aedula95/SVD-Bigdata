import numpy as np
from random import randint

a = np.zeros(shape=(10000,10000))

for i in xrange(0,10000):
    for j in xrange(0,10000):
        a[i][j] = randint(0,9)

with open('testnah.txt','w') as f:
      np.savetxt(f, a, fmt='%0.2f')

print "done" 
