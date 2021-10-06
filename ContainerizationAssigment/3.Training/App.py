import os

import pandas as pd
import requests
from flask import Flask, Response

from flask import jsonify
from Resources import TrainV2


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/Training/model', methods=['POST'])
def train_models():
    db_api = os.environ['TRAININGDB_API']
    # Make a GET request to training db service to retrieve the training data/features.
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    resp = TrainV2.train(df.values)
    return resp


app.run(host='0.0.0.0', port=5000)