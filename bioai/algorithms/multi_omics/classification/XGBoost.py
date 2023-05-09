import numpy as np
import pandas as pd
from bioai.algorithms.base import XGBoost


class Model(XGBoost):
    def __init__(self, 
                 X_train: pd.DataFrame, 
                 X_test: pd.DataFrame, 
                 Y_train: np.ndarray, 
                 Y_test: np.ndarray, 
                 n_estimators=100, 
                 max_depth=5, 
                 random_state=42, 
                 learning_rate=0.0001, 
                 task='binary_cls', 
                 output='Result_XGBoost'):
        super().__init__(X_train, X_test, Y_train, Y_test, n_estimators, max_depth, random_state, learning_rate, task, output)