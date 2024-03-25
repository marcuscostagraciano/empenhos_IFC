import streamlit as st
import pandas as pd
import altair as alt

def run():
    st.set_page_config(
        page_title="Empenhos IFC Araquari | Empenhos Pagos", 
        page_icon="📃", 
        layout="wide", 
        initial_sidebar_state="expanded", 
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': """
                Este projeto de pesquisa tem como objetivo apresentar dados financeiros sobre o IFC Campus Araquari, no que respeita aos empenhos pagos e à liquidar..
                \\
                \\
                Professor Responsavel: [Fábio Longo de Moura](www.github.com/ldmfabio) 
                \\
                Aluno Responsavel: [Mateus Lopes Albano](www.github.com/mateus-lopes)
                \
                \

            """
        }
    )
    st.markdown(
        """
        ## 📃 Empenhos IFC Araquari | Empenhos Pagos
        #####
        """
    )

    df = pd.read_csv('./assets/csv/pagos.csv', sep=';', decimal=',')
    colunas_visiveis = ['Natureza Despesa', 'Natureza Despesa Detalhada', 'Nome Favorecido', 'Mês', 'Saldo']
    filtered_df = df[colunas_visiveis]

    tab1, tab2 = st.tabs(["Dados", "Gráficos"])

    with tab1:
        st.write(filtered_df)

    with tab2:

        tab3, tab4, tab5 = st.tabs(["Por Mês", "Por Natureza de Despesa", "Por Mês e Natureza de Despesa"])

        with tab3:
            df_grouped = filtered_df.groupby('Mês').sum().reset_index()

            chart = alt.Chart(df_grouped).mark_bar().encode(
                x='Mês',
                y='Saldo',
                color='Mês'
            ).properties(
                width=800,
                height=400
            )

            st.altair_chart(chart, use_container_width=True)


        with tab4:
            chart1 = alt.Chart(filtered_df).mark_bar().encode(
                x=alt.X('Mês', axis=alt.Axis(title='Mês')),
                y=alt.Y('sum(Saldo)', axis=alt.Axis(title='Saldo')),
                color='Natureza Despesa',
                tooltip=['Mês', 'Natureza Despesa', alt.Tooltip('sum(Saldo)', title='Saldo')]
            ).properties(
                width=800,
                height=400
            )

            st.altair_chart(chart1, use_container_width=True)

        with tab5:
            def filtrar_dados(filtered_df, mes, natureza):
                if mes == 'Todos' and natureza == 'Todas':
                    return filtered_df
                elif mes == 'Todos':
                    return filtered_df[filtered_df['Natureza Despesa'] == natureza]
                elif natureza == 'Todas':
                    return filtered_df[filtered_df['Mês'] == mes]
                else:
                    return filtered_df[(filtered_df['Mês'] == mes) & (filtered_df['Natureza Despesa'] == natureza)]
                
            meses_unicos = ['Todos'] + filtered_df['Mês'].unique().tolist()
            naturezas_unicas = ['Todas'] + filtered_df['Natureza Despesa'].unique().tolist()

            mes_selecionado = st.selectbox('Selecione o mês', meses_unicos)
            natureza_selecionada = st.selectbox('Selecione a natureza de despesa', naturezas_unicas)

            df_filtrado = filtrar_dados(filtered_df, mes_selecionado, natureza_selecionada)

            df_grouped = df_filtrado.groupby(['Mês', 'Natureza Despesa']).sum().reset_index()

            chart2 = alt.Chart(df_grouped).mark_bar().encode(
                x='Mês',
                y='Saldo',
                color='Natureza Despesa',
                tooltip=['Mês', 'Natureza Despesa', alt.Tooltip('Saldo', title='Saldo')]
            ).properties(
                width=800,
                height=400
            ).interactive()

            st.altair_chart(chart2, use_container_width=True)

   

if __name__ == "__main__":
    run()