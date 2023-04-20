import argparse, warnings


warnings.filterwarnings('ignore')


def get_args():
    parser = argparse.ArgumentParser(
                                     prog='BioAI',
                                     usage="\n>>> \n" + '-'*30,
                                     description="description>>> \n" + '-'*30, 
                                     epilog=" ",
                                     add_help=False,
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=50),
                                     )

    # program params
    group_program = parser.add_argument_group("Program paramters")
    group_program.add_argument("-h", "--help", action="help", help="show this help message and exit.")
    group_program.add_argument("-v", "--version", help="show the program version.", metavar='')
    
    # input params
    group_input = parser.add_argument_group("Data paramters")
    group_input.add_argument("-i", "--input", required=True, action='append',help="Input data file with .csv format.", metavar='')
    group_input.add_argument("-n", "--name", required=False, action='append',help="(optional) Input data names.", metavar='')

    # preprocess
    group_preprocess = parser.add_argument_group("Data preprocess")
    group_preprocess.add_argument("-p", "--preprocess", required=False, default='REF', metavar="",
                                  help="The method of data preprocessing, the current version supports: PCA, REF, LASSO.\nDefault is REF."
                                  )
    

    
    args = parser.parse_args()
    
    print(args.input)
    return args





if __name__ == '__main__':
    get_args()

