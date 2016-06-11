import sys
import numpy as np
from mrjob.job import MRJob
class Test(MRJob):
      a = np.zeros(shape=(2,2))
   #   a = np.loadtxt(sys.stdin)
      
      def mapper(self,key,record):
          print Test.a   
         

if __name__  == '__main__':
   Test.run()
