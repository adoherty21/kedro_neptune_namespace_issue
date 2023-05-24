import pandas as pd

def read_raw_data(column_name, neptune_run=None):

    df = pd.DataFrame({"index": [1,2,3,4,5], column_name: [6,7,8,9,10]})

    if neptune_run is not None:
        neptune_run["df"] = df

    return df