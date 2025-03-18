import pandas as pd

def add_data_to_dataframe(df, new_data):
    """
    Adds new data (single row or multiple rows) to an existing DataFrame.
    
    Parameters:
        df (pd.DataFrame): The original DataFrame.
        new_data (dict or list of dicts or pd.DataFrame): 
            - If dict: Adds a single row.
            - If list of dicts: Adds multiple rows.
            - If DataFrame: Merges another DataFrame.
    
    Returns:
        pd.DataFrame: Updated DataFrame with new data.
    """
    if isinstance(new_data, dict):  # Single row
        new_data = pd.DataFrame([new_data])  
    elif isinstance(new_data, list):  # Multiple rows
        new_data = pd.DataFrame(new_data)  
    elif not isinstance(new_data, pd.DataFrame):
        raise ValueError("new_data must be a dict, list of dicts, or a Pandas DataFrame.")
    
    return pd.concat([df, new_data], ignore_index=True)