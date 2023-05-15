def runRF(args):
    import sys 
    from bioai.data import ReadData
    from bioai.preprocessing.dataPreprocessing import CleanPipeline, percent_split
    from bioai.algorithms.classifier import RandomForestClassification
    from bioai.algorithms.regressor import RandomForestRegression
    from bioai.utils import getTime
    from bioai.utils.check import checkTask
    
    # 1. get parms
    dataFiles = args.i 
    labelFile = args.l 
    groupNames = args.g 
    output = args.o
    task = args.t
    n_estimators = args.n
    max_depth = args.d
    seed = args.s
      
    # 2. read data
    datas, label = ReadData(dataFiles=dataFiles,
                            labelFile=labelFile,
                            groupName=groupNames
                            ).run()
    
    # 3. preprocessing
    Data, Label = CleanPipeline(datas=datas, label=label).run()
    
    # 4. data spliting
    X_train, X_test, Y_train, Y_test = percent_split(Data, Label)
    
    # 5. build model
    if task == 'auto':
        task = checkTask(Label.label.values)
    ## 5.1 classification model
    if task in ['bc', 'mc']: 
        model = RandomForestClassification(X_train=X_train, 
                                           X_test=X_test,
                                           Y_train=Y_train,
                                           Y_test=Y_test,
                                           n_estimators=n_estimators,
                                           max_depth=max_depth,
                                           output=output, 
                                           task=task,
                                           random_state=seed
                                            )
        model.buildModel()
        # evaluation
        model.evaluation()
        
    ## 5.2 regression model
    elif task == 're':
        model = RandomForestRegression(X_train=X_train, 
                                        X_test=X_test,
                                        Y_train=Y_train,
                                        Y_test=Y_test,
                                        n_estimators=n_estimators,
                                        max_depth=max_depth,
                                        output=output, 
                                        task=task,
                                        random_state=seed
                                    )
        model.buildModel()
        model.evaluation()
     
    else:
        print('[Error] Failed to automatically identify the task type, please set it manually.')
        sys.exit(1)

    # 6. finished
    info = f"{getTime()} >>> The program has been executed.\n"
    print(info)
        