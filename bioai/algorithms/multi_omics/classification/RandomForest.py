from sklearn.ensemble import RandomForestClassifier
import pickle
import os
from mlcakes.evaluation.multi_class import Metrics
import numpy as np
import pandas as pd 


class Model:
    def __init__(self, 
                 X_train:pd.DataFrame or np.ndarray, 
                 X_test:pd.DataFrame or np.ndarray, 
                 Y_train:np.ndarray, 
                 Y_test:np.ndarray,
                 n_estimators=100,
                 max_depth=5,
                 random_state=42,
                 output='Result_RandomForest',  # output directory
                 ):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        
        # parms
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.output = output
        
    def buildModel(self):
        """ 
        train and save model.
        """
        model = RandomForestClassifier(n_estimators=self.n_estimators, 
                                       max_depth=self.max_depth, 
                                       random_state=self.random_state,
                                       )
        model.fit(self.X_train, self.Y_train)
        os.makedirs(self.output, exist_ok=True)
        with open(os.path.join(self.output, 'model.pkl'), 'wb') as FO:
            pickle.dump(model, FO)
    
    def evaluation(self):
        """ 
        After performing, the metrics_ attribute holds the model evaluation metrics.
        evaluation.json will be written on output directory.
        """
        with open(os.path.join(self.output, 'model.pkl'), 'rb') as FO:
            model = pickle.load(FO)
        y_pred = model.predict(self.X_test)
        y_score = model.predict_proba(self.X_test)
        y_true = self.Y_test
        Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true, 
                             output=os.path.join(self.output, 'evaluation.json')
                             )
        self.metrics_ = Evaluation.metrics_  
    
    def predict(self, data):
        """ 
        data: the format should be same with X_train / X_test
        Return: 
            y_pred: predicted label
            y_score: predicted prob.
        """
        with open(os.path.join(self.output, 'model.pkl'), 'rb') as FO:
            model = pickle.load(FO)
        y_pred = model.predict(data)
        y_score = model.predict_proba(data)
        return y_pred, y_score


