import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load dataframe from a given path

    Args:
        path (str): Path to the csv file

    Returns:
        pd.DataFrame: Processed dataframe
    """
    dfs = []
    for i in range(1, 6):
        dfs.append(pd.read_csv(path + f"_{i}.csv", index_col=0))
    df = pd.concat(dfs)
    df.index = pd.to_datetime(df.index, format="mixed").round("H")
    df = df.groupby(df.index).mean()
    df = df.replace(0, np.nan)
    return df
