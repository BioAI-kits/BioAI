import numpy as np 
import pandas as pd 
from bioai.utils.getTime import getTime

class Pipeline:
    def __init__(self, datas:list, label:pd.DataFrame) -> None:
        self.datas = datas
        self.label = label
        
    def run(self):
        # perform merge datas
        self.mergeData() 

        # perform norm
        self.normlization()
        
        return self.DataNorm, self.Label
    
    def mergeData(self):
        """ 
        merge data and label accordding sample id.
        """
        info = f"{getTime()} >>> Merge the data according to the sample id, and only keep the samples with the shared id...\n"
        print(info)
        
        datas_tmp = self.datas
        datas_tmp.append(self.label)
        data_left = datas_tmp[0]
        for idx in range(1, len(datas_tmp)):
            data_left = pd.merge(left=data_left, 
                                 right=datas_tmp[idx], 
                                 how='inner', 
                                 left_index=True, 
                                 right_index=True
                                 )
        self.Data = data_left.iloc[:, :-1]
        self.Label = data_left.iloc[:, -1].values

        info = f"{getTime()} >>> The number of samples retained is: {self.Label.shape[0]} ."
        print(info)
    
    # 填充缺失值
    def imputation(self):
        pass 
    
    
    # 移除缺失值太多的特征
    def remove_features(self):
        pass 
    
    
    # 归一化
    def normlization(self):
        self.DataNorm = (self.Data - self.Data.min())/(self.Data.max() - self.Data.min())
    

