#!/bin/bash

if hs matest1.py retest1.py etest gg; then
   
   if  hadoop fs -mv gg/part-00000 sample; then
     
       hs matest1.py rtest.py sample etout

fi

fi
