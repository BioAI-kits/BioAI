def checkTask(labels):
    import pandas as pd 
    import sys 
    label = pd.value_counts(labels).index
    if len(label) == 2 and label.dtype in ['int', 'int32', 'int64']:
        return 'bc'
    elif len(label) > 2 and label.dtype in ['int', 'int32', 'int64']:
        return 'mc'
    elif label.dtype not in ['int', 'int32', 'int64']:
        return 're'
    else:
        print('[Error] Failed to automatically identify the task type, please set it manually.')
        sys.exit(1)