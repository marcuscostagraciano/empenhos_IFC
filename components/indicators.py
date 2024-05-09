import streamlit as st

def indicators():
    st.divider()
    st.write(f"## Indicadores Gerais")
    row = st.columns(3)
    st.divider()

    with row[0]:
        st.write("#### R$ 1.000.000,00")
        st.caption("Total de Empenhos Pagos")

    with row[1]:
        st.write("#### R$ 500.000,00")
        st.caption("Total de Empenhos a Liquidar")

    with row[2]:
        st.write("#### R$ 500.000,00")
        st.caption("Saldo Disponível")