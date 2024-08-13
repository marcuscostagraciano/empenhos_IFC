from time import time

import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

from classes.dataframe_manager import DataframeManager
from utils import *


def by_month(advanced_report=False):
    df_manager = DataframeManager()

    start_time = time()
    months = [
        formatted_months(month) for month in st.session_state.df_master["Mês"].unique()
    ]
    stop_time = time()
    print(f"Tempo gasto with MONTHS: {stop_time - start_time}")

    st.session_state.months = st.multiselect(
        label="Selecione os meses",
        key=f"get_month_{advanced_report}",
        options=months,
        placeholder="Selecione o mês",
        default=months[-1],
    )

    if st.session_state.months == []:
        st.info("Selecione um mês", icon="ℹ️")
    else:
        raw_datas = []
        unformatted_months_list = [
            unformatted_months(month) for month in st.session_state.months
        ]
        df = df_manager.get_df_month_values(unformatted_months_list)
        raw_datas.append(df)
        # print(raw_datas)

        if len(raw_datas) > 0:
            raw_datas_df = pd.concat(raw_datas)
            print(f"{raw_datas_df = }")
        else:
            raw_datas_df = []

        st.table(raw_datas_df)
        row2 = st.columns(2, gap="medium")

        start_time = time()
        with row2[0]:
            st.caption("## Empenhado")
            st.caption("Recurso empenhado pela Direção do IFC - Araquari")
            meses = [unformatted_months(month) for month in st.session_state.months]
            raw_datas = df_manager.get_df_month_monetary_values(meses, "Empenhado")
            chart_options = get_options_month_detail(raw_datas, "Empenhado")
            start_time = time()
            st_echarts(
                chart_options,
                height="500px",
                key=f"{st.session_state}df_moth_detail_comitted",
            )
            stop_time = time()
            print(f"Tempo gasto plotando Gráfico 'empenhado': {stop_time - start_time}")

        stop_time = time()
        print(f"Tempo gasto Gráfico 'empenhado': {stop_time - start_time}")

        start_time = time()
        with row2[1]:
            st.caption("## Liquidado")
            st.caption("Empenho liquidado pela Direção do IFC - Araquari")
            meses = [unformatted_months(month) for month in st.session_state.months]
            raw_datas = df_manager.get_df_month_monetary_values(meses, "Liquidado")
            chart_options = get_options_month_detail(raw_datas, "Liquidado")
            start_time = time()
            st_echarts(
                chart_options,
                height="500px",
                key=f"{st.session_state}df_moth_detail_liquidated",
            )
            stop_time = time()
            print(f"Tempo gasto plotando Gráfico 'liquidado': {stop_time - start_time}")

        stop_time = time()
        print(f"Tempo gasto Gráfico 'liquidado': {stop_time - start_time}")
