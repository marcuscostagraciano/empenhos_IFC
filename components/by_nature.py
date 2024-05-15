import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager

def by_nature(onlyTable=False):
    df_manager = DataframeManager()  
    st.session_state.month = st.selectbox(
        label="Selecione o mês",
        key=f'41232134123{onlyTable}',
        index=None,
        options=["01", "02", "03", "04"],
        placeholder="Selecione o mês",
    )
    if st.session_state.month == None:
        st.info("Selecione um mês", icon="ℹ️")

    row1 = st.columns(2, gap="medium")
    with row1[0]:
        if not st.session_state.month == None:
            st.caption("## Empenhado")
            st.caption('Relatório do dinheiro requisitados para o governo pela reitoria do IF')
            df_moth_detail = df_manager.get_df_month_detail(value='Empenhado')
            if onlyTable:
                st.table(df_moth_detail)
            else:
                chart_options = get_options_month_detail(df_moth_detail)
                st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_empenho")

    with row1[1]:
        if not st.session_state.month == None:
            st.caption("## Liquidado")
            st.caption('Relatório do dinheiro investido pela reitoria do IF')
            df_moth_detail = df_manager.get_df_month_detail(value='Liquidado')
            if onlyTable:
                st.table(df_moth_detail)
            else:
                chart_options = get_options_month_detail(df_moth_detail)
                st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_liquidado")
