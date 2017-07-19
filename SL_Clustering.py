# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:46:41 2017

@author: sara
"""
import numpy as np
import pickle
import re
import scipy.io as sio
import scipy
import math
from matplotlib import pyplot as plt
from sklearn import manifold, datasets
from sklearn.cluster import KMeans
## subfunctions
def euclideanDistance(instance1, instance2, length):
    ed = 0
    for x in range(length):
        ed += pow((instance1[x]-instance2[x]), 2)
    #print('Euclidean distance',ed)
    return math.sqrt(ed)
def data_Preprocessing(ndata):
    
    jn=25
    data=[]
    for i in range(len(ndata))    :
        [r,c]=ndata[i].shape
        #    curdata=np.zeros([r,c-1],np.str)
        #    #print(curdata.shape)
        #    for k in range(r):
        #        for j in range(c-1):
        #            curdata[k][j] = ndata[i][k][j+1]
        curdata=scipy.delete(ndata[i],0,1)
        data.append(curdata)
    
    print(len(data))
    SubjCordState=[]
    for si in range(len(data)):
    #print(data[si].shape)    
    #Cordinstate = np.zeros([data[si].shape[1],3,data[si].shape[0]], dtype='float')
    #Cordinstate = np.zeros([data[si].shape[1],data[si].shape[0],3], dtype='float')
        Cordinstate = np.zeros([jn,3,data[si].shape[0]], dtype='float')

        for nd in range(jn):

            Xstate=[]
            Ystate = []
            Zstate = []
            curstate = []
            for k in range(data[si].shape[0]):       
                #cordstate=re.findall("\d+\.\d+",data[si][k][nd])
                cordstate=re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*",data[si][k][nd])
                #print(si,nd,k,cordstate)
                if len(cordstate):
                    Xstate.append(float(cordstate[0]))# /1000 for tremor cuz its mm not m
                    Ystate.append(float(cordstate[1]))
                    Zstate.append(float(cordstate[2]))
                    curstate.append(data[si][k][nd])
       
            Cordinstate[nd][0][:] = Xstate#.append([Xstate])
            Cordinstate[nd][1][:] = Ystate#.append([Ystate])
            Cordinstate[nd][2][:] = Zstate#.append([Zstate])
        SubjCordState.append(Cordinstate)
    return(SubjCordState)
    
def find_speed(data):
    speeddata=np.zeros([len(data),2],dtype=np.float)
    for i in range(len(data)):
        cur_data = data[i]
        ld = data[i].shape[2]
        disdata=[]
        print(cur_data.shape)
        for i in range(cur_data.shape[0]):
            
            instance1=[cur_data[i][0][0],cur_data[i][1][0],cur_data[i][2][0]]
            instance2=[cur_data[i][0][ld-1],cur_data[i][1][ld-1],cur_data[i][2][ld-1]]
            fd = euclideanDistance(instance1, instance2, 3)
            disdata.append(fd)
            np.array(disdata)
        speeddata[i][0] = np.average(disdata)
        speeddata[i][1] = ld
    return speeddata
        
###########################################################Step Length Analysis
##################################################################### Main part
with open('SLDataGen.pickle','rb') as f:  
    ndata = pickle.load(f)
data = data_Preprocessing(ndata)
#print(data)
# find length and speed data
spdata = find_speed(data)  
print(spdata)  

X=spdata

random_state = 1
kmeans = KMeans(n_clusters=3,random_state=random_state).fit(X)
print(kmeans.labels_)