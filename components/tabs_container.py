import streamlit as st
from components.main_chart import main_chart
from components.tabs_childrens import tabs_childrens
from components.indicators import indicators

def tabs_container():
    tab1, tab2 = st.tabs(['Dados em forma de Gráficos', 'Dados em forma de Tabela'])

    with tab1:
        indicators()
        main_chart()
        tabs_childrens()

    with tab2:
        indicators()
        main_chart(onlyTable=True)
        tabs_childrens(onlyTable=True)
