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
# 4. MOODBOARD GRID SYSTEM (Safe Base64 Local Image Core)
# ==============================================================================
st.subheader("Current Aesthetics Overview")

import base64

# Функция для безопасной конвертации локальной картинки в формат Base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()
    except Exception:
        # Если файл по какой-то причине не найден, отдаем пустую стильную заглушку цвета карточки
        return "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"

# Строим адаптивную сетку в 3 колонки
cols = st.columns(3)

for index, row in df.iterrows():
    with cols[index % 3]:
        # Безопасно кодируем все три кадра lookbook-коллажа
        img1_base64 = get_base64_image(row['Image1'])
        img2_base64 = get_base64_image(row['Image2'])
        img3_base64 = get_base64_image(row['Image3'])
        
        card_html = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Inter:wght@300;400;500;600&display=swap');
            
            .aesthetic-card {{
                background: #FFFFFF;
                border: 1px solid #EBE9E1;
                border-radius: 12px;
                overflow: hidden;
                font-family: 'Inter', sans-serif;
                color: #1A1A1A;
                box-shadow: 0 4px 20px rgba(26, 26, 26, 0.02);
                margin-bottom: 24px;
            }}
            
            .moodboard-collage {{
                display: grid;
                grid-template-columns: 1.8fr 1fr;
                grid-template-rows: 105px 105px;
                gap: 4px;
                background: #EBE9E1;
                height: 214px;
                width: 100%;
            }}
            
            .collage-img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                background: #EBE9E1; /* Элегантный фон, пока картинка грузится */
            }}
            
            .img-main {{
                grid-row: span 2;
            }}
            
            .card-content {{
                padding: 20px 24px 24px 24px;
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
            <div class="moodboard-collage">
                <img class="collage-img img-main" src="{img1_base64}">
                <img class="collage-img" src="{img2_base64}">
                <img class="collage-img" src="{img3_base64}">
            </div>
            
            <div class="card-content">
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
                    <strong style="text-transform: uppercase; font-size: 0.75rem; color: #76746E; letter-spacing: 0.03em;">Palette:</strong>
                    <div class="palette-container">
                        <span class="color-dot" style="background-color: {row['Color1']};" title="{row['Color1']}"></span>
                        <span class="color-dot" style="background-color: {row['Color2']};" title="{row['Color2']}"></span>
                        <span class="color-dot" style="background-color: {row['Color3']};" title="{row['Color3']}"></span>
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.components.v1.html(card_html, height=570, scrolling=False)

# ==============================================================================
# 5. DATA VISUALIZATION SECTION (Aesthetic Trend Analytics)
# ==============================================================================
st.subheader("Trend Velocity & Analytics")
st.markdown("<p style='font-style: italic; color: #666; font-size: 0.95rem; margin-top: -10px; margin-bottom: 20px;'>Comparative search volume and social media engagement trajectory (Jan - Jun).</p>", unsafe_allow_html=True)

# 1. Formatting analytical data for all 9 aesthetics
analytics_data = {
    "Timeline": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 9,
    "Aesthetic": (
        ["Acubi"] * 6 + ["Coquette"] * 6 + ["Office Siren"] * 6 + 
        ["Brat"] * 6 + ["Eclectic Grandpa"] * 6 + ["Y2K"] * 6 + 
        ["Clean Girl"] * 6 + ["Balletcore"] * 6 + ["Old Money"] * 6
    ),
    "Velocity Index": [
        # Acubi (Stable, steady Korean streetwear)
        55, 58, 60, 62, 65, 64,
        # Coquette (High stable baseline)
        82, 85, 80, 88, 85, 83,
        # Office Siren (Currently peaking)
        70, 78, 85, 92, 98, 95,
        # Brat (Explosive summer club culture hype)
        30, 35, 42, 60, 95, 120,
        # Eclectic Grandpa (Steady rising vintage trend)
        40, 48, 55, 68, 74, 80,
        # Y2K (Gentle decline, shifting into staple wardrobe)
        75, 72, 68, 65, 60, 58,
        # Clean Girl (Slight decline, evolving into new forms)
        90, 88, 82, 79, 75, 72,
        # Balletcore (Soft seasonal shifts in Spring)
        60, 68, 75, 78, 72, 68,
        # Old Money (Absolute timeless, permanent classic)
        70, 71, 70, 72, 70, 71
    ]
}

df_analytics = pd.DataFrame(analytics_data)

# 2. Building an interactive multi-line Plotly chart
fig = px.line(
    df_analytics, 
    x="Timeline", 
    y="Velocity Index", 
    color="Aesthetic",
    markers=True, # Adds clean data points on the line vertices
    color_discrete_sequence=[
        "#8A8A8A", "#FFC0CB", "#3A3B3C", "#8ACE00", "#556B2F", 
        "#FF69B4", "#F5F5DC", "#E6CFE6", "#D4AF37"
    ] # Line colors strictly match the main signature hex codes from the cards!
)

# 3. Editorial Minimalist Chart Styling Engine
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",   # Transparent chart canvas backplate
    paper_bgcolor="rgba(0,0,0,0)",  # Transparent outer layout background
    font_family="Inter",
    font_color="#1A1
