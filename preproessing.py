# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:38:26 2017

@author: sara
"""

#dtarr = np.array(dtlist)
dtlist=np.array(dtlist)
#print(dtlist)
#dataprep = np.chararray((len(dtlist), dtlist[0].shape[0]*dtlist[0].shape[1]))
dataprep=[]
maxll=0

## Data preparation
for i in range(len(dtlist)):
    curdt = np.array(dtlist[i])
    [r,c] = curdt.shape
    #if r*c > maxll:
        #maxll=r*c
    curdtn= np.reshape(curdt,[1,r*c])
    dataprep.append(curdtn)
    #dataprep[i,:]=curdtn
    
## remove spaces
dtfinal=[]
for k in range (len(dataprep)):
    curdt = dataprep[k][0]
    #print(curdt)
    datanew=[]
    for w in range(curdt.shape[0]):
        if curdt[w] != '':
            datanew.append(curdt[w])
    curdtn = np.array(datanew)
    ll = len(curdtn)
    if ll > maxll:
        maxll=ll
    dtfinal.append(datanew)

## making them same size
ssdata=[]    
for k in range (len(dtfinal)):
    curdt = dtfinal[k]
    content = ([x.strip().split(',') for x in curdt])
    content1 = np.array(content)
    dss = np.empty(maxll, dtype='<U32')
    dss[:]='0'
    dss[:content1.shape[0]]=content
    dss = dss.astype(np.float)
    ssdata.append(dss)
    print(dss.shape)
    
    
    
'''   
## Clustering
#print(dataprep)

myfile = open('TUG.csv', 'w')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
for item in dataprep:
    wr.writerow(item)

dataprep=np.array(dataprep)
#clust_Input = np.transpose(dataprep)

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(ssdata)

'''

