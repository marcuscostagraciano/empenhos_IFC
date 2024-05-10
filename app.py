from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from utils import *
from components.indicators import indicators
from components.select_if import select_if
from components.tabs_container import tabs_container

def main():    
    st.warning("__AVISO__: DURANTES OS TESTE PODEM HAVER ERROS DE ID(**DuplicateWidgetID**)")
    st.write(f"# Análise de Empenhos Pagos e a Liquidar dos :green[Institutos Federais]")
    select_if()
    indicators()
    tabs_container()

if __name__ == "__main__":
    st.set_page_config(
        page_title="IF - Análise de Empenhos Pagos e a Liquidar", 
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
    )
    main()
