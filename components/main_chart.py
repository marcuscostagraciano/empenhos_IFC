import streamlit as st
from utils import create_simple_chart
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from streamlit_echarts import st_echarts, st_pyecharts
from classes.dataframe_manager import DataframeManager

def main_chart(onlyTable=False):
    row = st.columns((8,4))
    df_manager = DataframeManager()
    [options, df] = df_manager.get_options_main()

    
    df_master = st.session_state.df_master
    settled = df_master['Liquidado'].sum()
    committed = df_master['Empenhado'].sum() - settled

    if onlyTable:
        st.table(df)
    else:
        st.caption("#")
        st.caption("### Total de Recursos Empenhados e Liquidados")
        options = {
            **options,
            "grid": {"left": "1%", "right": "25%", "bottom": "3%", "containLabel": True},
            "series": [
                *options['series'],
                {
                    "name": "Soma Total (R$)",
                    "type": "pie",
                    "radius": '60%',
                    "center": ["90%", "50%"],
                    "data": [
                        {"value":  settled, "name": "Liquidado"},
                        {"value":committed , "name": "Empenhado"},
                    ],
                    "emphasis": {
                        "label": {
                            "show": True,
                        }
                    },
                    "label": {
                        "show": False,
                        "formatter": "{d}%",
                        "fontSize": 15,
                        "fontWeight": "bold",
                        "position": 'center'
                    }
                }
            ],
        }
        st_echarts(options=options, height="400px")