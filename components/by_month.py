from time import perf_counter
from typing import Final

import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

from classes.dataframe_manager import DataframeManager
from utils import formatted_months, get_options_month_detail, unformatted_months


def by_month(advanced_report=False):
    df_manager = DataframeManager()

    df_sorted_by_month = st.session_state.df_master.sort_values(by="Mês")
    months = [formatted_months(month) for month in df_sorted_by_month["Mês"].unique()]

    st.multiselect(
        label="Selecione os meses",
        # Identificador no "st.session_state"
        # Com o 'key="months"', não é necessário atribuir este seletor ao "st.session_state.months"
        key="months",
        options=months,
        placeholder="Selecione o mês",
        default=months[0],
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
        columns = st.columns(2, gap="medium")

        GRAPH_TYPES: Final[list[str]] = ["empenhado", "liquidado"]
        for index, graph_type in enumerate(GRAPH_TYPES):
            with columns[index]:
                graph_plot(df_manager, graph_type)


def graph_plot(df_manager: DataframeManager, graph_type: str) -> None:
    capitalized_graph_type: str = graph_type.capitalize()
    st.caption(f"## {capitalized_graph_type}")

    st.caption(f"Empenho {graph_type} pela Direção do IFC - Araquari")
    meses = [unformatted_months(month) for month in st.session_state.months]

    raw_datas = df_manager.get_df_month_monetary_values(meses, capitalized_graph_type)
    chart_options = get_options_month_detail(raw_datas, capitalized_graph_type)

    st_echarts(
        chart_options,
        height="500px",
        key=f"GRAFICO_{graph_type}",
    )
