import streamlit as st
from classes.dataframe_manager import DataframeManager

def indicators():
    df_manager = DataframeManager()
    st.divider()
    st.caption("### Indicadores Gerais")
    [committed , settled, balance] = df_manager.get_indicators()
    row = st.columns(3)

    with row[0]:
        st.markdown(f"<p style='font-size: 2.4em; font-weight: 700;'>R$ {committed}</p>", unsafe_allow_html=True)
        st.caption("*Montante Empenhado*")

    with row[1]:
        st.markdown(f"<p style='font-size: 2.4em; font-weight: 700;'>R$ {settled}</p>", unsafe_allow_html=True)
        st.caption("*Montante Liquidado*")

    with row[2]:
        st.markdown(f"<p style='font-size: 2.4em; font-weight: 700; color: red;'>R$ {balance}</p>", unsafe_allow_html=True)
        st.caption("*Montante Pendente de Liquidação*")