# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:33:37 2017

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
import numpy.linalg as la
########################## TUG Data Clustering#################################
### I should find the angle between these two vectors: 1- Spine_Mid,Spine_Base  2- Spine_Base, Knee_Right joints
## Subfunctions
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))
def py_ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    stimenp.arccos(sinang, cosang)
    
def length(v):

  return math.sqrt(dotproduct(v, v))
  
def angle_detection(ndata):
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
    angdata=[]
    for j in range(len(data)):
        curdata=data[i]
        curangs =[]
        for w in range(curdata.shape[0]):
            sp_mid = curdata[w][0]# j1
            sp_base = curdata[w][1]# j2
            knee_right = curdata[w][17]#j18
            sp_mid_cord=re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*",sp_mid)
            sp_base_cord=re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*",sp_base)
            knee_right_cord=re.findall("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*",knee_right)
            v1 = [float(sp_mid_cord[0]) - float(sp_base_cord[0]), float(sp_mid_cord[1]) - float(sp_base_cord[1]),float(sp_mid_cord[2]) - float(sp_base_cord[2])]
            v2 = [float(sp_mid_cord[0]) - float(knee_right_cord[0]), float(sp_mid_cord[1]) - float(knee_right_cord[1]),float(sp_mid_cord[2]) - float(knee_right_cord[2])]
            #ang = math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
            ang = py_ang(v1, v2)
            curangs.append(ang[0])
            curangs.append(ang[1])
        angdata.append(np.array(curangs))
    return(angdata)
def get_MeanStd(data):
    Subj_Meanstd=[]
    for i in range(len(data)):
        curdata = data[i]
        currSubj_Meanstd=np.zeros(2,dtype=np.float)# 0: mena 1:std
        currSubj_Meanstd[0]=np.mean(curdata[:])
        currSubj_Meanstd[1]=np.std(curdata[:])
           
        Subj_Meanstd.append(currSubj_Meanstd)
    Subj_Meanstd=np.array(Subj_Meanstd)
    return Subj_Meanstd
def data_visualization(flattenData):
     
    #colord = []
    #for i in range(30):
    #    if grlabel[i]==0:
    #        colord.append('red')
    #    else:
    #        colord.append('green')
    tsne = manifold.TSNE(n_components=3, init='pca', random_state=0)
    Y = tsne.fit_transform(flattenData)
    
    #plt.scatter(Y[:, 0], Y[:, 1],c=colord,  cmap=plt.cm.Spectral)
    plt.scatter(Y[:, 0], Y[:, 1],cmap=plt.cm.Spectral)
    
    plt.title("t-SNE (%.2g sec)" )
    
    plt.axis('tight')

    plt.show()            
##################################################################### Main part
with open('TUGdata.pickle','rb') as f:  
    ndata = pickle.load(f)
## find angles for each subject as its features
angdata = angle_detection(ndata)  
print(angdata)  
## data flattening for the subjects
flattenData=[]
for i in range(len(angdata)):
    flattenData.append(angdata[i].flatten())
flattenData=np.array(flattenData)
## visualize the data
data_visualization(flattenData)
## get mean std
X = get_MeanStd(flattenData)
#print(X)
## clustering
#X=angdata
random_state = 1
kmeans = KMeans(n_clusters=3,random_state=random_state).fit(X)
print(kmeans.labels_)
