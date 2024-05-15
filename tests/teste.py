import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados
# data = {
#     'Mês': ['Jan', 'Jan', 'Fev', 'Fev', 'Mar', 'Mar'],
#     'Natureza Despesa Detalhada': ['Alimentação', 'Comida', 'Alimentação', 'Transporte', 'Alimentação', 'Transporte'],
#     'Saldo': [1000, 1500, 1200, 800, 1000, 900]
# }

# Convertendo os dados para um DataFrame
# df = pd.DataFrame(data)
st.write("# Natureza Despesa agrupada por Mês")
dados = pd.read_csv('./assets/csv/pagos.csv', sep=';', decimal=',')

def filtrar_dados(filtered_df, mes):
    if mes == "Todos":
        return filtered_df
    else:
        return filtered_df[
            (filtered_df["Mês"] == mes)
        ]

meses = dados['Mês']
naturezas = dados['Natureza Despesa']
saldos = dados['Saldo']
df = pd.DataFrame({'Mês': meses, 'Natureza Despesa': naturezas, 'Saldo': saldos})

meses_unicos = ["Todos"] + df["Mês"].unique().tolist()
mes_selecionado = st.selectbox("Selecione o mês", meses_unicos)

# Agrupando os dados por mês e natureza da despesa
df = filtrar_dados(df, mes_selecionado)
grouped_df = df.groupby(['Mês', 'Natureza Despesa']).sum().reset_index()

# Criando o gráfico de barras agrupadas
def grouped_bar_chart():
    fig, ax = plt.subplots()

    meses = grouped_df['Mês'].unique()
    largura_barra = 0.35
    indice = np.arange(len(meses))

    # Iterando sobre os meses
    for i, mes in enumerate(meses):
        df_mes = grouped_df[grouped_df['Mês'] == mes]
        # Posicionando as barras para cada categoria ao lado das barras do mesmo mês
        for j, categoria in enumerate(df_mes['Natureza Despesa'].unique()):
            valores = df_mes[df_mes['Natureza Despesa'] == categoria]['Saldo'].values
            ax.bar(indice[i] + largura_barra * j, valores, largura_barra, label=categoria)
            ax.text(indice[i] + largura_barra * j, valores[0] + 50, str(f'{valores[0]:.2f}'), ha='center', va='bottom', rotation=0)

    ax.set_xlabel('Natureza Despesa Detalhada por Mês')
    ax.set_ylabel('Saldo')
    ax.set_title('')
    ax.set_xticks(indice + largura_barra / 2)
    # ax.set_xticklabels(meses)
    ax.legend(title='Natureza Despesa', bbox_to_anchor=(1.05, 1), loc='upper left')

    return fig

# Criando a aplicação Streamlit
def main():
    # st.title('Gráfico de Barras Agrupadas')
    st.pyplot(grouped_bar_chart())

if __name__ == '__main__':
    main()
