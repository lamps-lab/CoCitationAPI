# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:01:15 2020

@author: weixin
"""

#cocitationAll is a dictionary, not a list
#output has original doi
#output has year information  (incomplete)
#in the output is 'DOI'

import requests
import json
import csv
import time
#import numpy as np
#from pandas.core.frame import DataFrame


csvfile = open('SCORE.csv','r', encoding= 'latin-1')
reader = csv.reader(csvfile)
DOI = [row[4] for row in reader]     #the row starts from 0, so [4] is the fifth

cocitationsAll = {}
yearsAll = {}    # about year
counter = 0
counter_sourceDOI = 0
notfound_source = []
notfound2 = []

#for k in range(1, len(DOI)):
for k in range(1, 51):
    print("DOI", k)

    
    url = 'https://api.semanticscholar.org/v1/paper/' + DOI[k]
    
    time.sleep(3) #delay for 3 secs
    
    r = requests.get(url, auth=('user', 'pass'))
    
    #data = json.dumps(dataAPI)
    print(url)
    print(r)
    #print(r.json())
    
    dataapi = r.json()   # a dictionary
    
    citations = dataapi.get('citations')
    pubYear = dataapi.get('year')
    
    if citations is None or len(citations) == 0:
       counter_sourceDOI +=1
       print("counter_sourceDOI:", counter_sourceDOI)
       notfound_source.append(DOI[k])
    else:
    
        #references = dataapi.get('references')
        
        ciID = []
        dict = {}
        years= {}   # about year
        counter = 0
        for i in range(0, len(citations)):
        
           id = citations[i].get('paperId')
           ciID.append(id)
           url_cite = 'https://api.semanticscholar.org/v1/paper/' + id
           time.sleep(3) #delay for 3 secs
           r1 = requests.get(url_cite, auth=('user', 'pass'))
           #print('i=', i)
           #print(url_cite)
           #print(r1)
           data_cite = r1.json()
           references_cite = data_cite.get('references')
           if references_cite is None or len(references_cite) == 0:    # need to use url to request, if is none, will be 404, code would stop
               counter +=1
               print("counter:", counter)
               notfound2.append(id)
           else:
               for j in range(0, len(references_cite)):
               
                   id2 = references_cite[j].get('doi')
                   year = references_cite[j].get('year')    # about year
                   
                   years[id2] = year     # about year
                   
                   if id2 not in dict:
                       dict[id2] = 1
                   else:
                       dict[id2] +=1
               
    cocitationsAll[DOI[k]] = dict
    yearsAll[DOI[k]] = years     # about year
    
cocitation = json.dumps(cocitationsAll)          #save dictionary to json file
fileObject = open('cocitation1to50.json', 'w')  #this line corresponds to txt file name
fileObject.write(cocitation)  
fileObject.close()  

yearss = json.dumps(yearsAll)          #save dictionary to json file
fileObject = open('yearss1to50.json', 'w')  
fileObject.write(yearss)  
fileObject.close() 
  
print("counter_sourceDOI:", counter_sourceDOI)
print("notfound_source:", notfound_source)
print("counter:", counter)
print("notfound2:", notfound2)
