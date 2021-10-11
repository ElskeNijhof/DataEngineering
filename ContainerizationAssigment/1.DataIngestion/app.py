from flask import Flask, json, request, Response

from Resources import DataIngestion

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/DataIngestion/database', methods=['GET'])
def read_data():
  

    df_train = DataIngestion.Readjson()   
    resp = Response(df_train.to_json(orient='records'), status=200, mimetype='application/json')
    return resp

app.run(host='0.0.0.0', port=5000)