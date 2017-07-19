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
def orgrowtrem(newrow):
    orgdata=np.zeros(newrow.shape)
    orgdata[:,0]= newrow[:,3]
    orgdata[:,1]= newrow[:,5]
    orgdata[:,2]= newrow[:,23]
    #orgdata[:,2:3]=newrow[3],newrow[5],newrow[23]
    #orgdata[:,0:3]=newrow[3],newrow[5],newrow[23]
    return orgdata
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
            ## create formatted data row
            # dataorg= orgrowtrem(newrow)
            datanew.append(newrow)
        datanew =  np.array(datanew)    
        dtlist.append(datanew)        
dtlist = np.array(dtlist)
#print(dtlist)
## oraganizing the joint position
dtlistorg=[]
for i in range(len(dtlist)):
   
    curdt=dtlist[i]
    newcurdt=np.zeros([curdt.shape[0],13], dtype='<U32')
    for j in range(curdt.shape[0]):
        newcurdt[j,0]= curdt[j,0]
        newcurdt[j,1]= str(curdt[j,1])+','+str(curdt[j,3])+','+str(curdt[j,21])
        newcurdt[j,2]= str(curdt[j,2])+','+str(curdt[j,4])+','+str(curdt[j,20])
        newcurdt[j,3]= str(curdt[j,5])+','+str(curdt[j,6])+','+str(curdt[j,19])
        newcurdt[j,4]= str(curdt[j,7])+','+str(curdt[j,8])+','+str(curdt[j,24])
        newcurdt[j,5]= str(curdt[j,9])+','+str(curdt[j,10])+','+str(curdt[j,23])
        newcurdt[j,6]= str(curdt[j,11])+','+str(curdt[j,12])+','+str(curdt[j,22])
        newcurdt[j,7]= curdt[j,13]
        newcurdt[j,8]= curdt[j,14]
        newcurdt[j,9]= curdt[j,15]
        newcurdt[j,10]= curdt[j,16]
        newcurdt[j,11]= curdt[j,17]
        newcurdt[j,12]= curdt[j,18]
    dtlistorg.append(newcurdt)

dtlistorg = np.array(dtlistorg)       
print(dtlistorg)
## saving
# Saving the objects:
with open('Tremdata.pickle', 'wb') as f:  # Python 3: open(..., 'wb')
    pickle.dump(dtlistorg, f)