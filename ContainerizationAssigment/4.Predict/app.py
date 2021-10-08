import os
import pandas as pd
import requests
from flask import Flask, Response,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict/Age:<age>/class:<clss>', methods=['GET'])
def predict(age, clss):
    # Get Model:
    Model_api = os.environ['MODEL_API']
    prediction = Model_api.predict(age, clss)
    return prediction


