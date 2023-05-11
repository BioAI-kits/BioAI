import numpy as np 
import pandas as pd 
from bioai.utils.getTime import getTime


class CleanPipeline:
    def __init__(self, datas:list, label:pd.DataFrame, groupName=None) -> None:
        self.datas = datas
        self.label = label
        self.group = groupName
        
    def run(self):
        # perform merge datas
        self.merge() 

        # imputation
        self.imputation()
        
        # perform norm
        self.normlization()
        
        return self.DataNorm, self.Label
    
    def merge(self):
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
        self.Label = data_left.iloc[:, [-1]]

        info = f"{getTime()} >>> The number of samples retained is: {self.Label.shape[0]} \n"
        print(info)
    
    
    def inverse_merge(self):
        pass 
    
    
    # 填充缺失值
    def imputation(self):
        self.Data = self.Data.fillna(0)
    
    
    # 移除缺失值太多的特征
    def remove_features(self):
        pass 
    
    
    # 归一化
    def normlization(self):
        self.DataNorm = (self.Data - self.Data.min())/(self.Data.max() - self.Data.min())
    

