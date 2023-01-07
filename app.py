import streamlit as st
import pandas as pd
import plotly.express as px
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Time",
    ("By Day", "By Month", "By Year")
)

# if(add_selectbox=="By Day"):
#     x = st.sidebar.slider('Days', min_value=1, max_value=7, step=1)
if(add_selectbox=="By Month"):
    x = st.sidebar.slider('Month', min_value=1, max_value=12, step=1)
# if(add_selectbox=="By Year"):
#     x = st.sidebar.slider('Days', min_value=1, max_value=10, step=1)

df = pd.read_csv ('Groceries_dataset.csv')
df['year'] = pd.DatetimeIndex(df['Date']).year
st.dataframe(df) 
