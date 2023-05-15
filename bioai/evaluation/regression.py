from sklearn import metrics
import numpy as np
import json


class Metrics():
    def __init__(self, y_pred, y_true, output='metrics.json') -> None:
        self.y_pred = y_pred
        self.y_true = y_true
        self.output = output

        self.checkData()
        self.run()
        self.saveData()
        
    def checkData(self) -> None:
        if not self.output.endswith('.json'):
            self.output += '.json'          
    
    def run(self):
        self.mse()
        self.mae()
    
    def mse(self) -> None:
        self.mse = metrics.mean_squared_error(self.y_true, self.y_pred)
    
    def mae(self) -> None:
        self.mae = metrics.mean_absolute_error(self.y_true, self.y_pred)
        
    def saveData(self) -> None:
        print(self.mse)
        self.metrics_ = {
                        'mean_squared_error': self.mse,
                        'mean_absolute_error': self.mae,
                        }
        with open(self.output, 'w') as OUT:
            OUT.write(json.dumps(self.metrics_, indent=4))


if __name__ == '__main__':
    y_pred = np.random.random(100)
    y_true = np.random.random(100)
    
    Evaluation = Metrics(y_pred=y_pred, y_true=y_true)
    
    print(Evaluation.metrics_)
   
            