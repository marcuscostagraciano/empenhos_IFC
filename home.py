import csv
from time import perf_counter

import streamlit as st

from components.indicators import indicators
from components.main_chart import main_chart
from components.nature_all import nature_all
from components.select_if import select_if
from components.tabs_childrens import tabs_childrens


def save_time_spent_to_csv(
    select: float,
    indicators: float,
    main_charts: float,
    nature_alls: float,
    tabs_children: float,
) -> None:
    print(f"Tempo gasto com 'select_if()': {select}s")
    print(f"Tempo gasto com 'indicators()': {indicators}s")
    print(f"Tempo gasto com 'main_chart()': {main_charts}s")
    print(f"Tempo gasto com 'nature_all()': {nature_alls}s")
    print(f"Tempo gasto com 'tabs_childrens()': {tabs_children}s\n")

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
                "select_if": select,
                "indicators": indicators,
                "main_chart": main_charts,
                "nature_all": nature_alls,
                "tabs_childrens": tabs_children,
            }
        )
        print("Dados salvos no CSV!")


def main():
    st.title("Acompanhamento da execução orçamentária do :green[IFC - Campus Araquari]")
    st.caption(":blue[Version 1.0.5]")

    t1 = perf_counter()
    select_if()
    tempo_select_if = perf_counter() - t1

    t1 = perf_counter()
    indicators()
    tempo_indicators = perf_counter() - t1

    t1 = perf_counter()
    main_chart()
    tempo_main_chart = perf_counter() - t1

    t1 = perf_counter()
    nature_all()
    tempo_nature_all = perf_counter() - t1

    t1 = perf_counter()
    tabs_childrens()
    tempo_tabs_childrens = perf_counter() - t1

    save_time_spent_to_csv(
        tempo_select_if,
        tempo_indicators,
        tempo_main_chart,
        tempo_nature_all,
        tempo_tabs_childrens,
    )

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


if __name__ == "__main__":
    st.set_page_config(
        page_title="Acompanhamento da execução orçamentária do IFC - Campus Araquari",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    main()
