import os
from flask.wrappers import Request
import pandas as pd
import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict/Age:<age>/class:<clss>', methods=['GET'])
def predict(age, clss):
    html = "<h3>Hello, you will probably...</h3>" \
           "<b>{liveOrDie}</b><br/>" 
    
    #Check if model is already saved locally
    model_repo = os.environ['MODEL_REPO']
    Model = os.path.join[model_repo, "model.h5"]
    if Model:
        j = "Available"
        return html.format(liveOrDie =j)
    else:
        j =  "nog avaiable"
        return html.format(liveOrDie =j)
   
    # Get Model:
    #Model_api = os.environ['Train_API']

    #Model = requests.get(Model_api)
    #j = Model.json()

    #return html.format(liveOrDie =j)

app.run(host='0.0.0.0', port=500)
