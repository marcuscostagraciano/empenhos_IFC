import streamlit as st
import pandas as pd
from utils import *

def by_nature(onlyTable=False):
    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")

    with row1[0]:
        create_card(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico', onlyTable=onlyTable)

    with row1[1]:
        create_card(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico', onlyTable=onlyTable)

    with row2[0]:
        create_card(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico', onlyTable=onlyTable)

    with row2[1]:
        create_card(title='Titulo do Grafico', desciption='pequena descrição sobre o grafico', onlyTable=onlyTable)