import pandas as pd

def clean_convert_column(df, column_name):
    """
    This function cleans and converts a column to float, handling various decimal separators.

    Args:
        df (pandas.DataFrame): The DataFrame containing the column to clean.
        column_name (str): The name of the column to clean and convert.

    Returns:
        pandas.DataFrame: The DataFrame with the cleaned and converted column.
    """

    # Replace thousand separators with decimals (assuming '.' is decimal separator)
    df[column_name] = df[column_name].str.replace(',', '.')

    # Handle potential decimal separators other than '.' (e.g., ',')
    df[column_name] = df[column_name].str.replace(r"[^\d\-+\.]", "", regex=True)

    # Try converting to float, replacing errors with NaN (or a specified value)
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

    return df
