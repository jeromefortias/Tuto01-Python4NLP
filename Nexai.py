import random
import string
import json

import pdb
import sys
from datetime import datetime
import socket
import getpass
import re
 
import requests

class Nexai :
    
    elasticsearch = ''
    name = ''
    
    def __init__(self,filename):
        self.filename = filename
        
        self.port = 0
        self.url = ""
        self.dataset_folder = ""
        self.model_location = ""
        self.model_name = ""
        self.epochs = 0;
        with open(filename) as file_in:
            for line in file_in:
                if (line.find(":") > 0 and len(line)>0):
                    parts = line.split(": ")
                    if len(parts) >= 1:
                        label = str(parts[0]).replace(' ', '')
                        value = str(parts[1]).replace(' ', '')
                            
                        if label == 'elasticsearch':
                            self.elasticsearch = value.strip()
                            
                        if label == 'port':
                            self.port = int(value.strip())
                            
                        if label == 'name':
                            self.name = value.strip()
                            
                        if label == 'url':
                            self.url = value.strip()
                            
                        if label == 'dataset_location':
                            self.dataset_folder = value.strip()
                            
                        if label == 'model_location':
                            self.model_location = value.strip()
                            
                        if label == 'model_name':
                            self.model_name = value.strip()
                            
                        if label == 'epochs':
                            self.epochs = int(value.strip())
    

    

    
    def EventPut(self,step, status, comments, strtags):
        
        myurl1 = "http://"+ self.elasticsearch 
        myurl2 = myurl1 +'/admin.events/_doc'
        #print("My ES Url : " +myurl2)
        
        machinename = socket.gethostname()
        username = getpass.getuser()
        today2 = datetime.now();
        tags = strtags.split(",")
        d2 = today2.strftime("%Y-%m-%dT%H:%M:%S.%f+02:00")
        #print(d2)
        payload = json.dumps({
                "program": self.name,  
                "step": step,
                "status": status,
                "comments": comments,
                "metaDatas": [],
                "tags": tags,
                "date": d2,
                "machineName": machinename,
                "userName": username
                })
        headers = { 'Content-Type': 'application/json'}
        response = requests.request("POST", myurl2, headers=headers, data=payload)
        #print(response.text) 
    
    def TrainingPut(self,step, algorithmclass, comments, strtags, duration, epochnb, loss, dataset):
        
        myurl1 = "http://"+ self.elasticsearch 
        myurl2 = myurl1 +'/admin.training/_doc'
        #print("My ES Url : " +myurl2)
        
        machinename = socket.gethostname()
        username = getpass.getuser()
        today2 = datetime.now();
        tags = strtags.split(",")
        d2 = today2.strftime("%Y-%m-%dT%H:%M:%S.%f+02:00")
        #print(d2)
        payload = json.dumps({
                "program": self.name,  
                "algorithmClass" : "algorithmClass",
                "step": step,
                "dataset" : "dataset",
                "comments": comments,
                "metaDatas": [],
                "tags": tags,
                "date": d2,
                "machineName": machinename,
                "userName": username,
                "duration" : duration,
                "epochnb" : epochnb
                })
        headers = { 'Content-Type': 'application/json'}
        response = requests.request("POST", myurl2, headers=headers, data=payload)
        #print(response.text)         

    def LogPut(self,step, status, comments, strtags, duration):
        
        myurl1 = "http://"+ self.elasticsearch 
        myurl2 = myurl1 +'/admin.logs/_doc'
        #print("My ES Url : " +myurl2)
        
        machinename = socket.gethostname()
        username = getpass.getuser()
        today2 = datetime.now();
        tags = strtags.split(",")
        d2 = today2.strftime("%Y-%m-%dT%H:%M:%S.%f+02:00")
        #print(d2)
        payload = json.dumps({
                "program": self.name,  
                "step": step,
                "status": status,
                "comments": comments,
                "metaDatas": [],
                "tags": tags,
                "date": d2,
                "machineName": machinename,
                "userName": username,
                "duration" : duration
                })
        headers = { 'Content-Type': 'application/json'}
        response = requests.request("POST", myurl2, headers=headers, data=payload)
        #print(response.text) 
    


