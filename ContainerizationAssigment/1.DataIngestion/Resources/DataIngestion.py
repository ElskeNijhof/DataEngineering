import pandas as pd

def Readjson():

    df_train = pd.read_csv('train.csv').dropna()

    return df_train