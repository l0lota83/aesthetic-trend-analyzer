import streamlit as st
import pandas as pd
import plotly.express as px

# Page Title
st.title("✨ Aesthetic Trend Analyzer")

# Load Data
data = pd.read_csv("data.csv")

# Dataset
st.header("📊 Aesthetic Dataset")
st.dataframe(data)

# Color Palettes
st.header("🎨 Color Palettes")

for _, row in data.iterrows():
    st.markdown(
        f"""
        <div style="
        background:{row['Color']};
        padding:20px;
        border-radius:10px;
        margin-bottom:10px;">
        <b>{row['Aesthetic']}</b><br>
        {row['Color']}
        </div>
        """,
        unsafe_allow_html=True
    )

# Filter
st.header("🔍 Explore Aesthetics")

selected = st.selectbox(
    "Choose an aesthetic",
    data["Aesthetic"]
)

filtered = data[data["Aesthetic"] == selected]

st.write(filtered)

# Popularity Chart
st.header("📈 Popularity Comparison")

fig = px.bar(
    data,
    x="Aesthetic",
    y="Popularity",
    title="Popularity Comparison"
)

st.plotly_chart(fig)

# Trend Score Graph
st.header("📉 Trend Score Analysis")

fig2 = px.line(
    data,
    x="Aesthetic",
    y="TrendScore",
    markers=True,
    title="Trend Scores"
)

st.plotly_chart(fig2)

# Pie Chart
st.header("🥧 Popularity Distribution")

fig3 = px.pie(
    data,
    names="Aesthetic",
    values="Popularity",
    title="Popularity Share"
)

st.plotly_chart(fig3)

# Moodboards
st.header("🖼️ Moodboard Gallery")

st.info(
    "Add aesthetic images to an 'images' folder and connect them here."
)

# Recommendation Feature
st.header("💡 Aesthetic Recommendation")

style = st.selectbox(
    "Which style do you prefer?",
    [
        "Minimalist",
        "Cute",
        "Vintage",
        "Luxury"
    ]
)

if style == "Minimalist":
    st.success("Recommended Aesthetic: Acubi")

elif style == "Cute":
    st.success("Recommended Aesthetic: Coquette")

elif style == "Vintage":
    st.success("Recommended Aesthetic: Y2K")

elif style == "Luxury":
    st.success("Recommended Aesthetic: Old Money")
