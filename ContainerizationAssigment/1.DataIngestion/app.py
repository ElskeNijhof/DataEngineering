from flask import Flask, json, request, Response

from Resources import DataIngestion

app = Flask(__name__)
app.config["DEBUG"] = True
# db_util = DBUtil()


@app.route('/training-db/<table_name>', methods=['GET'])
def read_data(table_name):
    df = db_util.read_data_records(table_name)
    df = df.drop(columns=['id'])
    resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=5000)