import numpy as np 
from sklearn import feature_selection as FS 


class Select:
    def __init__(self, 
                 data: np.ndarray, 
                 label: np.ndarray, 
                 featNum: float or int, 
                 featName: np.ndarray,
                 method='chi'
                 ) -> None:
        """ 
        data: 
        """
        self.data = data
        self.label = label
        self.featNum = featNum
        self.sampleNum = int(len(self.label))
        self.featName = featName
        self.method = method
        self.check()
        
    def check(self):
        # 如果通过百分比提取特征
        if 0 < self.featNum < 1: 
            self.featNum = int(self.sampleNum*self.featNum)
        # 如果设置的特征提取数量 大于 数据集特征数据，则提取所有特征
        elif self.featNum > self.sampleNum:
            self.featNum = self.sampleNum
        else:
            print("Error: please check the number of feature selection.")
    
    def chi(self):
        selector = FS.SelectKBest(FS.chi2, k=self.featNum).fit(self.data, self.label)
        # transformer data
        selected_data = selector.transform(self.data)
        selected_feat = self.featName[selector.get_support()]
        return selected_data, selected_feat
    
    def anova(self):
        pass 
    
    def lasso(self):
        pass 
    
    def ref(self):
        pass 
    
    def pca(self):
        pass 
    
    def run(self):
        if self.method == 'chi':
            selected_data, selected_feat= self.chi()
        
            
        
        return selected_data, selected_feat
    
    

if __name__ == '__main__':
    data = np.random.rand(32, 20)
    featNames = np.array(['feat' + str(i) for i in range(20)])
    labels = np.random.choice(2, 32)
    

    dat, feat = Select(data=data, 
                       label=labels, 
                       featName=featNames, 
                       featNum=0.5,
                       method='chi'
                       ).run()

    print(dat.shape, feat)


