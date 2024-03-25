import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def run():
    st.set_page_config(
        page_title="IFC Araquari | Empenhos 2024", 
        page_icon="📉", 
        layout="wide", 
        initial_sidebar_state="expanded", 
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': """
                Este projeto de pesquisa tem como objetivo apresentar dados financeiros sobre o IFC Campus Araquari, no que respeita aos empenhos pagos e à liquidar.
                  
                \\
                \\
                Professor Responsavel: [Fábio Longo de Moura](www.github.com/ldmfabio) 
                \\
                Aluno Responsavel: [Mateus Lopes Albano](www.github.com/mateus-lopes)
                \
                \

            """
        }
    )  

    with st.sidebar:
        pass
    
    st.markdown(
        """
        ## 📉 IFC Araquari | Empenhos 2024  
        #####
        ##### Descrição do Projeto:
        Este projeto de pesquisa tem como objetivo apresentar dados financeiros sobre o IFC Campus Araquari, no que respeita aos empenhos pagos e à liquidar.
        """
    )
        
    st.write(
        """
        ##### 
        \
        """
    )
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.image('./assets/img/logo-ifc.png', width=300)

    with col2:
        st.image('./assets/img/logo-fabrica.png')
    st.write("*Versão 1.0.3*")


if __name__ == "__main__":
    run()