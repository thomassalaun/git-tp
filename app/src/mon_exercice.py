import pandas as pd

def calculate_median_of_columns(df: pd.DataFrame) -> pd.Series:
    return df.median()
