import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60.0, 32.0], [37.0, 40.0], [29.0, 10.0]])
st.write(vals)
cmap = plt.colormaps["tab20c"]
# outer_colors = cmap(np.arange(3) * 4)
# inner_colors = cmap([1, 2, 5, 6, 9, 10])
outer_colors = ["blue", "yellow", "green"]  # Cores para as fatias externas
inner_colors = [
    "red",
    "purple",
    "orange",
    "brown",
    "gray",
    "cyan",
]  # Cores para as fatias internas

ax.pie(
    vals.sum(axis=1),
    labels=["A", "B", "C"],
    radius=1,
    colors=outer_colors,
    # wedgeprops=dict(width=size, edgecolor="w"),
    wedgeprops=dict(width=size, edgecolor="w"),
    autopct=lambda pct: f"{int(pct * sum(vals.sum(axis=1)) / 100)}",
)

ax.pie(
    vals.flatten(),
    labels=["D", "E", "F", "G", "H", "I"],
    radius=1 - size,
    colors=inner_colors,
    # wedgeprops=dict(width=size, edgecolor="w"),
    wedgeprops=dict(width=size, edgecolor="w"),
    autopct=lambda pct: f"{int(pct * sum(vals.flatten()) / 100)}",
)

ax.set(aspect="equal", title="Pie plot with `ax.pie`")
st.pyplot(fig)


# fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

# size = 0.3
# vals = np.array([[60.0, 32.0], [37.0, 40.0], [29.0, 10.0]])
# # Normalize vals to 2 pi
# valsnorm = vals / np.sum(vals) * 2 * np.pi
# # Obtain the ordinates of the bar edges
# valsleft = np.cumsum(np.append(0, valsnorm.flatten()[:-1])).reshape(vals.shape)

# cmap = plt.colormaps["tab20c"]
# outer_colors = cmap(np.arange(3) * 4)
# inner_colors = cmap([1, 2, 5, 6, 9, 10])

# ax.bar(
#     x=valsleft[:, 0],
#     width=valsnorm.sum(axis=1),
#     bottom=1 - size,
#     height=size,
#     color=outer_colors,
#     edgecolor="w",
#     linewidth=1,
#     align="edge",
# )

# ax.bar(
#     x=valsleft.flatten(),
#     width=valsnorm.flatten(),
#     bottom=1 - 2 * size,
#     height=size,
#     color=inner_colors,
#     edgecolor="w",
#     linewidth=1,
#     align="edge",
# )

# ax.set(title="Pie plot with `ax.bar` and polar coordinates")
# ax.set_axis_off()
# plt.show()
