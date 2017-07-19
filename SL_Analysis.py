"""
Created on Sat Apr  1 19:34:01 2017

@author: sara
"""

import numpy as np
import glob
import pickle 
#import Kmean as km

dtlist1=[]
dtlist2=[]
dtlistGen=[]
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
        if 'cw' in sub:
            dtlist1.append(datanew)        
        elif 'pw' in sub:
            dtlist2.append(datanew) 
        dtlistGen.append(datanew)
            
dtlist1 = np.array(dtlist1)
dtlist2 = np.array(dtlist2)
dtlistGen=np.array(dtlistGen)

## saving
# Saving the objects:
with open('SLdataPD.pickle', 'wb') as f1:  # Python 3: open(..., 'wb')
    pickle.dump(dtlist1,f1)
    
with open('SLdataCN.pickle', 'wb') as f2:  # Python 3: open(..., 'wb')
    pickle.dump(dtlist2,f2)
    
with open('SLDataGen.pickle', 'wb') as f3:  # Python 3: open(..., 'wb')
    pickle.dump(dtlistGen,f3)
