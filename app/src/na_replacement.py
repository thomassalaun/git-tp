import pandas as pd

def impute_missing_with_mean(df:pd.DataFrame, column_name:str) -> pd.DataFrame:
    """
    Remplace les valeurs manquantes d'une colonne numérique d'un DataFrame 
    par la moyenne de cette colonne.
    
    Args:
        df (pd.DataFrame): Le DataFrame contenant la colonne à traiter.
        column_name (str): Le nom de la colonne à imputer.
    
    Returns:
        pd.DataFrame: Le DataFrame avec les valeurs imputées.
    """
    if column_name not in df.columns:
        raise ValueError(f"La colonne '{column_name}' n'existe pas dans le DataFrame.")
    
    if not pd.api.types.is_numeric_dtype(df[column_name]):
        raise ValueError(f"La colonne '{column_name}' n'est pas de type numérique.")
    
    mean_value = df[column_name].mean(skipna=True)
    df[column_name] = df[column_name].fillna(mean_value)
    
    return df
