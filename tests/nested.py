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

    # Aqui começa o código do nested_pie.py
    st.write("Dataframe Janeiro")
    df_mes = (
        df.groupby(["Mês", "Natureza Despesa"])[["Empenhado", "Liquidado"]]
        .sum()
        .reset_index()
    )
    df_mes["Pendente"] = df_mes["Empenhado"] - df_mes["Liquidado"]

    x1 = df_mes[df_mes["Mês"] == "01/2024"]
    x2 = df_mes[df_mes["Mês"] == "01/2024"]

    st.write(x1)
    plt.figure(figsize=(29, 20))
    plt.pie(
        x1["Empenhado"],
        labels=x1["Natureza Despesa"],
        startangle=90,
        pctdistance=0.88,
        radius=1.0,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 18, "fontweight": "bold"},
        wedgeprops={"linewidth": 3, "edgecolor": "white"},
    )
    plt.legend(loc="lower right", fontsize=15)
    plt.title("Empenhos IFC", fontsize=50, fontweight="bold", pad=30)
    # fig = plt.gcf()
    plt.axis("equal")

    # Aqui criamos um novo dataframe, copiando a estrutura do x2, mas duplicando este dataframe para separar a coluna Pendente e a coluna Liquidado
    x2_pendente = x1[["Mês", "Natureza Despesa", "Pendente"]].copy()
    x2_liquidado = x1[["Mês", "Natureza Despesa", "Liquidado"]].copy()
    x2_pendente["Tipo"] = "Pendente"
    x2_liquidado["Tipo"] = "Liquidado"

    # Aqui concatenamos os dois dataframes, x3_pendente e x3_liquidado, para formar um novo dataframe com as colunas Mês, Natureza da Despesa, Valor e Tipo
    x2 = pd.concat([x2_pendente, x2_liquidado], ignore_index=True)
    x2.loc[x2["Tipo"] == "Liquidado", "Valor"] = x2["Liquidado"]
    x2.loc[x2["Tipo"] == "Pendente", "Valor"] = x2["Pendente"]
    colunas_a_remover = ["Pendente", "Liquidado"]
    x2 = x2.drop(columns=colunas_a_remover)
    st.write(x2.sort_values(by="Natureza Despesa"))
    # Foi finalizada a criação do dataframe, colocando os dados de Pendente e Liquidado em uma única coluna chamada Valor, removendo essas duas colunas

    plt.clf()
    plt.figure(figsize=(29, 20))
    plt.pie(
        x1["Empenhado"],
        labels=x1["Natureza Despesa"],
        startangle=90,
        pctdistance=0.88,
        radius=1.0,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 18, "fontweight": "bold"},
        wedgeprops={"linewidth": 3, "edgecolor": "white"},
    )
    plt.legend(loc="lower right", fontsize=15)
    plt.pie(
        x2["Valor"],
        labels=x2["Tipo"],
        startangle=90,
        pctdistance=0.85,
        radius=0.75,
        autopct="%1.1f%%",
        labeldistance=1.1,
        textprops={"fontsize": 12, "fontweight": "bold"},
        wedgeprops={"linewidth": 3, "edgecolor": "white"},
    )

    centre_circle = plt.Circle((0, 0), 0.15, fc="white")
    plt.title("Empenhos IFC", fontsize=50, fontweight="bold", pad=30)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis("equal")
    plt.tight_layout()
    st.pyplot(plt)

if __name__ == "__main__":
    run()
