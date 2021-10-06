from flask import Flask, json, request, Response

from Resources.db_util import DBUtil

app = Flask(__name__)
app.config["DEBUG"] = True
db_util = DBUtil()


@app.route('/2.FeatureExtractions/<table_name>', methods=['POST'])
def create_table(table_name):
    # get the payload or body
    req_data = request.get_json()
    columns = req_data['columns']
    db_util.create_tb(table_name, columns)
    return json.dumps({'message': 'a table was created'}, sort_keys=False, indent=4), 200


@app.route('/2.FeatureExtractions/<table_name>', methods=['GET'])
def read_data(table_name):
    df = db_util.read_data_records(table_name)
    df = df.drop(columns=['id'])
    resp = Response(df.to_json(orient='records'), status=200, mimetype='application/json')
    return resp


app.run(host='0.0.0.0', port=5000)