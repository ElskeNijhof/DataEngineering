from flask import Flask, json, request, Response

from Resources.db_util import DBUtil

app = Flask(__name__)
app.config["DEBUG"] = True
db_util = DBUtil()

@app.route('/2.FeatureExtractions/DatabaseFeatures', methods=['GET'])
def Extract_features():
    db_api = os.environ['TRAININGDB_API']
    # Make a GET request to training db service to retrieve the Database
    r = requests.get(db_api)
    j = r.json()
    df = pd.DataFrame.from_dict(j)
    df_new = df[['Age', 'Pclass','Survived']]
    resp = Response(df_new.to_json(orient='records'), status=200, mimetype='application/json')
    return resp

app.run(host='0.0.0.0', port=5000)