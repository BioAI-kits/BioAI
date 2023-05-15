from sklearn import metrics
import numpy as np
import json


class Metrics():
    def __init__(self, y_pred, y_true, y_score, output='metrics.json') -> None:
        """ 
        macro: Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
        micro: Calculate metrics globally by counting the total true positives, false negatives and false positives.
        weighted: Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label). This alters ‘macro’ to account for label imbalance; it can result in an F-score that is not between precision and recall.
        
        """
        self.y_pred = y_pred
        self.y_true = y_true
        self.y_score = y_score
        self.output = output
        self.checkData()
        self.run()
        self.saveData()
        
    def checkData(self) -> None:
        assert len(set(self.y_pred)) > 2, f"Not a Multi classification task. The predicted label is less than 2 types: {set(self.y_pred)}"
        assert len(set(self.y_true)) > 2, f"Not a Multi classification task. The actual label is less than 2 types: {set(self.y_true)}"
        assert np.max(self.y_score) <= 1, f"The y_score is greater than 1"
        assert np.min(self.y_score) >= 0, f"The y_score is less than 0"
        if not self.output.endswith('.json'):
            self.output += '.json'          
    
    def run(self):
        self.confusion_matrix()
        self.classification_report()
        self.accuracy()
        self.balanced_accuracy()
        self.precision()
        self.recall()
        self.f1()
        self.auc()
    
    def classification_report(self):
        self.class_report = metrics.classification_report(y_true=self.y_true, y_pred=self.y_pred, output_dict=True)
    
    def confusion_matrix(self) -> None:
        self.cm = metrics.confusion_matrix(y_true=self.y_true, y_pred=self.y_pred).tolist()
        
    def accuracy(self) -> None:
        self.acc = metrics.accuracy_score(y_true=self.y_true, y_pred=self.y_pred, normalize=True)
    
    def balanced_accuracy(self) -> None:
        """ 
        The balanced accuracy in binary and multiclass classification problems to deal with imbalanced datasets. 
        It is defined as the average of recall obtained on each class.
        """
        self.b_acc = metrics.balanced_accuracy_score(y_true=self.y_true, y_pred=self.y_pred)
        
    def precision(self) -> None:
        prec = {}
        # each classification precision
        for cls in set(self.y_true):
            cls = str(cls)
            prec[f'class_{cls}'] = self.class_report[cls]['precision']
        
        # macro average precision
        prec['macro_precision'] = self.class_report['macro avg']['precision']
        
        # micro average precision
        prec['micro_precision'] = metrics.precision_score(y_true=self.y_true, y_pred=self.y_pred, average='micro')
        
        # weighted average precision
        prec['weighted_precision'] = self.class_report['weighted avg']['precision']
        
        self.precision = prec

    def recall(self) -> None:
        "Recall / TPR / Sensitivity"
        recall_ = {}
        # each classification recall
        for cls in set(self.y_true):
            cls = str(cls)
            recall_[f'class_{cls}'] = self.class_report[cls]['recall']
        
        # macro average recall
        recall_['macro_recall'] = self.class_report['macro avg']['recall']
        
        # micro average recall
        recall_['micro_recall'] = metrics.recall_score(y_true=self.y_true, y_pred=self.y_pred, average='micro')
        
        # weighted average recall
        recall_['weighted_recall'] = self.class_report['weighted avg']['recall']
        
        self.recall_score = recall_
    
    def f1(self) -> None:
        """
        F1 = 2 * (precision * recall) / (precision + recall)
        """
        f1_ = {}
        # each classification f1-score
        for cls in set(self.y_true):
            cls = str(cls)
            f1_[f'class_{cls}'] = self.class_report[cls]['f1-score']
            
        # macro average f1-score
        f1_['macro_f1'] = self.class_report['macro avg']['f1-score']
        
        # micro average f1-score
        f1_['micro_f1'] = metrics.f1_score(y_true=self.y_true, y_pred=self.y_pred, average='micro')
        
        # weighted average f1-score
        f1_['weighted_f1'] = self.class_report['weighted avg']['f1-score']
    
        self.f1_score = f1_

    def auc(self) -> None:
        auc_ = {}
        auc_['macro_ovr_auc'] = metrics.roc_auc_score(self.y_true, self.y_score, average='macro', multi_class='ovr')
        auc_['macro_ovo_auc'] = metrics.roc_auc_score(self.y_true, self.y_score, average='macro', multi_class='ovo')
        auc_['micro_ovr_auc'] = metrics.roc_auc_score(self.y_true, self.y_score, average='micro', multi_class='ovr')
        auc_['weighted_ovr_auc'] = metrics.roc_auc_score(self.y_true, self.y_score, average='weighted', multi_class='ovr')
        auc_['weighted_ovo_auc'] = metrics.roc_auc_score(self.y_true, self.y_score, average='weighted', multi_class='ovo')
        self.auc_score = auc_   
    
    def saveData(self) -> None:
        self.metrics_ = {
                        'confusion_matrix': self.cm,
                        'accuracy': self.acc,
                        'balanced_accuracy': self.b_acc,
                        'precision': self.precision,
                        'recall': self.recall_score,
                        'f1_score': self.f1_score,
                        'auc': self.auc_score,
                        }
        with open(self.output, 'w') as OUT:
            OUT.write(json.dumps(self.metrics_, indent=4))       


if __name__ == '__main__':
    y_pred = np.random.choice(5, size=100)
    y_true = np.random.choice(5, size=100)
    y_score = np.random.random((100,5))
    def softmax(x):
        a = np.sum(np.exp(x), axis=1)
        return np.exp(x) / a[:, None]

    y_score = softmax(y_score)
    
    Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true)
    
    print(Evaluation.metrics_)
   
            