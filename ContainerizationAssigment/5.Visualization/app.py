import os
import pandas as pd
import requests
from flask import Flask, Response,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/visualization/Age:<age>/class:<clss>', methods=['GET'])
def Visualization(age, clss):
    
    Prediction_api = os.environ['/predict/Age:{}/class:{}'.format(age, clss)]
    if Prediction_api >= 0.5:
        print("gello")
        #return alive
    else:
        print("gello")
        #return you are dead

   
    


