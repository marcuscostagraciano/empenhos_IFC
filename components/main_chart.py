import streamlit as st
from utils import create_simple_chart
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from streamlit_echarts import st_echarts, st_pyecharts
from classes.dataframe_manager import DataframeManager

def main_chart(onlyTable=False):
    st.caption("#")
    st.caption("### Empenhado x Liquidado (Mês a Mês)")
    row = st.columns((8,4))
    df_manager = DataframeManager()
    [options, df] = df_manager.get_options_main()

    
    df_master = st.session_state.df_master
    committed = df_master['Empenhado'].sum()
    settled = df_master['Liquidado'].sum()

    if onlyTable:
        st.table(df)
    else:
        options = {
            **options,
            "grid": {"left": "1%", "right": "25%", "bottom": "3%", "containLabel": True},
            "series": [
                *options['series'],
                {
                    "name": "Soma Total (R$)",
                    "type": "pie",
                    "radius": ['30%', '60%'],
                    "center": ["90%", "50%"],
                    "itemStyle": {
                        "borderRadius": 10,
                        "borderColor": "#fff",
                        "borderWidth": 10,
                    },
                    "data": [
                        {"value":  settled, "name": "Liquidado"},
                        {"value":committed , "name": "Empenhado"},
                    ],
                    "emphasis": {
                        "label": {
                            "show": True,
                            "fontSize": 18,
                            "fontWeight": 'bold'
                        }
                    },
                    "label": {
                        "show": False,
                        "position": 'center',
                        "formatter": "{d}%"
                    }
                }
            ],
        }
        st_echarts(options=options, height="400px")
        # with row[0]:
        
        # with row[1]:
        #     options = {
        #         "title": { },
        #         "tooltip": {"trigger": "item"},
        #         "legend": {"right": "right",},
        #         "series": [
        #             {
        #                 "name": "Soma Total (R$)",
        #                 "type": "pie",
        #                 "radius": '60%',
        #                 "data": [
        #                     {"value": committed, "name": "Empenhado"},
        #                     {"value": settled, "name": "Liquidado"},
        #                 ],
        #             }
        #         ],
        #     }
        #     st_echarts(
        #         options=options, height="400px",
        #     )