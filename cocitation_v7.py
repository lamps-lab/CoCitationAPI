# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:56:24 2020

@author: weixi
"""

#cocitationAll is "append" dict
#output paperID
#only look at papers that cited the source paper 3 years after  (YearGap)

import requests
import json
import csv
import time
import numpy as np
from pandas.core.frame import DataFrame

#================================================================================================
#load data (source paper)
#================================================================================================
csvfile = open('SCORE.csv','r', encoding= 'latin-1')
reader = csv.reader(csvfile)
DOI = [row[4] for row in reader]     #the row starts from 0, so [4] is the fifth

#===============================================================================================
# Main part, Construct cocitation
#===============================================================================================

cocitationsAll = {}

YearGap = 3          # change this to control the publish time of papers that cited the source paper
counter_sourceDOI = 0
for k in range(1, len(DOI)):
#for k in range(83, 86):
    print("DOI", k)

    
    url = 'https://api.semanticscholar.org/v1/paper/' + DOI[k]
    
    time.sleep(3) #delay for 3 secs
    
    r = requests.get(url, auth=('user', 'pass'))
    
    #data = json.dumps(dataAPI)
    print(url)
    print(r)
    #print(r.json())
    
    dataapi = r.json()   # a dictionary for the source paper
    
    citations = dataapi.get('citations')
    pubYear = dataapi.get('year')
    sourceid = dataapi.get('paperId')
    
    if citations is None or len(citations) == 0:  #sometimes 'citations' is empty
       counter_sourceDOI +=1
       print("counter_sourceDOI:", counter_sourceDOI)
    
        
    else:
    
        #references = dataapi.get('references')
        
        ciID = []
        dict = {}
        counter = 0
        counter_year = 0
        rm_sourceid = 0
        for i in range(0, len(citations)):  #check each paper in 'citations'
        
            id = citations[i].get('paperId')
            year_becited = citations[i].get('year')    # about year
           
            if year_becited != None and year_becited-pubYear <= YearGap:       # Select the papers publishes less than or equal to 3 years after the original paper
           
                ciID.append(id)
                url_cite = 'https://api.semanticscholar.org/v1/paper/' + id
                time.sleep(3) #delay for 3 secs
                r1 = requests.get(url_cite, auth=('user', 'pass'))
                print('i=', i)
                #print(url_cite)
                print(r1)
                data_cite = r1.json()
                references_cite = data_cite.get('references')
                if references_cite is None or len(references_cite) == 0:
                    counter +=1
                    print("counter:", counter)
                else:
                    for j in range(0, len(references_cite)):
                   
                        id = references_cite[j].get('paperId')
                        
                       
                        if id not in dict:
                            dict[id] = 1
                        else:
                            dict[id] +=1
                            
                if sourceid in dict:           
                    del dict[sourceid]#remove the source paper
                else:
                    rm_sourceid +=1
            
            else:
                counter_year+=1
                       
    cocitationsAll[DOI[k]] = dict


#========================================================================================
#export json file
#========================================================================================    
cocitation = json.dumps(cocitationsAll)          #save dictionary to json file
fileObject = open('cocitation.json', 'w')  
fileObject.write(cocitation)  
fileObject.close()    