import streamlit as st
import pandas as pd
from utils import *
from classes.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def by_nature_details(onlyTable=False):
    df_manager = DataframeManager()
    nature = [item for item in st.session_state.df_master["Natureza Despesa"].unique()]
    st.session_state.nature = st.multiselect(
        label="Selecione a Natureza Despesa",
        key=f"get_m123onth_{onlyTable}_{id}",
        options=nature,
        placeholder="Ex: LOCACAO DE MAO-DE-OBRA, SERVICOS DE TECNOLOGIA DA INFORMACAO E COMUNICACAO - PJ	",
    )
    if st.session_state.nature == []:
        st.info("Selecione uma Natureza Despesa", icon="ℹ️")
    else:
        [option, df_by_nature] = df_manager.get_df_by_nature(st.session_state.nature)
        
        with st.expander("Dados Gerais", expanded=True):
            st.table(df_by_nature)
        with st.expander("Dados Especificos", expanded=True):
            st_echarts(options=option, height="500px", key=f'{onlyTable}_id_dessa_porra2')