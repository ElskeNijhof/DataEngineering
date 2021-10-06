from flask import Flask, json, request, Response

from Resources import DataIngestion

app = Flask(__name__)
app.config["DEBUG"] = True
<<<<<<< HEAD
=======
#db_util = DBUtil()
>>>>>>> 0cf1dd7f9038f28577a9ccc994e5d411720299e1


@app.route('/training-db/<table_name>', methods=['GET'])
def read_data():
    df_train = DataIngestion.Readjson()   
    resp = Response(df_train.to_json(orient='records'), status=200, mimetype='application/json')
    return resp

<<<<<<< HEAD
=======
@app.route('/training-db/<table_name>', methods=['POST'])
def create_table(table_name):
    # get the payload or body
    req_data = request.get_json()
    columns = req_data['columns']
    db_util.create_tb(table_name, columns)
    return json.dumps({'message': 'a table was created'}, sort_keys=False, indent=4), 200
>>>>>>> 0cf1dd7f9038f28577a9ccc994e5d411720299e1
app.run(host='0.0.0.0', port=5000)