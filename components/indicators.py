import streamlit as st
from classes.dataframe_manager import DataframeManager

def indicators():
    df_manager = DataframeManager()
    st.caption("### Indicadores Gerais")
    [committed , settled, balance] = df_manager.get_indicators()
    row = st.columns(3)

    with row[0]:
        st.write(f"## **:black[R$ {committed}]**")
        st.caption("*Total de Empenhos a Liquidar*")

    with row[1]:
        st.write(f"## **:black[R$ {settled}]**")
        st.caption("*Total de Empenhos Pagos*")

    with row[2]:
        st.write(f"## **:black[R$ {balance}]**")
        st.caption("*Saldo Disponível*")