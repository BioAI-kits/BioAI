def runRF(args):
    from bioai.data import ReadData
    from bioai.preprocessing.dataPreprocessing import CleanPipeline, percent_split
    from bioai.algorithms.classifier import RandomForestClassification
    from bioai.utils import getTime
    
    # get parms
    dataFiles = args.i 
    labelFile = args.l 
    groupNames = args.g 
    output = args.o
    task = args.t
    
    # TODO: 根据task配置计算流程
    
    
    # read data
    datas, label = ReadData(dataFiles=dataFiles,
                            labelFile=labelFile,
                            groupName=groupNames
                            ).run()
    
    # preprocessing
    Data, Label = CleanPipeline(datas=datas, label=label).run()
    
    # data spliting
    X_train, X_test, Y_train, Y_test = percent_split(Data, Label)
    
    # build model
    model = RandomForestClassification(X_train, X_test, Y_train.label.values, Y_test.label.values,
                                    output=output, task=task
                                    )
    model.buildModel()

    # evaluation
    model.evaluation()

    # finished
    info = f"{getTime()} >>> The program has been executed.\n"
    print(info)