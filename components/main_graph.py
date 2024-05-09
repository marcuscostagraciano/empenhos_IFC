import streamlit as st
from utils import create_simple_chart

def main_graph():
    st.write(f"## Empenhado x Liquidado (Mês a Mês)")
    st.caption("pequena descrição sobre o grafico")
    st.altair_chart(create_simple_chart(), use_container_width=True)