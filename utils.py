import pandas as pd
import altair as alt
import streamlit as st

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

def create_simple_chart():
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 30, 40, 50]
    })

    chart = (
        alt.Chart(df)
        .mark_line(point=True)
        .encode(x='x', y='y')
    )

    return chart

def get_campus_option(id):
    """
    This function returns the selected campus option.

    Returns:
        str: The selected campus option.
    """

    campus_option = st.selectbox(
        f"Selecione o Campus {id}",
        ["Araquari", "Camboriú", "Sombrio", "Videira"],
    )

    return campus_option