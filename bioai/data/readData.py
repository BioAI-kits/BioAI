import pandas as pd 


class ReadData:
    def __init__(self, files: list, label: str) -> None:
        """ 
        files: input files: .csv, .csv.gz, .tsv, .tsv.gz 
        label: label files: .csv, .csv.gz, .tsv, .tsv.gz
        """
        self.files = files 
    
    def read_csv(self):
        pass 
    
    def read_tsv(self):
        pass 
    
    def read_label(self):
        pass 
    
    
        



