# MLP for Pima Indians Dataset saved to single file
# see https://machinelearningmastery.com/save-load-keras-deep-learning-models/
import logging
import os
import pickle
from sklearn.linear_model import LinearRegression
from flask import jsonify


def train(dataset):
    # split into input (X) and output (Y) variables
    X = dataset[["Age", 'Pclass']]
    Y = dataset['Survived']

    model = LinearRegression()
    model.fit(X, Y)

    
    #Saving model in a given location provided as an env. variable
    model_repo = os.environ['MODEL_REPO']
    
    if model_repo:
        file_path = os.path.join(model_repo, "Titanic_model.pkl")  
        with open(file_path, 'wb') as file:
            pickle.dump(model, file)
        logging.info("Saved the model to the location : " + model_repo)
        return 200
    else:
        model.save("model.h5")
        return jsonify({'message': 'The model was saved locally.'}), 200