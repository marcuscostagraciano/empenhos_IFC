import streamlit as st
from components.turn_dataframes import turn_dataframes
from components.turn_graphs import turn_graphs

def tabs_container():
    tab1, tab2 = st.tabs(['Dados em forma de Gráficos', 'Dados em forma de Tabela'])

    with tab1:
        turn_graphs()
    with tab2:
        turn_dataframes()
