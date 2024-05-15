# importing package
import altair as alt
import pandas as pd
import streamlit as st
  
# create data
data = pd.DataFrame([['A', 10, 20],
                     ['B', 5, 29],
                     ['B', 10, 39],
                     ['A', 15, 29],
                     ['B', 15, 20]],
                    columns=['Team', 'Round 1', 'Round 2'])
# view data
print(data)
  
gp_chart = alt.Chart(data).mark_bar().encode(
    alt.Column('Round 2'), alt.X('Team'),
    alt.Y('Round 1', axis=alt.Axis(grid=False)),
    alt.Color('Team'))
  
st.write(gp_chart)