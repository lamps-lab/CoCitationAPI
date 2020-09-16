# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:22:46 2020

@author: weixin
"""

import requests
import json
import csv
import time
import numpy as np
from pandas.core.frame import DataFrame



csvfile = open('SCORE.csv','r', encoding='utf-8')
reader = csv.reader(csvfile)
DOI = [row[4] for row in reader]     #the row starts from 0, so [4] is the fifth
    
d = 1
citeD = {}
for i in range(1, len(DOI)):
    
    url = 'https://api.semanticscholar.org/v1/paper/' + DOI[i]
    
    time.sleep(3) #delay for 4 secs
    
    r = requests.get(url, auth=('user', 'pass'))
    
    print(url)
    print(r)
    
    dataapi = r.json()

    citations = dataapi.get('citations')
    
    citeD[DOI[i]] = citations



    

cocitation = [[0]*(len(DOI)-1) for i in range((len(DOI)-1))]
    
for i in range(0, (len(DOI)-1)):
    print("i:", i)
    a = citeD[DOI[i+1]] 
    if a is None or len(a) == 0:       #the API webpage returns empty results
        print('this is a nonetype1')
    else:
        print(type(a))
        print(len(a))
        #print(type(a[0]))
        for j in range(0, len(a)):
            print("j:", j)
            temp1 = a[j]['paperId']
            for k in range(0, (len(DOI)-1)):
                print("k:", k)
                b = citeD[DOI[k+1]]
                if b is None or len(b) == 0:
                    print('this is a nontype2')
                else:
                    for l in range(0, len(b)):
                        print("l:", l)
                        temp2 =  b[l]['paperId']
                        if temp1 == temp2:
                            cocitation[i][k] += 1
                   
                   
#cocitation1=np.array(cocitation)
#np.save('cocitation1.csv',cocitation1)   

cocitation_df = DataFrame(cocitation)
cocitation_df.to_csv("cocitation.csv",index=True,sep=',')    
       
       
#citeDic = json.dumps(citeD)          #save dictionary to json file
#fileObject = open('citeDic.json', 'w')  
#fileObject.write(citeDic)  
#fileObject.close()         
       
       
       
       
       
       
       
       
       
       