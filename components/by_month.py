from time import time
from typing import Final

import pandas as pd
import streamlit as st
import plotly.express as px
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

    st.multiselect(
        label="Selecione os meses",
        # Identificador no "st.session_state"
        # Com o 'key="months"', não é necessário atribuir este seletor ao "st.session_state.months"
        key="months",
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

        if len(raw_datas) > 0:
            raw_datas_df = pd.concat(raw_datas)
        else:
            raw_datas_df = []

        st.table(raw_datas_df)
        row2 = st.columns(2, gap="medium")

        INDICE_TIPO: Final[dict[int, str]] = {0: "empenhado", 1: "liquidado"}
        for indice in INDICE_TIPO:
            with row2[indice]:
                cria_grafico(df_manager, INDICE_TIPO[indice])


def cria_grafico(df_manager: DataframeManager, tipo_dado: str) -> None:
    tipo_dado_maiusculo: str = tipo_dado.capitalize()
    st.caption(f"## {tipo_dado_maiusculo}")

    st.caption(f"Empenho {tipo_dado} pela Direção do IFC - Araquari")
    meses = [unformatted_months(month) for month in st.session_state.months]

    raw_datas = df_manager.get_df_month_monetary_values(meses, tipo_dado_maiusculo)
    #chart_options = get_options_month_detail(raw_datas, tipo_dado_maiusculo)
    start_time = time()

    #Não esquece que tem que instalar o plotly
    #pip install plotly==5.23.0
    
    if (tipo_dado == 'empenhado'):
        fig = px.pie(raw_datas, values = 'Empenhado', names = 'Natureza Despesa')
    else:
        fig = px.pie(raw_datas, values = 'Liquidado', names = 'Natureza Despesa')

    event = st.plotly_chart(fig)
    event.selection

    #st_echarts(
    #    chart_options,
    #    height="500px",
    #    key=f"GRAFICO_{tipo_dado}",
    #)
    # st_echarts(
    #     chart_options,
    #     height="500px",
    #     key=f"{st.session_state}df_moth_detail_liquidated",
    # )

    stop_time = time()
    print(
        f"Tempo gasto plotando Gráfico '{tipo_dado_maiusculo}': {stop_time - start_time}\n"
    )
