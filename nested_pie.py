import io
import streamlit as st
import pandas as pd

# import altair as alt
import matplotlib.pyplot as plt

# import numpy as np


def run():
    df = pd.read_csv(
        "./assets/xls/empenhos.csv", encoding="ISO-8859-1", sep=";", decimal=","
    )

    colunas_visiveis = [
        "Natureza Despesa",
        "Natureza Despesa Detalhada",
        "Métrica",
        "Mês",
        "Empenhado",
        "Liquidado",
    ]

    df = df[colunas_visiveis]
    df["Empenhado"] = (
        df["Empenhado"].str.replace(".", "").str.replace(",", ".").astype(float)
    )
    df["Liquidado"] = (
        df["Liquidado"].str.replace(".", "").str.replace(",", ".").astype(float)
    )

    st.write("Dataframe Janeiro")
    df_mes = df.groupby(["Mês", "Natureza Despesa"])[["Empenhado", "Liquidado"]].sum().reset_index()
    x1 = (df_mes[df_mes["Mês"] == "01/2024"])
    x2 = (df_mes[df_mes["Mês"] == "02/2024"])
    # x3 = (df[df["Mês"] == "03/2024"])

    plt.figure(figsize=(29, 20))
    plt.pie(
        x1["Empenhado"],
        labels=x1["Natureza Despesa"],
        startangle=90,
        pctdistance=0.88,
        radius=1.0,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 18, "fontweight":"bold"},
        wedgeprops={'linewidth': 3, 'edgecolor': 'white'}
    )
    plt.pie(
        x2["Empenhado"],
        labels=x2["Natureza Despesa"],
        startangle=90,
        pctdistance=0.85,
        radius=0.75,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 18, "fontweight":"bold"},
        wedgeprops={'linewidth': 3, 'edgecolor': 'white'}
    )
    centre_circle = plt.Circle((0,0), 0.45, fc='white')
    plt.legend(loc='lower right', fontsize=15)
    plt.title("Empenhos IFC", fontsize=50, fontweight="bold", pad=30)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    plt.tight_layout()
    st.pyplot(plt)

if __name__ == "__main__":
    run()
