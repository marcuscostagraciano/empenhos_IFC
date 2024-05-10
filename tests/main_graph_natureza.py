import altair as alt
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

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

# return
# df
# df_mes
# df_mes_natureza

get_df_dashboard_empenhado = df_mes_natureza[['Mês', 'Natureza Despesa', 'Empenhado']]
st.write(get_df_dashboard_empenhado)

pivoted = pd.pivot_table(get_df_dashboard_empenhado, values='Empenhado', index='Natureza Despesa', columns='Mês')
pivoted.columns = ['01/2024', '02/2024', '03/2024', '04/2024']
# pivoted.columns = pd.to_datetime(pivoted.columns).astype(int) / 10**9
pivoted = pivoted.fillna(0) 

st.table(pivoted)

pivoted_reset = pivoted.reset_index()
st.write(pivoted_reset.iloc[3].tolist())
st.write(pivoted_reset.columns.tolist())


st.session_state.a1 = st.selectbox(
    f"Selecione o Mês",
    ["01", "02", "03", "04"]
)

option = {
    "legend": {},
    "tooltip": {"trigger": "axis", "showContent": False},
    "dataset": {
        "source": [
            # (df_mes['Mês'].tolist() + ['Mês'])[::-1], mes pelo df_mes
            pivoted_reset.columns.tolist(),
            pivoted_reset.iloc[0].tolist(),
            pivoted_reset.iloc[1].tolist(),
            pivoted_reset.iloc[2].tolist(),
            pivoted_reset.iloc[3].tolist(),
        ]
    },
    "xAxis": {"type": "category"},
    "yAxis": {"gridIndex": 0},
    "grid": {"top": "55%"},
    "series": [
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "line",
            "smooth": True,
            "seriesLayoutBy": "row",
            "emphasis": {"focus": "series"},
        },
        {
            "type": "pie",
            "id": "pie",
            "radius": "30%",
            "center": ["50%", "25%"],
            "emphasis": {"focus": "data"},
            "label": {"formatter": "{b}: {@04/2024} ({d}%)"},
            "encode": {"itemName": "Natureza Despesa", "value": f"{st.session_state.a1}/2024", "tooltip": "04/2024"},
        },
    ],
}
st_echarts(option, height="500px", key="echarts")

st.write(st.session_state.a1)