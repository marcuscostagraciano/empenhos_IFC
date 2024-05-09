import streamlit as st
import pandas as pd
# import altair as alt
import matplotlib.pyplot as plt
# import numpy as np

def run():
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
    df_mes["Empenhado Formatado"] = df_mes["Empenhado"].map("R$ {:,.2f}".format)
    df_mes["Liquidado Formatado"] = df_mes["Liquidado"].map("R$ {:,.2f}".format)

    df_mes_natureza = df.groupby(['Mês', 'Natureza Despesa'])[['Empenhado', 'Liquidado']].sum().reset_index()
    df_mes_natureza["Empenhado Formatado"] = df_mes_natureza["Empenhado"].map("R$ {:,.2f}".format)
    df_mes_natureza["Liquidado Formatado"] = df_mes_natureza["Liquidado"].map("R$ {:,.2f}".format)

    # df_mes_natureza_detalhada = df.groupby(['Mês', 'Natureza Despesa Detalhada']).sum().reset_index()

    st.write('Dataframe Geral')
    st.write(df)

    st.write('Dataframe Agrupado por Mês')
    st.write(df_mes)

    st.write('Dataframe Agrupado por Mês e Natureza de Despesa')
    st.write(df_mes_natureza)

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
    # min_y = min(df_mes[['Empenhado', 'Liquidado']].min())
    # max_y = max(df_mes[['Empenhado', 'Liquidado']].max())
    # plt.ylim(min_y, max_y)
    st.pyplot(plt)

    plt.clf();
    st.write("Dataframe Janeiro")
    df_mes = (
        df.groupby("Natureza Despesa")[["Empenhado", "Liquidado"]]
        .sum()
        .reset_index()
    )
    st.write(df_mes)
    # x1 = df_mes[df_mes["Mês"] == "01/2024"]
    # x2 = (df[df["Mês"] == "02/2024"])
    # x3 = (df[df["Mês"] == "03/2024"])

    plt.figure(figsize=(29, 20))
    plt.pie(
        df_mes["Empenhado"],
        labels=df_mes["Natureza Despesa"],
        startangle=90,
        pctdistance=0.85,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 18, "fontweight": "bold"},
        wedgeprops={"linewidth": 3, "edgecolor": "white"},
    )
    plt.legend(loc="lower right", fontsize=15)
    plt.title("Empenhos IFC", fontsize=50, fontweight="bold", pad=30)
    plt.axis("equal")
    st.pyplot(plt)


if __name__ == "__main__":
    run()