import pandas as pd

def calculate_median_of_columns(df: pd.DataFrame) -> pd.Series:
    """
    Calcul de la médiane pour chaque colonne d'un DataFrame.

    Args:
        df (pd.DataFrame): Le DataFrame contenant les données.

    Returns:
        pd.Series: La médiane de chaque colonne.
    """
    return df.median()
