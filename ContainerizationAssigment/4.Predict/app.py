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
    # Get Model:
    Model_api = os.environ['MODEL_API']
    Request = requests.get(Model_api)
    f = Request.json()
    result = 0

    return html.format(liveOrDie = result)

app.run(host='0.0.0.0', port=500)
