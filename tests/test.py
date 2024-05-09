# import streamlit as st
# import pandas as pd
# import numpy as np

# df = np.random.randn(20, 3)
# st.write(df)

# chart_data = pd.DataFrame(df, columns=["a", "b", "c"])

# st.line_chart(chart_data)


# from matplotlib import pyplot as plt
# import numpy as np
# import streamlit as st


# size = 6
# cars = ["AUDI", "BMW", "FORD", "TESLA", "JAGUAR", "MERCEDES"]

# data = np.array([[23, 16], [17, 23], [35, 11], [29, 33], [12, 27], [41, 42]])
# norm = data / np.sum(data) * 2 * np.pi
# left = np.cumsum(np.append(0, norm.flatten()[:-1])).reshape(data.shape)
# cmap = plt.get_cmap("tab20c")
# outer_colors = cmap(np.arange(6) * 4)
# inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10, 12, 13, 15, 17, 18, 20]))
# fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(polar=True))

# ax.bar(
#     x=left[:, 0],
#     width=norm.sum(axis=1),
#     bottom=1 - size,
#     height=size,
#     color=outer_colors,
#     edgecolor="w",
#     linewidth=1,
#     align="edge",
# )

# ax.bar(
#     x=left.flatten(),
#     width=norm.flatten(),
#     bottom=1 - 2 * size,
#     height=size,
#     color=inner_colors,
#     edgecolor="w",
#     linewidth=1,
#     align="edge",
# )

# ax.set(title="Nested pie chart")
# ax.set_axis_off()
# st.pyplot(fig)
# # plt.show()


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo CSV
df = pd.read_csv(
    "./assets/xls/empenhos.csv", encoding="ISO-8859-1", sep=";", decimal=","
)

# Selecionar apenas as colunas visíveis
colunas_visiveis = [
    "Natureza Despesa",
    "Natureza Despesa Detalhada",
    "Métrica",
    "Mês",
    "Empenhado",
    "Liquidado",
]
df = df[colunas_visiveis]

# Normalizando os dados para cada mês
emp_data = np.array(df["Empenhado"].values)
emp_data = emp_data.tolist()
liq_data = np.array(df["Liquidado"].values)
liq_data = liq_data.tolist()

norm_emp = float(emp_data) / float(np.sum(array(emp_data))) * 2 * np.pi
norm_liq = float(liq_data) / float(np.sum(liq_data)) * 2 * np.pi

left_emp = np.cumsum(np.append(0, norm_emp.flatten()[:-1])).reshape(emp_data.shape)
left_liq = np.cumsum(np.append(0, norm_liq.flatten()[:-1])).reshape(liq_data.shape)

# Criando a paleta de cores
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(len(emp_data)) * 4)
inner_colors = cmap(np.arange(len(liq_data)) * 4)

# Plotando o gráfico
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(polar=True))
ax.bar(
    x=left_emp.flatten(),
    width=norm_emp.flatten(),
    bottom=1,
    height=0.3,
    color=outer_colors,
    edgecolor="w",
    linewidth=1,
    align="edge",
)
ax.bar(
    x=left_liq.flatten(),
    width=norm_liq.flatten(),
    bottom=0.7,
    height=0.3,
    color=inner_colors,
    edgecolor="w",
    linewidth=1,
    align="edge",
)

# Configurando título e eixo
ax.set(title="Relação de Valor Empenhado e Liquidado por Mês")
ax.set_axis_off()

# Exibindo o gráfico no Streamlit
st.pyplot(fig)
