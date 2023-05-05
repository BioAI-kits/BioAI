import numpy as np
import pandas as pd
from bioai.algorithms.base import RandomForest


class Model(RandomForest):
    def __init__(self, 
                 X_train: pd.DataFrame, 
                 X_test: pd.DataFrame, 
                 Y_train: np.ndarray, 
                 Y_test: np.ndarray, 
                 n_estimators=100, 
                 max_depth=5, 
                 random_state=42, 
                 output='Result_RandomForest'
                 ):
        super().__init__(X_train, X_test, Y_train, Y_test, n_estimators, max_depth, random_state, output)
    

