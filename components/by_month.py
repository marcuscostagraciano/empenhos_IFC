import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager

def by_month(onlyTable=False):
    df_manager = DataframeManager()  
    if not onlyTable:  
        st.write("#")
        row_option_month = st.columns((2, 7), gap="medium")
        with row_option_month[0]:
            st.write("**Selecione o Mês para filtrar os resultados**")
        with row_option_month[1]:
            st.session_state.month = st.selectbox(
                label="",
                label_visibility="collapsed",
                key=12321341234,
                options=["01", "02", "03", "04"],
            )

    row1 = st.columns(2, gap="medium")
    with row1[0]:
        st.caption("## Empenhado")
        st.caption('Relatório do dinheiro requisitados para o governo pela reitoria do IF')
        df_moth_detail = df_manager.get_df_month_detail(value='Empenhado')
        if onlyTable:
            st.table(df_moth_detail)
        else:
            chart_options = get_options_month_detail(df_moth_detail)
            st_echarts(chart_options, height="1000px", key="df_moth_detail_empenho")

    with row1[1]:
        st.caption("## Liquidado")
        st.caption('Relatório do dinheiro investido pela reitoria do IF')
        df_moth_detail = df_manager.get_df_month_detail(value='Liquidado')
        if onlyTable:
            st.table(df_moth_detail)
        else:
            chart_options = get_options_month_detail(df_moth_detail)
            st_echarts(chart_options, height="1000px", key="df_moth_detail_liquidado")