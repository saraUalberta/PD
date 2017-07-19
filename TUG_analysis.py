# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 19:34:01 2017

@author: sara
"""

import numpy as np
import glob
import csv
import pickle 
#import Kmean as km
from sklearn import cluster


dtlist=[]
for sub in glob.glob("*.txt"):
    #fname='TUG'+str(i+1)+'.txt'
    with open(sub) as f:
        lines = f.read().splitlines()
        
        content = ([x.strip().split('\t') for x in lines])
        tcontent = np.array(content)
        tcontent = tcontent[:,2:]
        
        datanew=[]#np.empty(tcontent.shape[0], dtype='<U32')
        for w in range(tcontent.shape[0]):
            currow=tcontent[w][:]
            newrow = [i for i in currow if i != '']
            newrow = np.array(newrow)
            datanew.append(newrow)
        datanew =  np.array(datanew)    
        dtlist.append(datanew)        
dtlist = np.array(dtlist)


## saving
# Saving the objects:
with open('TUGdata.pickle', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(dtlist, f)