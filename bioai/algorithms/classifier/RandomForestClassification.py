import os, pickle
import numpy as np
import pandas as pd 
import mlcakes
from bioai.utils.getTime import getTime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


class RandomForestClassification:
    """
    To build a classification model using RandomForest algorithm.
    """
    def __init__(self, 
                 X_train:pd.DataFrame or np.ndarray, 
                 X_test:pd.DataFrame or np.ndarray, 
                 Y_train:np.ndarray, 
                 Y_test:np.ndarray,
                 n_estimators=100,
                 max_depth=5,
                 random_state=42,
                 task='bc',
                 output='Result_RandomForest',  # output directory
                 ):
        """
        Args:
            X_train (pd.DataFrameornp.ndarray): X train data.
            X_test (pd.DataFrameornp.ndarray): X test data.
            Y_train (np.ndarray): Y train data.
            Y_test (np.ndarray): Y test data.
            n_estimators (int, optional): _description_. Defaults to 100.
            max_depth (int, optional): _description_. Defaults to 5.
            random_state (int, optional): _description_. Defaults to 42.
            output (str, optional): _description_. Defaults to 'Result_RandomForest'.
            task(str): 
        """
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        
        # parms
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.output = output
        
        # task
        assert task in ['bc', 'mc'], '[Error]: Task should be bc or mc.'
        self.task = task
        
    def buildModel(self):
        """ 
        train and save model.
        """
        info = f"{getTime()} >>> Building model...\n"
        print(info)
        
        # Grid Search
        parameters = {}
        if self.n_estimators == 'auto':
            parameters['n_estimators'] = [50, 100, 150, 200]
        if self.max_depth == 'auto':
            parameters['max_depth'] = [4, 6, 8, 10]
        if len(parameters) > 0:
            gs = GridSearchCV(RandomForestClassifier(random_state=self.random_state), 
                              parameters, 
                              refit = False, 
                              cv = 5, 
                              verbose = 0, 
                              n_jobs = -1)
            gs.fit(self.X_train, self.Y_train)
            if 'n_estimators' in gs.best_params_:
                self.n_estimators = gs.best_params_['n_estimators']
            if 'max_depth' in gs.best_params_:
                self.max_depth = gs.best_params_['max_depth']

        # Training Model
        model = RandomForestClassifier(n_estimators=int(self.n_estimators), 
                                       max_depth=int(self.max_depth), 
                                       random_state=self.random_state,
                                       )
        model.fit(self.X_train, self.Y_train)
        
        # Saving Model
        os.makedirs(self.output, exist_ok=True)
        with open(os.path.join(self.output, 'model.pkl'), 'wb') as FO:
            pickle.dump(model, FO)
    
    def evaluation(self):
        """ 
        After performing, the metrics_ attribute holds the model evaluation metrics.
        evaluation.json will be written on output directory.
        """
        info = f"{getTime()} >>> Evaluating model...\n"
        print(info)
        if self.task == 'mc':
            from mlcakes.evaluation.multi_class import Metrics
        else:
            from mlcakes.evaluation.binary_class import Metrics
        
        with open(os.path.join(self.output, 'model.pkl'), 'rb') as FO:
            model = pickle.load(FO)
        y_pred = model.predict(self.X_test)
        y_score = model.predict_proba(self.X_test)
        y_true = self.Y_test
        
        # if binary cls, score represent label1 score.
        if self.task == 'bc':
            y_score = y_score[:,1]
            
        Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true, 
                             output=os.path.join(self.output, 'evaluation.json')
                             )
        self.metrics_ = Evaluation.metrics_  
    
    def gridSearch(self):
        # TODO
        pass 
    
    def randomizedSearch(self):
        # TODO
        pass 
    
    
    @staticmethod
    def predict(path, data):
        """ 
        data: the format should be same with X_train / X_test
        Return: 
            y_pred: predicted label
            y_score: predicted prob.
        """
        info = f"{getTime()} >>> Predicting using model...\n"
        print(info)
        with open(os.path.join(path, 'model.pkl'), 'rb') as FO:
            model = pickle.load(FO)
        y_pred = model.predict(data)
        y_score = model.predict_proba(data)
        return y_pred, y_score
    
    

if __name__ == '__main__':
    import numpy as np
    print('正在测试多分类任务: ')
    # X_train = np.random.rand(64, 16)
    # Y_train = np.random.choice(3, 64)
    # X_test = np.random.rand(32, 16)
    # Y_test = np.random.choice(3, 32)
    
    # model = XGBoost(X_train, X_test, Y_train, Y_test, task='multi_cls')
    # model.buildModel()
    # model.evaluation()
    # pred, score = XGBoost.predict('Result_XGBoost', data=X_test)
    # print(pred, score)
    
    print('正在测试2分类任务: ')
    X_train = np.random.rand(64, 16)
    Y_train = np.random.choice(2, 64)
    X_test = np.random.rand(32, 16)
    Y_test = np.random.choice(2, 32)
    model = RandomForestClassification(X_train, X_test, Y_train, Y_test, task='binary_cls')
    model.buildModel()
    model.evaluation()
    pred, score = RandomForestClassification.predict('Result_XGBoost', data=X_test)
    print(pred, score)
    


