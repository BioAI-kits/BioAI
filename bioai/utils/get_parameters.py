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
        description = '-'*30 + "\n\nBioAI can conveniently build AI models for single-omics or multi-omics data.\n\n" + '-'*30
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
                            type=str,
                            help="Input your data file with csv format.", 
                            metavar='')
        rf_config.add_argument("-o", 
                            default='Result' + self.now,
                            required=False,
                            help="Set the directory to save the results. Default: " + 'Result' + self.now, 
                            metavar='')
        
        rf_model = rf_parser.add_argument_group("Parameters for Random Forest Algorithm")
        rf_model.add_argument('-ts',
                            default=0.3,
                            type=float,
                            required=False,
                            metavar='',
                            help='It should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. Default is 0.3.'
                            )
        rf_model.add_argument("-n", 
                            default=100,
                            required=False,
                            type=int,
                            help="The number of trees in the forest. Default is 100.", 
                            metavar='')
        rf_model.add_argument('-m',
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
    
    
    

def get_args():
    now = getTime()
    description = '-'*30 + "\n\nBioAI can conveniently build AI models for single-omics or multi-omics data.\n\n" + '-'*30
    parser = argparse.ArgumentParser(
                                     prog='BioAI',
                                     usage=argparse.SUPPRESS,
                                     description=description, 
                                     epilog=" ",
                                     add_help=False,
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=60),
                                     )
       
    subparsers = parser.add_subparsers(title='BioAI currently designs the following subcommands', 
                                       metavar=' '*8,
                                       )
    
    # program params
    group_program = parser.add_argument_group("Program paramters")
    group_program.add_argument("-h", action="help", help="show this help message and exit.")
    group_program.add_argument("-v", help="show the program version.", metavar='')    
    
    # sub-cmd: Random Forest
    rf_parser = subparsers.add_parser('RF', 
                                      help="""Build your model based on a random forest.
                                           """,
                                      usage=argparse.SUPPRESS,                       
                                      )
    rf_config = rf_parser.add_argument_group("Config Parameters")
    rf_config.add_argument("-i", 
                           required=True,
                           type=str,
                           help="Input your data file with csv format.", 
                           metavar='')
    rf_config.add_argument("-o", 
                           default='Result' + now,
                           required=False,
                           help="Set the directory to save the results. Default: " + 'Result' + now, 
                           metavar='')
    
    rf_model = rf_parser.add_argument_group("Parameters for Random Forest Algorithm")
    rf_model.add_argument('-ts',
                          default=0.3,
                          type=float,
                          required=False,
                          metavar='',
                          choices=range(0,1),
                          help='It should be between 0.0 and 1.0 and represent the proportion of the dataset to include in the test split. Default is 0.3.'
                          )
    rf_model.add_argument("-n", 
                          default=100,
                          required=False,
                          type=int,
                          help="The number of trees in the forest. Default is 100.", 
                          metavar='')
    rf_model.add_argument('-m',
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


    # # sub-cmd: SVM
    # svm_parser = subparsers.add_parser('svm', help='SVM')
    # svm_parser_group_program = svm_parser.add_argument_group("SVM >>>")
    # svm_parser_group_program.add_argument('-a', required=True, metavar='', help='Input files')
    
    # # sub-cmd: XGboost
    # xgboost_parser = subparsers.add_parser('xgboost')
    # xgboost_parser_group_program = svm_parser.add_argument_group("xgboost >>>")
    # # xgboost_parser_group_program.add_argument('-i', '--input', required=True, metavar='', help='Input files')
    
    # # sub-cmd: Logistic regression
    # lr_parser = subparsers.add_parser('lr')
    # lr_parser_group_program = lr_parser.add_argument_group("LR >>>")
    # # lr_parser_group_program.add_argument('-i', '--input', required=True, metavar='', help='Input files')
    
    

    
    args = parser.parse_args()
    
    print(args.ts)
    
    return args





if __name__ == '__main__':
    # get_args()
    args = GetArgs().register()
    print(args.ts)

