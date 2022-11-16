
import sys
import json  

#contains config file with path to all valid endpoints
with open('config.json','r') as file:
    paths = json.loads(file.read())   

#adds the path of each project to global path
for i in range(len(paths.keys())):
    sys.path.insert(i,list(paths.values())[i])  


#import the function to trigger on recieving the push notif.
from github_hooks import github_listener 


#define all valid endpoints here
endpoints = {'github':github_listener}
