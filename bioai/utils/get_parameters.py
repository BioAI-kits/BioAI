import argparse, warnings
from bioai.utils.getTime import getTime

warnings.filterwarnings('ignore')


class GetArgs:
    def __init__(self) -> None:
        self.now = getTime()
        info = "BioAI can conveniently build AI models for single-omics or multi-omics data.\n\n" \
               "Author: Billy Liang \n\n" \
               "Email: liangbilin0324@163.com \n\n" \
               "GitHub: https://github.com/BioAI-kits/BioAI \n\n"

        description = f"{'-'*30}\n\n{info}\n\n{'-'*30}"
        self.parser = argparse.ArgumentParser(
                                     prog='BioAI',
                                     usage=argparse.SUPPRESS,
                                     description=description, 
                                     epilog=" ",
                                     add_help=False,
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=60),
                                     )
       
        self.subparsers = self.parser.add_subparsers(title='BioAI currently includes the following subcommands', 
                                                     metavar=' '*8,
                                                    )
        # program params
        group_program = self.parser.add_argument_group("Program paramters")
        group_program.add_argument("-h", action="help", help="show this help message and exit.")
        group_program.add_argument("-v", help="show the program version.", metavar='')       
            
    def register(self):
        # Random Forest Params
        self.randomForest()
        
        # XGboost Params
        
        args = self.parser.parse_args()
        return args
    
    
    def randomForest(self):
        example = "bioai-moi RF -i .\example\cnv.csv.gz -g cnv -i .\example\met.csv.gz -g met -o test -l .\example\label.csv"
        description = '-'*30 + f"\n\nBioAI can conveniently build AI models for single-omics or multi-omics data.\n\n{example}\n\n" + '-'*30
        
        rf_parser = self.subparsers.add_parser('RF', 
                                      help="""Build your model based on a random forest.
                                           """,
                                      usage=argparse.SUPPRESS,
                                      description= description,
                                      formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=60)                   
                                      )
        rf_config = rf_parser.add_argument_group("Config Parameters")
        rf_config.add_argument("-i", 
                            required=True,
                            action='append',
                            type=str,
                            help="Input your data file with csv format.", 
                            metavar='')
        rf_config.add_argument("-g", 
                            required=True,
                            action='append',
                            type=str,
                            help="Input your data group.", 
                            metavar='')
        rf_config.add_argument("-l", 
                            required=True,
                            type=str,
                            help="Input your label file with csv format.", 
                            metavar='')
        rf_config.add_argument("-o", 
                            default='Result' + self.now,
                            required=False,
                            help="Set the directory to save the results. Default: " + 'Result' + self.now, 
                            metavar='')
        
        rf_preprocess = rf_parser.add_argument_group("Preprocess Parameters")
        rf_preprocess.add_argument("-pm",
                                   type=str,
                                   default='chi2',
                                   choices=['chi2', 'annova'],
                                   help="The method of feature extraction currently supports: chi2, annov."
                                   )
        rf_preprocess.add_argument("-k",
                                   type=float or int, 
                                   default=0.5,
                                   metavar='',
                                   help="If set to a number between 0 and 1, it indicates the percentage of features retained.\n" \
                                        "If set to a positive integer, indicates the number of features to select. " \
                                        "Default is 0.5"
                                   )
        
        rf_model = rf_parser.add_argument_group("Parameters for Random Forest Algorithm")
        rf_model.add_argument('-ts',
                            default=0.3,
                            type=float,
                            required=False,
                            metavar='',
                            help='The proportion of the dataset to include in the test split (0,1). Default is 0.3.'
                            )
        rf_model.add_argument("-n", 
                            default=100,
                            required=False,
                            type=int,
                            help="The number of trees in the forest. Default is 100.", 
                            metavar='')
        rf_model.add_argument('-d',
                            default=5,
                            type=int,
                            required=False,
                            metavar='',
                            help="The maximum depth of the tree. Default is 5."
                            )
        rf_model.add_argument('-s',
                            default=42,
                            type=int,
                            required=False,
                            metavar='',
                            help="Random number seed. Default is 42."
                            )
        
    
    def xgboost(self):
        pass 
    
if __name__ == '__main__':
    args = GetArgs().register()
    print(args)

