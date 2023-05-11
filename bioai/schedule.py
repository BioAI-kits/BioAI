import argparse, warnings
from bioai.utils import getTime
from bioai.launcher import runRF, runXGBoost

warnings.filterwarnings('ignore')


class Schedule:
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
        group_program.add_argument("-h", "--help", action="help", help="show this help message and exit.")
            
    def register(self):
        # add random forest params
        self.randomForest()
        
        # add xgboost params
        self.xgboost()
        
        # root param parser
        args = self.parser.parse_args()
        
        # to perform program accordding to sub-parser
        args.func(args)
        
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
        rf_config.add_argument("-t", 
                            required=True,
                            type=str,
                            choices=['bc', 'mc', 're', 'auto'],
                            help="The task type of the model, currently supports classification and regression.\n" \
                                 "bc: to build a binary classification model\n" \
                                 "mc: to build a multi-classification model\n" \
                                 "re: to build a regression model\n" \
                                 "auto: automatically identify through label data.", 
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
        # set callback function
        rf_parser.set_defaults(func=runRF)
        
    def xgboost(self):
        example = "bioai-moi xgboost -i .\example\cnv.csv.gz -g cnv -i .\example\met.csv.gz -g met -o test -l .\example\label.csv"
        description = '-'*30 + f"\n\nBioAI can conveniently build AI models for single-omics or multi-omics data.\n\n{example}\n\n" + '-'*30
        
        xgboost_parser = self.subparsers.add_parser('xgboost', 
                                      help="""Build your model based on XGBoost.
                                           """,
                                      usage=argparse.SUPPRESS,
                                      description= description,
                                      formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=60)                   
                                      )
        xg_config = xgboost_parser.add_argument_group("Config Parameters")
        xg_config.add_argument("-i", 
                            required=True,
                            action='append',
                            type=str,
                            help="Input your data file with csv format.", 
                            metavar='')
        xg_config.add_argument("-g", 
                            required=True,
                            action='append',
                            type=str,
                            help="Input your data group.", 
                            metavar='')
        xg_config.add_argument("-l", 
                            required=True,
                            type=str,
                            help="Input your label file with csv format.", 
                            metavar='')
        xg_config.add_argument("-t", 
                            required=True,
                            type=str,
                            choices=['multi_cls', 'binary_cls'],
                            help="Task", 
                            metavar='')
        xg_config.add_argument("-o", 
                            default='Result' + self.now,
                            required=False,
                            help="Set the directory to save the results. Default: " + 'Result' + self.now, 
                            metavar='')
        
        xg_preprocess = xgboost_parser.add_argument_group("Preprocess Parameters")
        xg_preprocess.add_argument("-pm",
                                   type=str,
                                   default='chi2',
                                   choices=['chi2', 'annova'],
                                   help="The method of feature extraction currently supports: chi2, annov."
                                   )
        xg_preprocess.add_argument("-k",
                                   type=float or int, 
                                   default=0.5,
                                   metavar='',
                                   help="If set to a number between 0 and 1, it indicates the percentage of features retained.\n" \
                                        "If set to a positive integer, indicates the number of features to select. " \
                                        "Default is 0.5"
                                   )
        
        xg_model = xgboost_parser.add_argument_group("Parameters for Random Forest Algorithm")
        xg_model.add_argument('-ts',
                            default=0.3,
                            type=float,
                            required=False,
                            metavar='',
                            help='The proportion of the dataset to include in the test split (0,1). Default is 0.3.'
                            )
        xg_model.add_argument("-n", 
                            default=100,
                            required=False,
                            type=int,
                            help="Number of gradient boosted trees. Equivalent to number of boosting rounds. Default is 100.", 
                            metavar='')
        xg_model.add_argument('-d',
                            default=5,
                            type=int,
                            required=False,
                            metavar='',
                            help="The maximum depth of the tree. Default is 5."
                            )
        xg_model.add_argument('-r',
                            default=0.0001,
                            type=float,
                            required=False,
                            metavar='',
                            help="Boosting learning rate. Default is 0.0001"
                            )
        xg_model.add_argument('-s',
                            default=42,
                            type=int,
                            required=False,
                            metavar='',
                            help="Random number seed. Default is 42."
                            )
        # set callback function
        xgboost_parser.set_defaults(func=runXGBoost)
    

   
if __name__ == '__main__':
    args = Schedule().register()

