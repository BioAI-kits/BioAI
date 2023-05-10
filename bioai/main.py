from bioai.utils.getParams import GetArgs
from bioai.data.readData import ReadData
from bioai.preprocessing.dataPreprocessing.cleanData import Pipeline
from bioai.preprocessing.dataPreprocessing.splitData import percent_split
from bioai.algorithms.multi_omics.classification.RandomForest import Model


def moi():
    # parms
    args = GetArgs().register()
    dataFiles = args.i 
    groupNames = args.g 
    labelFile = args.l 
    output = args.o
    task = args.t
    
    print(args)
    # read data
    datas, label = ReadData(dataFiles=dataFiles, 
                            labelFile=labelFile,
                            groupName=groupNames
                            ).run()

    # preprocessing
    Data, Label = Pipeline(datas=datas, label=label).run()

    # split data
    X_train, X_test, Y_train, Y_test = percent_split(Data, Label)

    # build model
    RF = Model(X_train, X_test, Y_train.label.values, Y_test.label.values,
                output=output, task=task
                )
    RF.buildModel()

    # evaluation
    RF.evaluation()

    # finished
    

def somic():
    # read data
    datas, label = ReadData(dataFiles=['./example/cnv.csv.gz',
                                        './example/met.csv.gz',
                                        './example/rna.csv.gz'
                                        ], 
                        labelFile='./example/label.csv',
                        groupName=['cnv', 'met', 'rna']
                        ).run()

    # preprocessing
    Data, Label = Pipeline(datas=datas, label=label).run()

    # split data
    X_train, X_test, Y_train, Y_test = percent_split(Data, Label)

    # build model
    RF = Model(X_train, X_test, Y_train.label.values, Y_test.label.values,
                output='../RF_Forest',
                )
    RF.buildModel()

    # evaluation
    RF.evaluation()


if __name__ == '__main__':
    moi()
