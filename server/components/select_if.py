import streamlit as st

def select_if(advanced_report=False):
    if advanced_report:
        st.write(
            """
            Este projeto de pesquisa visa analisar os dados financeiros do IFC Campus Araquari, concentrando-se nos empenhos pagos e a liquidar. O objetivo é compreender os padrões de gastos, identificar áreas prioritárias e avaliar a eficiência no uso dos recursos financeiros para auxiliar na gestão e no planejamento orçamentário do campus.
            """
        )
    else:
        st.write(
            """
            Este projeto de pesquisa visa analisar os dados financeiros dos Institutos Federais, concentrando-se nos empenhos pagos e a liquidar. O objetivo é compreender os padrões de gastos, identificar áreas prioritárias e avaliar a eficiência no uso dos recursos financeiros para auxiliar na gestão e no planejamento orçamentário do campus.
            """
        )
        layout_cols = st.columns((1, 1, 2))

        with layout_cols[0]:
            state_option = st.selectbox(
                f"Selecione o Estado",
                ["SC", "..."],
            )

        with layout_cols[1]:
            campus_option = st.selectbox(
                f"Selecione o Campus",
                ["Araquari", "..."],
            )
    
    st.markdown('''<div style="color: #888; font-size: .8em;position: absolute; right: 0; bottom: -2em;">
        Professor Responsavel: <a href="www.github.com/ldmfabio" style="padding-right: 1em">Fábio Longo de Moura</a> 
        Aluno Responsavel: <a href="www.github.com/mateus-lopes">Mateus Lopes Albano</a>
    </div>''', unsafe_allow_html=True)