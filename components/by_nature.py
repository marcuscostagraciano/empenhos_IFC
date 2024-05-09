import streamlit as st
import pandas as pd
from utils import get_campus_option, create_simple_chart, create_card_chart

def by_nature():
    st.write('by_nature')
    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")

    with row1[0]:
        create_card_chart(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico')

    with row1[1]:
        create_card_chart(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico')

    with row2[0]:
        create_card_chart(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico')

    with row2[1]:
        create_card_chart(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico')