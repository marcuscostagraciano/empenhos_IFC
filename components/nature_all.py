import streamlit as st
from utils import *
from classes.dataframe_manager import DataframeManager
from streamlit_echarts import st_echarts

def nature_all(onlyTable=False):
    df_manager = DataframeManager()
    months = [formatted_months(month) for month in st.session_state.df_master["Mês"].unique()]
    [option, get_dataframe_by_nature] = df_manager.get_df_by_all_nature()
    options = {
        **option,
        "title": {
            "text": '',
        },
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'shadow'
            },
        },
        "legend": {
            "data": ['Empenhado', 'Liquidado'],
            "left": '0%',
            "top": '1%',
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "top": '8%',
            "containLabel": True
        },
        "xAxis": {
            "type": 'value',
            "boundaryGap": [0, 0.01]
        }
    }

    if onlyTable:
        st.table(get_dataframe_by_nature)
    else:
        st.caption("##")
        st.caption("### Total de Recursos Empenhados e Liquidados por Natureza de Despesa")
        st_echarts(options=options, height="500px", key=f'{onlyTable}_id_dessa_porra')

