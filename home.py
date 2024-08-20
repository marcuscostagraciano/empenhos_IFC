import csv
from time import perf_counter

import streamlit as st

from components.indicators import indicators
from components.main_chart import main_chart
from components.nature_all import nature_all
from components.select_if import select_if
from components.tabs_childrens import tabs_childrens


def main():
    st.title("Acompanhamento da execução orçamentária do :green[IFC - Campus Araquari]")
    st.caption(":blue[Version 1.0.5]")

    t1 = perf_counter()
    select_if()
    tempo_select_if = perf_counter() - t1
    print(f"Tempo gasto com 'select_if()': {tempo_select_if}s")

    t1 = perf_counter()
    indicators()
    tempo_indicators = perf_counter() - t1
    print(f"Tempo gasto com 'indicators()': {tempo_indicators}s")

    t1 = perf_counter()
    main_chart()
    tempo_main_chart = perf_counter() - t1
    print(f"Tempo gasto com 'main_chart()': {tempo_main_chart}s")

    t1 = perf_counter()
    nature_all()
    tempo_nature_all = perf_counter() - t1
    print(f"Tempo gasto com 'nature_all()': {tempo_nature_all}s")

    t1 = perf_counter()
    tabs_childrens()
    tempo_tabs_childrens = perf_counter() - t1
    print(f"Tempo gasto com 'tabs_childrens()': {tempo_tabs_childrens}s\n")

    # REMOÇÃO (TALVEZ) TEMPORÁRIA
    # st.divider()
    # if st.button(
    #     "Ver Análise Avançada (beta)",
    #     help="Essa pagina é uma versão beta, clique aqui para ver mais detalhadamente os dados coletados.",
    #     use_container_width=True,
    #     type="primary",
    # ):
    #     st.switch_page("pages/home_(beta).py")
    # if st.button(
    #     "Ver Dados Brutos",
    #     help="Clique aqui para ver os dados brutos.",
    #     use_container_width=True,
    # ):
    #     st.switch_page("pages/dados_brutos.py")

    with open("tempos_carregamento.csv", "a", newline="\n") as arquivo_tempos:
        metodos = [
            "select_if",
            "indicators",
            "main_chart",
            "nature_all",
            "tabs_childrens",
        ]
        writer = csv.DictWriter(arquivo_tempos, fieldnames=metodos, delimiter=",")
        writer.writerow(
            {
                "select_if": tempo_select_if,
                "indicators": tempo_indicators,
                "main_chart": tempo_main_chart,
                "nature_all": tempo_nature_all,
                "tabs_childrens": tempo_tabs_childrens,
            }
        )
        print("Dados salvos no CSV!")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Acompanhamento da execução orçamentária do IFC - Campus Araquari",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    main()
