import pickle
import sys

with open("Titanic_model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)

print(sys.argv)

age = int(sys.argv[1])
clss = int(sys.argv[2])

print('Prediction: {0}'.format(pickle_model.predict([[age,clss]])))