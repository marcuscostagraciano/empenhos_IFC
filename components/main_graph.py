import streamlit as st
from utils import create_simple_chart
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from streamlit_echarts import st_echarts

def main_graph():

    st.write(f"## Empenhado x Liquidado (Mês a Mês)")
    st.caption("pequena descrição sobre o grafico")

    df = pd.read_csv("./assets/xls/empenhos.csv", encoding='ISO-8859-1', sep=";", decimal=",")

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
    st.write(df_mes)
    df_mes["Empenhado Formatado"] = df_mes["Empenhado"].map("R$ {:,.2f}".format)
    df_mes["Liquidado Formatado"] = df_mes["Liquidado"].map("R$ {:,.2f}".format)

    df_mes_natureza = df.groupby(['Mês'])[['Empenhado', 'Liquidado']].sum().reset_index()
    df_mes_natureza["Empenhado Formatado"] = df_mes_natureza["Empenhado"].map("R$ {:,.2f}".format)
    df_mes_natureza["Liquidado Formatado"] = df_mes_natureza["Liquidado"].map("R$ {:,.2f}".format)

    plt.figure(figsize=(10, 6))

    plt.plot(df_mes['Mês'], df_mes['Empenhado'], label='Empenhado', marker='x', color='red')
    plt.plot(df_mes['Mês'], df_mes['Liquidado'], label='Liquidado', marker='o', color='blue')
    plt.xlabel('Mês')
    plt.ylabel('Valor')
    plt.title('Empenhado x Liquidado por Mês')
    plt.legend()
    plt.xticks(df_mes['Mês'])
    valores_y = pd.concat([df_mes['Empenhado'], df_mes['Liquidado']])
    plt.yticks(valores_y)
    st.pyplot(plt)

    plt.clf();
    st.write("Dataframe Janeiro")
    df_mes = (
        df.groupby("Mês")[["Empenhado", "Liquidado"]]
        .sum()
        .reset_index()
    )
    df_mes["Empenhado"] = df_mes["Empenhado"].astype("int")
    df_mes["Liquidado"] = df_mes["Liquidado"].astype("int")
    st.write(df_mes)

    # plt.figure(figsize=(29, 20))
    # plt.pie(
    #     df_mes["Empenhado"],
    #     labels=df_mes["Natureza Despesa"],
    #     startangle=90,
    #     pctdistance=0.85,
    #     autopct="%1.1f%%",
    #     labeldistance=1.1,
    #     textprops={"fontsize": 18, "fontweight": "bold"},
    #     wedgeprops={"linewidth": 3, "edgecolor": "white"},
    # )
    # plt.legend(loc="lower right", fontsize=15)
    # plt.title("Empenhos IFC", fontsize=50, fontweight="bold", pad=30)
    # plt.axis("equal")
    # st.pyplot(plt)

    options = {
        "title": {"text": "Empenhado x Liquidado (Mês a Mês)"},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["Liquidado", "Teste", "Empenhado"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": df_mes['Mês'].tolist(),
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "name": "Liquidado",
                "type": "line",
                "stack": "Total",
                "data": df_mes['Liquidado'].tolist(),
            },
            {
                "name": "Liquidado",
                "type": "line",
                "stack": "Total",
                "data": df_mes['Liquidado'].tolist(),
            },
            {
                "name": "Empenhado",
                "type": "line",
                "stack": "Total",
                "data": df_mes['Empenhado'].tolist(),
                # "data": [200, 300000, 0, 1000000]
            },
        ],
    }
    st_echarts(options=options, height="400px")
