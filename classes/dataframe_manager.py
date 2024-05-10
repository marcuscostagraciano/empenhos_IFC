import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

class DataframeManager:
    def __init__(self):
        self.init_session_state()

    def init_session_state(self):
        if "error_message" not in st.session_state:
            st.session_state.error_message = ''
        if "df_master" not in st.session_state:
            st.session_state.df_master = pd.read_csv("assets/xls/empenhos.csv", encoding='ISO-8859-1', sep=";", decimal=",")
    
    def get_df_month(self):
        self.to_float()
        visible_columns = [
            'Mês',
            'Empenhado',
            'Liquidado',
        ]
        df = st.session_state.df_master[visible_columns]
        df_month = df.groupby(['Mês'])[['Empenhado', 'Liquidado']].sum().reset_index()
        df_month['Empenhado (R$)'] = st.session_state.df_master['Empenhado'].map('R$ {:,.2f}'.format)
        df_month['Liquidado (R$)'] = st.session_state.df_master['Liquidado'].map('R$ {:,.2f}'.format)
        
        return df_month[['Mês', 'Empenhado (R$)', 'Liquidado (R$)']]

    def clean_df(self):
        pass
        
    def to_float(self):
        st.session_state.df_master['Empenhado'] = st.session_state.df_master['Empenhado'].str.replace('.', '').str.replace(',', '.').astype(float)
        st.session_state.df_master['Liquidado'] = st.session_state.df_master['Liquidado'].str.replace('.', '').str.replace(',', '.').astype(float)

