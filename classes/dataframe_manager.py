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
        if "month" not in st.session_state:
            st.session_state.month = "01"
    
    def get_df_month(self):
        self.to_float()
        visible_columns = [
            'Mês',
            'Empenhado',
            'Liquidado',
        ]
        df = st.session_state.df_master[visible_columns]
        df_month = df.groupby(['Mês'])[['Empenhado', 'Liquidado']].sum().reset_index()
        df_month['Empenhado (R$)'] = df_month['Empenhado'].map('R$ {:,.2f}'.format)
        df_month['Liquidado (R$)'] = df_month['Liquidado'].map('R$ {:,.2f}'.format)
        
        return df_month[['Mês', 'Empenhado (R$)', 'Liquidado (R$)']]

    def get_df_month_detail(self, value='Empenhado'):
        self.to_float()
        visible_columns = [
            'Natureza Despesa',
            'Mês',
            'Empenhado',
            'Liquidado',
        ]

        df = st.session_state.df_master[visible_columns]

        df_month_detail = df.groupby(['Mês', 'Natureza Despesa'])[['Empenhado', 'Liquidado']].sum().reset_index()
        df_month_detail['Empenhado (R$)'] = st.session_state.df_master['Empenhado'].map('R$ {:,.2f}'.format)
        df_month_detail['Liquidado (R$)'] = st.session_state.df_master['Liquidado'].map('R$ {:,.2f}'.format)

        pivoted = pd.pivot_table(df_month_detail, values=value, index='Natureza Despesa', columns='Mês')
        pivoted.columns = ['01/2024', '02/2024', '03/2024', '04/2024']
        pivoted = pivoted.fillna(0)
        pivoted_reset = pivoted.reset_index()
        
        return pivoted_reset

    def clean_df(self):
        pass
        
    def to_float(self):
        if st.session_state.df_master['Empenhado'].apply(lambda x: isinstance(x, str)).any():
            st.session_state.df_master['Empenhado'] = st.session_state.df_master['Empenhado'].str.replace('.', '').str.replace(',', '.').astype(float)
        if st.session_state.df_master['Liquidado'].apply(lambda x: isinstance(x, str)).any():
            st.session_state.df_master['Liquidado'] = st.session_state.df_master['Liquidado'].str.replace('.', '').str.replace(',', '.').astype(float)

