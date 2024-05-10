import streamlit as st

def indicators():
    st.caption("### Indicadores Gerais")
    empenho, liquidado = [100000, 25000]
    row = st.columns(3)

    with row[0]:
        st.write(f"## **:black[R$ {empenho},00]**")
        st.caption("*Total de Empenhos Pagos*")

    with row[1]:
        st.write(f"## **:black[R$ {liquidado},00]**")
        st.caption("*Total de Empenhos a Liquidar*")

    with row[2]:
        st.write(f"## **:black[R$ {empenho - liquidado},00]**")
        st.caption("*Saldo Disponível*")