import pandas as pd
import os 
from sklearn import linear_model
import pickle

# Data ingestion
os.chdir('C:\\Users\\Elske\\OneDrive\\Documenten\\DE_Assignment1')
df_test = pd.read_csv('test.csv').dropna()
df_train = pd.read_csv('train.csv').dropna()

# Extract and store Features
X_train = df_train[['Age', 'Pclass']]
y_train = df_train['Survived']

# Train Model
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

# Pickle save
pkl_filename = "Titanic_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(reg, file)


