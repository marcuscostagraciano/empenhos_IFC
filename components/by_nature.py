import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from utils import *
from classes.dataframe_manager import DataframeManager

def by_nature(onlyTable=False):
    df_manager = DataframeManager()  
    months = [formatted_months(month) for month in st.session_state.df_master['Mês'].unique()]
    st.session_state.month = st.selectbox(
        label="Selecione o mês",
        key=f'get_month_{onlyTable}',
        index=None,
        options=months,
        placeholder="Selecione o mês",
    )
    if st.session_state.month == None:
        st.info("Selecione um mês", icon="ℹ️")

    row1 = st.columns(2, gap="medium")
    with row1[0]:
        if not st.session_state.month == None:
            st.caption("## Empenhado")
            st.caption('Relatório do dinheiro requisitados para o governo pela reitoria do IF')
            [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value='Empenhado')
            if onlyTable:
                st.table(formatted_datas)
            else:
                chart_options = get_options_month_detail(raw_datas)
                st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_comitted")

    with row1[1]:
        if not st.session_state.month == None:
            st.caption("## Liquidado")
            st.caption('Relatório do dinheiro investido pela reitoria do IF')
            [raw_datas, formatted_datas] = df_manager.get_df_month_detail(value='Liquidado')
            if onlyTable:
                st.table(formatted_datas)
            else:
                chart_options = get_options_month_detail(raw_datas)
                st_echarts(chart_options, height="500px", key=f"{st.session_state}df_moth_detail_settled")
