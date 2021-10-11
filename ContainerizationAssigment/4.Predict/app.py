import os
from flask.wrappers import Request
import pandas as pd
import requests
from flask import Flask, Response, jsonify
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict/Age:<age>/class:<clss>', methods=['GET'])
def predict(age, clss):
    html = "<h3>Hello, you will probably...</h3>" \
           "<b>{liveOrDie}</b><br/>" 
    
    #Check if model is already saved locally
    model_repo = os.environ['MODEL_REPO']
    Model_DIR = os.path.join[model_repo, "Titanic_model.pkl"]
    with open(Model_DIR, 'rb') as file:
        pickle_model = pickle.load(file)
    
    if pickle_model:
        j = "Available"
        return html.format(liveOrDie =j)
    else:
        j =  "not avaiable"
        return html.format(liveOrDie =j)
   
    # Get Model:
    #Model_api = os.environ['Train_API']

    #Model = requests.get(Model_api)
    #j = Model.json()

    #return html.format(liveOrDie =j)

app.run(host='0.0.0.0', port=500)
