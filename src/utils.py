import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load dataframe from a given path

    Args:
        path (str): Path to the csv file

    Returns:
        pd.DataFrame: Processed dataframe
    """
    df = pd.read_csv(path, index_col=0)
    df.index = pd.to_datetime(df.index, format="mixed").normalize()
    df = df.groupby(df.index).sum()
    df = df.replace(0, np.nan)
    return df
