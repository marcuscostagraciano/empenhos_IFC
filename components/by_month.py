import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager

def by_month(onlyTable=False):
    df_manager = DataframeManager()  

    st.caption("## Empenhado")
    st.caption('Relatório do dinheiro requisitados para o governo pela reitoria do IF')
    df_moth_detail = df_manager.get_df_month_detail(value='Empenhado')
    if onlyTable:
        st.table(df_moth_detail)
    else:
        chart_options = get_options_month(df_moth_detail)
        st_echarts(chart_options, height="500px", key="df_moth_empenho")

    st.caption("## Liquidado")
    st.caption('Relatório do dinheiro investido pela reitoria do IF')
    df_moth_detail = df_manager.get_df_month_detail(value='Liquidado')
    if onlyTable:
        st.table(df_moth_detail)
    else:
        chart_options = get_options_month(df_moth_detail)
        st_echarts(chart_options, height="500px", key="df_moth_liquidado")