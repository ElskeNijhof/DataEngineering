import os

import pandas as pd
import requests
from flask import Flask, Response,jsonify

from Resources import TrainV2


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/Training/model', methods=['GET'])
def train_models():

    feature_api = os.environ['FEATURE_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(feature_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    Model = TrainV2.train(df)
    resp = Response(Model, status=200, mimetype='application/json')
    
    return jsonify(Model)

app.run(host='0.0.0.0', port=500)