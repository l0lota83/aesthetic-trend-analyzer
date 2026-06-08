import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Aesthetic Trend Analyzer")

data = pd.read_csv("data.csv")

st.header("Aesthetic Dataset")
st.dataframe(data)

selected = st.selectbox(
    "Choose Aesthetic",
    data["Aesthetic"]
)

filtered = data[data["Aesthetic"] == selected]

st.write(filtered)

fig = px.bar(
    data,
    x="Aesthetic",
    y="Popularity",
    title="Popularity Comparison"
)

st.plotly_chart(fig)
