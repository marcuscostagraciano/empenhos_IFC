import streamlit as st
import pandas as pd
from utils import *
from classes.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def by_nature_details(onlyTable=False):
    df_manager = DataframeManager()
    nature = [item for item in st.session_state.df_master["Natureza Despesa"].unique()]
    st.session_state.nature = st.selectbox(
        label="Selecione a Natureza da Despesa", 
        options=nature, 
        key=f'{onlyTable}select_nature', 
        index=None
    )
    if st.session_state.nature == None:
        st.info("Nenhuma Natureza Despesa selecionada", icon="ℹ️")
    else:
        option2, option3, df_by_nature_test_1, df_by_nature_test_2, df_by_nature_test_3 = df_manager.get_df_by_nature(st.session_state.nature)
        st_echarts(options=option2, height="500px")
        if onlyTable:
            st.table(df_by_nature_test_2)
            st_echarts(options=option3, height="500px")
