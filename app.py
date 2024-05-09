from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from utils import *
from components.indicators import indicators
from components.tabs_child_graph import tabs_child_graph

def main():    
    st.info("__NOTA__: DURANTES OS TESTE PODEM HAVER ERROS DE ID(**DuplicateWidgetID**)")
    st.write(f"# Análise de Empenhos Pagos e a Liquidar dos Institutos Federais")
    st.divider()
    st.write(f"## Seleção do Campus")
    st.caption(
        """
        Este projeto de pesquisa visa analisar os dados financeiros do IFC Campus Araquari, concentrando-se nos empenhos pagos e a liquidar. O objetivo é compreender os padrões de gastos, identificar áreas prioritárias e avaliar a eficiência no uso dos recursos financeiros para auxiliar na gestão e no planejamento orçamentário do campus.
        """
    )
    layout_cols = st.columns((1, 1, 2))
    indicators()

    with layout_cols[0]:
        option1 = get_campus_option()

    with layout_cols[1]:
        option2 = get_campus_option()

    st.write(f"## Empenhado x Liquidado (Mês a Mês)")
    st.caption("pequena descrição sobre o grafico")
    st.altair_chart(create_simple_chart(), use_container_width=True)

    tabs_child_graph()

if __name__ == "__main__":
    st.set_page_config(
        page_title="Análise de Empenhos Pagos e a Liquidar", 
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )
    main()
