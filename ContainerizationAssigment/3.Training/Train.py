import pandas as pd
from sklearn.linear_model import LinearRegression

def train(df): 

    reg = LinearRegression()
    reg.fit(X_train, y_train)



# Save the model
# Location should be configurable







