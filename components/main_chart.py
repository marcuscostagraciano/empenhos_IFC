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

    df_manager = DataframeManager()
    [options, df] = df_manager.get_options_main()

    if onlyTable:
        st.table(df)
    else:
        st_echarts(options=options, height="400px")
