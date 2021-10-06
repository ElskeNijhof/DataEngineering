import pandas as pd
import os 

os.chdir('C:\\Users\\Elske\\OneDrive\\Documenten\\DE_Assignment1')

df_test = pd.read_csv('test.csv').dropna()
df_train = pd.read_csv('train.csv').dropna()