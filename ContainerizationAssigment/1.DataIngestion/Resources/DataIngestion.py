import pandas as pd

def Readjson():

    df_train = pd.read_json('train_json.json').dropna()

    return df_train