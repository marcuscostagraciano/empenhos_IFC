import streamlit as st
from utils import get_campus_option

def select_if():
    st.write(
        """
        Este projeto de pesquisa visa analisar os dados financeiros do IFC Campus Araquari, concentrando-se nos empenhos pagos e a liquidar. O objetivo é compreender os padrões de gastos, identificar áreas prioritárias e avaliar a eficiência no uso dos recursos financeiros para auxiliar na gestão e no planejamento orçamentário do campus.
        """
    )

    layout_cols = st.columns((1, 1, 2))

    with layout_cols[0]:
        state_option = st.selectbox(
            f"Selecione o Estado",
            ["SC", "RS", "PR", "..."],
        )

    with layout_cols[1]:
        campus_option = st.selectbox(
            f"Selecione o Campus",
            ["Araquari", "Camboriú", "Sombrio", "Videira", "..."],
        )
    