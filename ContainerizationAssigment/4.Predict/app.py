import os
from flask.wrappers import Request
import pandas as pd
import requests
from flask import Flask, Response, jsonify
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/predict/Age:<age>/class:<clss>', methods=['GET'])
def predict(age, clss):
   
    
    #Check if model is already saved locally
    model_repo = os.environ['MODEL_REPO']
    try: 
        Model_DIR = os.path.join(model_repo, "Titanic_model.pkl")
        with open(Model_DIR, 'rb') as file:
            pickle_model = pickle.load(file)

        prediction= pickle_model.predict([[age,clss]])
        #PREDICUT USING MODEL
        
        return str(prediction[0])   


    except:
        Train_API = os.environ['Train_API']   
        TrainModel = requests.get(Train_API)

        file_path = os.path.join(model_repo) 
        os.chdir(file_path)
        with open("Titanic_model.pkl", 'rb') as file:
            pickle_model = pickle.load(file)    
        
        prediction = pickle_model.predict([[age,clss]])
            # do API CALL TO TRAIN
        
            #PREDICUT USING MODEL

        return str(prediction[0])  
app.run(host='0.0.0.0', port=5000)
