import os

import pandas as pd
import requests
from flask import Flask, Response,jsonify

from Resources import TrainV2


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/Training/model', methods=['GET'])
def train_models():
    html = "<h3>Hello, you will probably...</h3>" \
           "<b>{liveOrDie}</b><br/>" 
    feature_api = os.environ['FEATURE_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(feature_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = TrainV2.train(df)

    return html.format(liveOrDie = j)

app.run(host='0.0.0.0', port=500)