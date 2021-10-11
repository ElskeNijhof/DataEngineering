import os
import pandas as pd
import requests
from flask import Flask, Response,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/visualization/Age:<age>/class:<clss>', methods=['GET'])
def Visualization(age, clss):
    #Set up returning text
    html = "<h3>Hello, you will probably...</h3>" \
           "<b>{liveOrDie}</b><br/>" 

    #Retrieve the score that indicates 'live' or 'die'
    Prediction_api = 'http://predict_service:500/predict/Age:{}/class:{}'.format(age, clss)
    Request = requests.get(Prediction_api)
    #j = Request.json()
    value = 0.6
    if value >= 0.5:
        result = "live"
        return html.format(liveOrDie = age)
    else:
        result = "die"
        return html.format(liveOrDie = result)

app.run(host='0.0.0.0', port=5000)
   
    


