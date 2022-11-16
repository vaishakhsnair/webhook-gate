# this script runs as a service and listens for any incoming webhook request acting as a webhook reverse proxy.
# any application can register by modifying the config file to register an endpoint and the absolute path to the project.
# the hooks_handler support file registers the path in the config file for n number of application only association required is the calling 
# class or function that is triggered on recieving the push notification .




import subprocess
import os
from flask import Flask,request,jsonify,abort
import requests
import time
import json
import hmac
import threading
import datetime
import hooks_handler #defines all the valid hooks

app = Flask(__name__)   # Flask constructor


VALID_ENDPOINTS = hooks_handler.endpoints


#paths to all the projects to change working directory
PATHS = hooks_handler.paths


@app.route('/hooks/<endpoint>',methods=['POST'])
def endpoint_listener(endpoint):
    if endpoint in VALID_ENDPOINTS.keys():
        return VALID_ENDPOINTS[endpoint](request,PATHS[endpoint])

                
                
if __name__ == '__main__':
    app.run(port=7949,host='0.0.0.0')
