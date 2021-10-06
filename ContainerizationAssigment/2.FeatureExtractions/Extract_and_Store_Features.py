import os
from typing import Dict
import pandas as pd

from sklearn.feature_extraction import DictVectorizer

from ContainerizationAssigment import DataIngestion
from Data
#Features extracten 

def ExtractandStore(data):
    vec=DictVectorizer()
    vec.fit_transform(data).toarray()
    vec.get_feature_names()

ExtractandStore(df_train)

