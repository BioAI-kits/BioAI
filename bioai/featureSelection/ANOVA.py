import pandas as pd
from sklearn.feature_selection import SelectPercentile


# ANOVA
def anova(args, data, label):
    """
    args: parameters
    data: data matrix (numpy.array).
    label: sample label.

    Return:
        selected omic data with DataFrame format.
    """
    select = SelectPercentile(percentile=args.percentile)
    select.fit(X=data, y=label)
    features = df_omic.columns.values[select.get_support()]  # features selected by ANOVA.
    return df_omic[features]


if __name__ == '__main__':
    import numpy as np 

