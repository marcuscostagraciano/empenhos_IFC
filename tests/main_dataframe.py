import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

df = pd.read_csv("../assets/xls/empenhos.csv", encoding='ISO-8859-1', sep=";", decimal=",")

colunas_visiveis = [
    'Natureza Despesa',
    'Natureza Despesa Detalhada',
    'Métrica',
    'Mês',
    'Empenhado',
    'Liquidado',
]

df = df[colunas_visiveis]
df['Empenhado'] = df['Empenhado'].str.replace('.', '').str.replace(',', '.').astype(float)
df['Liquidado'] = df['Liquidado'].str.replace('.', '').str.replace(',', '.').astype(float)
df['Empenhado Formatado'] = df['Empenhado'].map('R$ {:,.2f}'.format)
df['Liquidado Formatado'] = df['Liquidado'].map('R$ {:,.2f}'.format)

df_mes = df.groupby(['Mês'])[['Empenhado', 'Liquidado']].sum().reset_index()
df_mes["Empenhado Formatado"] = df_mes["Empenhado"].map("R$ {:,.2f}".format)
df_mes["Liquidado Formatado"] = df_mes["Liquidado"].map("R$ {:,.2f}".format)

df_mes_natureza = df.groupby(['Mês', 'Natureza Despesa'])[['Empenhado', 'Liquidado']].sum().reset_index()
df_mes_natureza["Empenhado Formatado"] = df_mes_natureza["Empenhado"].map("R$ {:,.2f}".format)
df_mes_natureza["Liquidado Formatado"] = df_mes_natureza["Liquidado"].map("R$ {:,.2f}".format)

st.write('Dataframe Geral')
st.write(df)

st.write('Dataframe Agrupado por Mês')
st.write(df_mes)

st.write('Dataframe Agrupado por Mês e Natureza de Despesa')
st.write(df_mes_natureza)