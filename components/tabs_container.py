import streamlit as st
from components.main_graph import main_graph
from components.main_table import main_table
from components.tabs_childrens import tabs_childrens
from components.indicators import indicators

def tabs_container():
    tab1, tab2 = st.tabs(['Dados em forma de Gráficos', 'Dados em forma de Tabela'])

    with tab1:
        indicators()
        main_graph()
        tabs_childrens()

    with tab2:
        indicators()
        main_table()
        tabs_childrens(onlyTable=True)
