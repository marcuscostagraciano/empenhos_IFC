from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from utils import *

def main():    
    st.write(f"# Análise de Empenhos Pagos e a Liquidar")
    st.caption(
        """
        Este projeto de pesquisa visa analisar os dados financeiros do IFC Campus Araquari, concentrando-se nos empenhos pagos e a liquidar. O objetivo é compreender os padrões de gastos, identificar áreas prioritárias e avaliar a eficiência no uso dos recursos financeiros para auxiliar na gestão e no planejamento orçamentário do campus.
        """
    )
    layout_cols = st.columns((1, 1, 2))

    with layout_cols[0]:
        option1 = get_campus_option("")

    with layout_cols[1]:
        option2 = get_campus_option(0)

    st.divider()

    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")
    
    st.divider()

    with row1[0]:
        container_col = st.container()
        container_col.write("### Titulo do Grafico")
        container_col.caption("pequena descrição sobre o grafico")
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            option1 = get_campus_option(1)

        with layout_cols[1]:
            option2 = get_campus_option(2)
        st.altair_chart(create_simple_chart(), use_container_width=True)

    with row1[1]:
        container_col = st.container()
        container_col.write("### Titulo do Grafico")
        container_col.caption("pequena descrição sobre o grafico")
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            option1 = get_campus_option(3)

        with layout_cols[1]:
            option2 = get_campus_option(4)
        st.altair_chart(create_simple_chart(), use_container_width=True)

    with row2[0]:
        container_col = st.container()
        container_col.write("### Titulo do Grafico")
        container_col.caption("pequena descrição sobre o grafico")
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            option1 = get_campus_option(5)

        with layout_cols[1]:
            option2 = get_campus_option(6)
        st.altair_chart(create_simple_chart(), use_container_width=True)

    with row2[1]:
        container_col = st.container()
        container_col.write("### Titulo do Grafico")
        container_col.caption("pequena descrição sobre o grafico")
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            option1 = get_campus_option(7)

        with layout_cols[1]:
            option2 = get_campus_option(8)
        st.altair_chart(create_simple_chart(), use_container_width=True)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Análise de Empenhos Pagos e a Liquidar", 
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )
    main()
