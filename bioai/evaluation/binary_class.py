from sklearn import metrics
import numpy as np
import json
import matplotlib.pyplot as plt


class Metrics():
    def __init__(self, y_pred, y_true, y_score, output='metrics.json', plot_roc=False, roc_fig=None) -> None:
        self.y_pred = y_pred
        self.y_true = y_true
        self.y_score = y_score
        self.plot_roc = plot_roc
        self.output = output
        self.roc_fig = roc_fig
        self.checkData()
        self.run()
        self.saveData()
        self.roc_curve()
        
    def checkData(self) -> None:
        assert len(set(self.y_pred)) <= 2, f"Not a binary classification task. The predicted label is more than 2 types: {set(self.y_pred)}"
        assert len(set(self.y_true)) <= 2, f"Not a binary classification task. The actual label is more than 2 types: {set(self.y_true)}"
        assert np.max(self.y_score) <= 1, f"The y_score is greater than 1"
        assert np.min(self.y_score) >= 0, f"The y_score is less than 0"
        if not self.output.endswith('.json'):
            self.output += '.json'          
    
    def run(self):
        self.confusion_matrix()
        self.accuracy()
        self.balanced_accuracy()
        self.precision()
        self.recall()
        self.f1()
        self.auc()
    
    def confusion_matrix(self) -> None:
        self.tn, self.fp, self.fn, self.tp = metrics.confusion_matrix(y_true=self.y_true, y_pred=self.y_pred).ravel()
        
    def accuracy(self) -> None:
        self.acc = metrics.accuracy_score(y_true=self.y_true, y_pred=self.y_pred, normalize=True)
    
    def balanced_accuracy(self) -> None:
        """ 
        The balanced accuracy in binary and multiclass classification problems to deal with imbalanced datasets. 
        It is defined as the average of recall obtained on each class.
        """
        self.b_acc = metrics.balanced_accuracy_score(y_true=self.y_true, y_pred=self.y_pred)
        
    def precision(self) -> None:
        self.precision = metrics.precision_score(y_true=self.y_true, y_pred=self.y_pred)

    def recall(self) -> None:
        "Recall / TPR / Sensitivity"
        self.recall_score = metrics.recall_score(y_true=self.y_true, y_pred=self.y_pred)
    
    def f1(self) -> None:
        """
        F1 = 2 * (precision * recall) / (precision + recall)
        """
        self.f1_score = metrics.f1_score(y_true=self.y_true, y_pred=self.y_pred)
    
    def auc(self) -> None:
        self.fpr, self.tpr, self.thresholds = metrics.roc_curve(y_true=self.y_true, y_score=self.y_score)
        self.auc_score = metrics.roc_auc_score(y_true=self.y_true, y_score=self.y_score)
    
    def saveData(self) -> None:
        self.metrics_ = {
                        'confusion_matrix': {'TN': int(self.tn), 
                                             'FP': int(self.fp), 
                                             'FN': int(self.fn), 
                                             'TP': int(self.tp)
                                             },
                        'accuracy': self.acc,
                        'balanced_accuracy': self.b_acc,
                        'precision': self.precision,
                        'recall': self.recall_score,
                        'f1_score': self.f1_score,
                        'auc': self.auc_score,
                        'tpr': list(self.tpr),
                        'fpr': list(self.fpr),
                        }
        with open(self.output, 'w') as OUT:
            OUT.write(json.dumps(self.metrics_, indent=4))

    def roc_curve(self):
        plt.figure()
        lw = 2
        plt.figure(figsize=(5.5, 4))
        plt.plot(self.fpr, self.tpr, color='darkorange',
                lw=lw, label='ROC curve (area = %0.3f)' % self.auc_score)
        plt.plot([0, 1], [0, 1], color='gray', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        # plt.title('Receiver operating characteristic example')
        plt.legend(loc="lower right")
        if self.roc_fig != None:
            plt.savefig(self.roc_fig)
        


if __name__ == '__main__':
    y_pred = np.random.choice(2, size=100)
    y_true = np.random.choice(2, size=100)
    y_score = np.random.random(100)
    
    Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true, roc_fig='aa.png')
    
    print(Evaluation.metrics_)
   
            