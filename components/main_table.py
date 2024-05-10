import streamlit as st
import pandas as pd
from classes.dataframe_manager import DataframeManager

def main_table():
    df_manager = DataframeManager()
    campus = 'Araquari'
    st.write(f"## Empenhado x Liquidado (Mês a Mês)")
    st.caption(f"Este gráfico apresenta a evolução dos valores empenhados e liquidados pelo IFC Campus {campus} ao longo dos meses.")
    df_month = df_manager.get_df_month()
    st.table(df_month)