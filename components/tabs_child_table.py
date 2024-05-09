import streamlit as st
from utils import *
from components.by_month import by_month
from components.by_nature import by_nature
from components.by_nature_details import by_nature_details

def tabs_child_table():
    tab1, tab2, tab3 = st.tabs(['Por Mês', 'Por Natureza', 'Por Natureza Detalhada'])

    with tab1:
        by_month()
    with tab2:
        by_nature()
    with tab3:
        by_nature_details()
