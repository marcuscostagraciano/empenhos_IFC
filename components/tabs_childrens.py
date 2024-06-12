import streamlit as st
from components.by_month import by_month
from components.by_month2 import by_month2
from components.by_nature_details import by_nature_details

def tabs_childrens(onlyTable=False):
    tab1, tab2 = st.tabs(['Buscar Por Mês', 'Buscar por Natureza'])

    with tab1:
        by_month()
        # by_month2(onlyTable=onlyTable)
    with tab2:
        by_nature_details(onlyTable=onlyTable)
    