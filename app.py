import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================================================================
# 1. PAGE CONFIGURATION & CUSTOM CSS (Must be at the very top)
# ==============================================================================
st.set_page_config(layout="wide", page_title="Aesthetic Trend Index")

# Injecting Custom CSS for a clean, editorial Pinterest aesthetic
st.markdown("""
    <style>
    /* Importing high-fashion typography */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500;600&display=swap');

    /* Premium Minimal Canvas */
    .stApp {
        background-color: #FAF9F6; /* Luxury Off-White / Alabaster */
        color: #1A1A1A; /* Deep Charcoal */
        font-family: 'Inter', sans-serif;
    }

    /* Magazine Editorial Headings */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        color: #1A1A1A !important;
        letter-spacing: -0.01em;
    }

    /* Elegant Moodboard Grid Card */
    .aesthetic-card {
        background: #FFFFFF;
        border: 1px solid #EBE9E1;
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(26, 26, 26, 0.02);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .aesthetic-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 30px rgba(26, 26, 26, 0.05);
        border-color: #D1CFC7;
    }

    /* Minimalist Color Indicator Dots */
    .color-dot {
        height: 16px;
        width: 16px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 10px;
        border: 1px solid rgba(0, 0, 0, 0.08);
    }
    
    /* Clean Divider Line */
    hr {
        border: 0;
        border-top: 1px solid #EBE9E1 !important;
        margin: 20px 0 !important;
    }
    </style>
""", unsafe_allow_html=True)


# ==============================================================================
# 2. DATA LOADING
# ==============================================================================
# Loading your updated data.csv file
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    # Fallback dataset if data.csv is not found locally during testing
    fallback_data = {
        "Aesthetic": ["Office Siren", "Brat", "Eclectic Grandpa"],
        "VibeCheck": ["90s corporate chic with a sharp intellectual edge.", "Messy rebellious party-girl energy with a raw club culture vibe.", "Cozy retro maximalism and layered styling inspired by vintage menswear."],
        "CoreElements": ["Bayonetta glasses; Pencil skirts", "Neon lime green; Distressed leather", "Oversized knit vests; Corduroy trousers"],
        "KeyBrands": ["Miu Miu; Gucci", "Acne Studios; Mowalola", "Bode; Tyler the Creator"],
        "LongevityPredictor": ["Peak Trend", "High-Impact Flash", "Rising Trend"],
        "Season": ["Winter", "Summer", "Autumn"],
        "Color": ["#3A3B3C", "#8ACE00", "#556B2F"]
    }
    df = pd.DataFrame(fallback_data)


# ==============================================================================
# 3. APP HEADER
# ==============================================================================
st.title("Aesthetic Trend Index")
st.markdown("<p style='font-style: italic; color: #666; font-size: 1.1rem; margin-top: -15px;'>A curated lookbook and contemporary subculture analysis.</p>", unsafe_allow_html=True)
st.write("---")


# ==============================================================================
# 4. MOODBOARD GRID SYSTEM (Updated for 3-color palettes)
# ==============================================================================
st.subheader("Current Aesthetics Overview")

# Build a responsive 3-column layout grid
cols = st.columns(3)

for index, row in df.iterrows():
    with cols[index % 3]:
        # Pack everything into a single HTML block string
        card_html = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500;600&display=swap');
            
            .aesthetic-card {{
                background: #FFFFFF;
                border: 1px solid #EBE9E1;
                border-radius: 8px;
                padding: 24px;
                font-family: 'Inter', sans-serif;
                color: #1A1A1A;
                box-shadow: 0 4px 20px rgba(26, 26, 26, 0.02);
            }}
            h3 {{
                font-family: 'Playfair Display', serif !important;
                font-weight: 400 !important;
                margin: 0 0 12px 0; 
                font-size: 1.6rem;
                color: #1A1A1A;
            }}
            .palette-container {{
                display: flex;
                align-items: center;
                gap: 6px;
            }}
            .color-dot {{
                height: 20px;
                width: 20px;
                border-radius: 50%;
                display: inline-block;
                border: 1px solid rgba(0, 0, 0, 0.08);
            }}
            hr {{
                border: 0;
                border-top: 1px solid #EBE9E1;
                margin: 20px 0;
            }}
        </style>
        
        <div class="aesthetic-card">
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; text-transform: uppercase; color: #76746E; letter-spacing: 0.08em; margin-bottom: 12px;">
                <span>{row['LongevityPredictor']}</span>
                <span>{row['Season']}</span>
            </div>
            
            <h3>{row['Aesthetic']}</h3>
            
            <p style="font-size: 0.92rem; color: #4A4A4A; line-height: 1.5; font-style: italic; margin-bottom: 18px;">
                "{row['VibeCheck']}"
            </p>
            
            <div style="font-size: 0.85rem; line-height: 1.6; color: #1A1A1A; margin-bottom: 6px;">
                <strong style="text-transform: uppercase; font-size: 0.75rem; color: #76746E; letter-spacing: 0.03em;">Essentials:</strong> {row['CoreElements']}
            </div>
            <div style="font-size: 0.85rem; line-height: 1.6; color: #1A1A1A; margin-bottom: 18px;">
                <strong style="text-transform: uppercase; font-size: 0.75rem; color: #76746E; letter-spacing: 0.03em;">Key Brands:</strong> {row['KeyBrands']}
            </div>
            
            <hr>
            
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="text-transform: uppercase; font-size: 0.75rem; color: #76746E; letter-spacing: 0.03em; font-weight: 500;">Palette:</span>
                <div class="palette-container">
                    <span class="color-dot" style="background-color: {row['Color1']};" title="{row['Color1']}"></span>
                    <span class="color-dot" style="background-color: {row['Color2']};" title="{row['Color2']}"></span>
                    <span class="color-dot" style="background-color: {row['Color3']};" title="{row['Color3']}"></span>
                </div>
            </div>
        </div>
        """
        
        # Render the custom card using Streamlit Components
        st.components.v1.html(card_html, height=340, scrolling=False)

# ==============================================================================
# 5. DATA VISUALIZATION SECTION
# ==============================================================================
st.subheader("Trend Analytics")

# Sample trend over time dataframe
trend_data = pd.DataFrame({
    "Timeline": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Velocity": [35, 48, 72, 68, 94, 120]
})

fig = px.line(trend_data, x="Timeline", y="Velocity", title="Trend Velocity Analysis")

# Modernist Plotly Styling Architecture
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",   # Transparent workspace background
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent overall paper wrapper
    font_family="Inter",
    font_color="#1A1A1A",
    title_font_family="Playfair Display",
    title_font_size=22,
    margin=dict(l=10, r=10, t=50, b=10),
    xaxis=dict(
        showgrid=False, 
        linecolor="#EBE9E1", 
        tickfont=dict(size=11, color="#76746E")
    ),
    yaxis=dict(
        showgrid=True, 
        gridcolor="#EBE9E1", 
        linecolor="rgba(0,0,0,0)",
        tickfont=dict(size=11, color="#76746E")
    )
)

# Render the path line as an ultra-crisp charcoal line
fig.update_traces(
    line_color="#1A1A1A", 
    line_width=2,
    hovertemplate="Velocity: %{y}<extra></extra>"
)

st.plotly_chart(fig, use_container_width=True)
