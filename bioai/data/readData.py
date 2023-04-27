import os, sys 
import pandas as pd 


class ReadData:
    def __init__(self, dataFiles: list, labelFile: str):
        """ 
        dataFiles: input files: .csv, .csv.gz. || example: ['./example/cnv.csv.gz']
        labelFile: label files: .csv, .csv.gz  || example: './example/label.csv'
        """
        self.dataFiles = dataFiles
        self.labelFile = labelFile
        
        # check file
        self.check_files(self.dataFiles)
        self.check_files(self.labelFile)
        
    def run(self):
        """ 
        Return:
        datas: list[pd.DataFrame]
        label: pd.DataFrame
        """
        datas = self.readData()
        label = self.readLabel()
        return datas, label
    
    def readData(self):
        if isinstance(self.dataFiles, list):
            datas = []
            for f in self.dataFiles:
                datas.append(self.read_csv(file=f))
            return datas 
        # TODO: 只要一个组学数据呢
                
    def readLabel(self):
        return self.read_csv(self.labelFile)
    
    @staticmethod
    def check_files(files):
        """To check files.
        files (str or list)
        """
        if isinstance(files, list):
            for f in files:
                if not os.path.exists(f):
                    print('[Error] {} not found.'.format(f))
                    sys.exit(1)
        elif isinstance(files, str):
            if not os.path.exists(files):
                print('[Error] {} not found.'.format(files))
                sys.exit(1)
        else:
            print('[Error] {} file path is wrong.'.format(files))
            sys.exit(1)
    
    @staticmethod
    def read_csv(file):
        # read file
        if file.endswith('.csv'):
            df = pd.read_csv(file, index_col=0)
        elif file.endswith('.csv.gz'):
            df = pd.read_csv(file, compression='gzip', index_col=0)
        else:
            print('\n[Error]: The program cannot infer the format of {} . Currently, only the csv format is supported, please ensure that the file name suffix is .csv or .csv.gz.'.format(file))
            sys.exit(0)
        return df


if __name__ == '__main__':
    datas, label = ReadData(dataFiles=['./example/cnv.csv.gz'], labelFile='./example/label.csv').run()
    print(label)