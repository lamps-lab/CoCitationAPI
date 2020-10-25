# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:16:00 2020

@author: weixi
"""

import requests
import json
import csv
import time


#================================================================================================
#load data (source paper)
#================================================================================================
csvfile = open('SCORE.csv','r', encoding= 'latin-1')
reader = csv.reader(csvfile)
DOI = [row[4] for row in reader]     #the row starts from 0, so [4] is the fifth


#===============================================================================================
# Main part, Construct cocitation
#===============================================================================================
BibliographicCouplingAll = {}
YearGap = 3          # change this to control the publish time of papers that cited the source paper

counter_sourceDOI = 0
for k in range(1, 3):
    
    url = 'https://api.semanticscholar.org/v1/paper/' + DOI[k]
    
    time.sleep(3) #delay for 3 secs
    
    r = requests.get(url, auth=('user', 'pass'))
    
    print(url)
    print(r)
    
    dataapi = r.json()   # a dictionary
    
    references = dataapi.get('references')
    pubYear = dataapi.get('year')
    sourceid = dataapi.get('paperId')
    
    if references is None or len(references) == 0:
       counter_sourceDOI +=1
       print("counter_sourceDOI:", counter_sourceDOI)
    else:
        
        dict = {}
        counter = 0
        counter_year = 0  #number of not entering "if year_cite != None and year_cite-pubYear <= YearGap:  "
        rm_sourceid = 0  # number of not entering "if sourceid in dict:"
        for i in range(0, len(references)): #check each paper in 'references' (intermediate papers)
            
            id = references[i].get('paperId')
            url_ref = 'https://api.semanticscholar.org/v1/paper/' + id
            time.sleep(3) #delay for 3 secs
            r1 = requests.get(url_ref, auth=('user', 'pass'))
            #print('i=', i, 'k=', k)
            #print(url_ref)
            print(r1)
            data2 = r1.json()
            citations = data2.get('citations')
            
            if citations is None or len(citations) == 0:
               counter +=1
               print("counter:", counter)
            else:
               for j in range(0, len(citations)):
                   #print('j:', j)
                   id = citations[j].get('paperId')
                   year_cite = citations[j].get('year') 
                   if year_cite != None and year_cite-pubYear <= YearGap:   
                       
                       if id not in dict:
                           dict[id] = 1
                       else:
                           dict[id] +=1
                   else:
                       counter_year+=1
            if sourceid in dict:
                del dict[sourceid]     #remove the source paper
            else:
                rm_sourceid +=1
    BibliographicCouplingAll[DOI[k]] = dict            
            
#========================================================================================
#export json file
#========================================================================================    
BibliographicCoupling = json.dumps(BibliographicCouplingAll)          #save dictionary to json file
fileObject = open('BibliographicCoupling.json', 'w')  
fileObject.write(BibliographicCoupling)  
fileObject.close()    