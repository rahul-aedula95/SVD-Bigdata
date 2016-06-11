import sys
import numpy as np
from mrjob.job import MRJob
class SVDtest(MRJob):
      def mapper(self):
          b = np.zeros(shape=(2,3))
          b = np.loadtxt(sys.stdin)
          c = np.zeros(shape=(2,3))
          key = 1
          for i in range(0,2):
              c[i][0] = key
              key = key+1

          for k in range(0,2):
              for l in range(0,2):
                  c[k][l+1] = b[k][l]



          for m in range(0,2):
              for n in range(0,3):
                  sys.stdout.write("%.2f\t"%(np.array(c[m][n]),))
              print
      def reducer(self):
          a = np.zeros(shape=(2,3))
          a = np.loadtxt(sys.stdin)
          x = np.zeros(shape=(2,2),dtype=complex)
          for i in range(0,2):
              for j in range(0,2):

                  x[i][j]=a[i][j+1]


          u,s,v = np.linalg.svd(x,full_matrices=True)
          print u
          print s
          print v
if __name__ == '__main__':
   SVDtest.run()
