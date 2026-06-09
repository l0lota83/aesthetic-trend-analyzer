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

# 1. Analytical dataset for all 9 aesthetics
analytics_data = {
    "Timeline": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 9,
    "Aesthetic": (
        ["Acubi"] * 6 + ["Coquette"] * 6 + ["Office Siren"] * 6 + 
        ["Brat"] * 6 + ["Eclectic Grandpa"] * 6 + ["Y2K"] * 6 + 
        ["Clean Girl"] * 6 + ["Balletcore"] * 6 + ["Old Money"] * 6
    ),
    "Velocity Index": [
        55, 58, 60, 62, 65, 64,  # Acubi
        82, 85, 80, 88, 85, 83,  # Coquette
        70, 78, 85, 92, 98, 95,  # Office Siren
        30, 35, 42, 60, 95, 120, # Brat
        40, 48, 55, 68, 74, 80,  # Eclectic Grandpa
        75, 72, 68, 65, 60, 58,  # Y2K
        90, 88, 82, 79, 75, 72,  # Clean Girl
        60, 68, 75, 78, 72, 68,  # Balletcore
        70, 71, 70, 72, 70, 71   # Old Money
    ]
}

df_analytics = pd.DataFrame(analytics_data)

# 2. Render dynamic line graph
fig = px.line(
    df_analytics, 
    x="Timeline", 
    y="Velocity Index", 
    color="Aesthetic",
    markers=True,
    color_discrete_sequence=[
        "#8A8A8A", "#FFC0CB", "#3A3B3C", "#8ACE00", "#556B2F", 
        "#FF69B4", "#F5F5DC", "#E6CFE6", "#D4AF37"
    ]
)

# 3. Clean editorial layout styling
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font_family="Inter",
    font_color="#1A1A1A",
    hovermode="x unified",
    margin=dict(l=10, r=10, t=20, b=10),
    legend=dict(
        title_text="Aesthetics",
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5,
        font=dict(size=11)
    ),
    xaxis=dict(
        showgrid=False, 
        linecolor="#EBE9E1", 
        tickfont=dict(size=11, color="#76746E")
    ),
    yaxis=dict(
        showgrid=True, 
        gridcolor="#EBE9E1",
        linecolor="rgba(0,0,0,0)",
        tickfont=dict(size=11, color="#76746E"),
        title_text="Trend Velocity Index"
    )
)

fig.update_traces(
    line_width=2.5,
    marker=dict(size=6),
    hovertemplate="%{y}"
)

st.plotly_chart(fig, use_container_width=True)

# ==============================================================================
# 6. TREND SCORE ANALYSIS SECTION
# ==============================================================================
st.write("---")
st.subheader("Trend Score Analysis & Nomenclature")

# Create a two-column layout for the metrics and definition guide
analysis_cols = st.columns([1, 2])

with analysis_cols[0]:
    st.markdown("""
    <div style="background-color: #FFFFFF; border: 1px solid #EBE9E1; border-radius: 12px; padding: 20px; height: 100%;">
        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.2rem; margin-top: 0;">Methodology</h4>
        <p style="font-size: 0.88rem; color: #4A4A4A; line-height: 1.5; margin-bottom: 0;">
            Our <strong>Trend Velocity Index</strong> weights global search volume variations, TikTok/Instagram audio reuse rates, and retail stock introduction speeds to rank current cultural shifts.
        </p>
    </div>
    """, unsafe_allow_html=True)

with analysis_cols[1]:
    st.markdown("""
    <div style="background-color: #FFFFFF; border: 1px solid #EBE9E1; border-radius: 12px; padding: 20px; height: 100%;">
        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.2rem; margin-top: 0;">Nomenclature Breakdown</h4>
        <ul style="font-size: 0.88rem; color: #4A4A4A; padding-left: 20px; margin-bottom: 0; line-height: 1.6;">
            <li><strong>Permanent Classic (Score 70-75):</strong> Immune to seasonal algorithms. High investment value.</li>
            <li><strong>Stable Core (Score 60-85):</strong> Long-term cultural relevance with a deeply loyal subculture base.</li>
            <li><strong>Peak / Rising Trend (Score 80-95):</strong> High commercial conversion rate right now. Mainstream adoption phase.</li>
            <li><strong>High-Impact Flash (Score 95+):</strong> Viral hyper-acceleration. Extreme cultural capital but fast decay risk.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Add a clean data table layout below the cards
st.markdown("<br>", unsafe_allow_html=True)

# Generate a sorted breakdown ranking the highest velocity trends for June
df_ranked = df_analytics[df_analytics["Timeline"] == "Jun"].sort_values(by="Velocity Index", ascending=False)

# Render a styled headers row for our leaderboard
st.markdown("""
<div style="display: flex; justify-content: space-between; padding: 10px 16px; background-color: #EBE9E1; border-radius: 6px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #1A1A1A;">
    <span>Rank & Aesthetic Movement</span>
    <span>June Velocity Score</span>
</div>
""", unsafe_allow_html=True)

# Loop through data to generate individual sleek list rows
for rank, (_, row) in enumerate(df_ranked.iterrows(), start=1):
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px 16px; border-bottom: 1px solid #EBE9E1; font-size: 0.9rem; color: #1A1A1A;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-family: monospace; font-size: 0.8rem; color: #76746E;">#{rank:02d}</span>
            <strong style="font-family: 'Inter', sans-serif; font-weight: 500;">{row['Aesthetic']}</strong>
        </div>
        <span style="font-family: monospace; font-weight: 600; color: {'#8ACE00' if row['Velocity Index'] > 95 else '#1A1A1A'};">
            {row['Velocity Index']} pts
        </span>
    </div>
    """, unsafe_allow_html=True)

    # ==============================================================================
# 7. INTERACTIVE COLOR PALETTE VISUALIZATION
# ==============================================================================
st.write("---")
st.subheader("Global Color Spectrum & Palette Explorer")
st.markdown("<p style='font-style: italic; color: #666; font-size: 0.95rem; margin-top: -10px; margin-bottom: 24px;'>A high-density visual index mapping the exact hex coordinates driving this season's subcultures.</p>", unsafe_allow_html=True)

# Собираем данные обо всех цветах из нашего основного датафрейма df
color_records = []
for _, row in df.iterrows():
    color_records.append({"Aesthetic": row["Aesthetic"], "Hex": row["Color1"], "Label": "Primary"})
    color_records.append({"Aesthetic": row["Aesthetic"], "Hex": row["Color2"], "Label": "Secondary"})
    color_records.append({"Aesthetic": row["Aesthetic"], "Hex": row["Color3"], "Label": "Accent"})

df_colors = pd.DataFrame(color_records)

# Сетка-лаборатория: делим экран на левую интерактивную витрину и правый аналитический блок
palette_cols = st.columns([2, 1])

with palette_cols[0]:
    # Генерируем сплошную мозаичную CSS-панель (Color Grid Macro View)
    mosaic_html = """
    <style>
        .spectrum-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
            gap: 8px;
            background: #FFFFFF;
            border: 1px solid #EBE9E1;
            border-radius: 12px;
            padding: 16px;
        }
        .spectrum-brick {
            height: 85px;
            border-radius: 6px;
            position: relative;
            cursor: pointer;
            transition: all 0.23s cubic-bezier(0.16, 1, 0.3, 1);
            border: 1px solid rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 10px;
            box-sizing: border-box;
        }
        .spectrum-brick:hover {
            transform: scale(1.04);
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
            z-index: 2;
        }
        .brick-meta {
            font-family: monospace;
            font-size: 0.72rem;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(4px);
            padding: 2px 4px;
            border-radius: 3px;
            color: #1A1A1A;
            text-align: center;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .brick-title {
            font-family: 'Inter', sans-serif;
            font-size: 0.65rem;
            text-transform: uppercase;
            letter-spacing: 0.02em;
            color: #76746E;
            margin-bottom: 3px;
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(4px);
            padding: 1px 4px;
            border-radius: 3px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
    </style>
    <div class="spectrum-grid">
    """
    
    # Заполняем мозаику всеми цветами проекта динамически
    for _, c in df_colors.iterrows():
        mosaic_html += f"""
        <div class="spectrum-brick" style="background-color: {c['Hex']};" onclick="navigator.clipboard.writeText('{c['Hex']}'); alert('Copied {c['Hex']} to clipboard!');">
            <div class="brick-title">{c['Aesthetic']}</div>
            <div class="brick-meta">{c['Hex']}</div>
        </div>
        """
    mosaic_html += "</div>"
    
    # Отображаем нашу арт-панель
    st.components.v1.html(mosaic_html, height=310, scrolling=True)

with palette_cols[1]:
    # Справа делаем распределение по тональностям (Color Weight Chart) через Plotly Treemap
    # Это показывает, какие оттенки доминируют в текущей культуре сильнее всего
    fig_tree = px.treemap(
        df_colors, 
        path=["Label", "Aesthetic"], 
        values=[1]*len(df_colors),
        color="Hex",
        color_discrete_map={hex_val: hex_val for hex_val in df_colors["Hex"]}
    )
    
    fig_tree.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_family="Inter"
    )
    fig_tree.update_traces(
        textinfo="label",
        hovertemplate="<b>%{label}</b><br>Hex: %{color}"
    )
    
    st.plotly_chart(fig_tree, use_container_width=True)

   # ==============================================================================
# 8. PIE CHART VISUALIZATION (Market Share of Voice)
# ==============================================================================
st.write("---")
st.subheader("Market Share of Voice & Macro Segmentation")
st.markdown("<p style='font-style: italic; color: #666; font-size: 0.95rem; margin-top: -10px; margin-bottom: 20px;'>A structural breakdown of subcultural dominance filtered by seasonal or longevity lifecycles.</p>", unsafe_allow_html=True)

# Interactive data stream selector
filter_choice = st.selectbox(
    "Analyze Market Segmentation By:",
    ["Aesthetic Longevity Lifecycle", "Seasonal Dominance Pattern"]
)

# Splitting layout into 2 columns: left for chart, right for context insights
pie_cols = st.columns([2, 1])

with pie_cols[0]:
    if filter_choice == "Aesthetic Longevity Lifecycle":
        # Grouping dataset rows by the longevity asset metric
        df_pie = df.groupby("LongevityPredictor").size().reset_index(name="Count")
        fig_pie = px.pie(
            df_pie, 
            values="Count", 
            names="LongevityPredictor", 
            hole=0.6, # Transforms a standard pie into an editorial donut chart
            color_discrete_sequence=["#D4AF37", "#1A1A1A", "#8ACE00", "#8A8A8A"]
        )
    else:
        # Grouping dataset rows by seasonal dominance trends
        df_pie = df.groupby("Season").size().reset_index(name="Count")
        fig_pie = px.pie(
            df_pie, 
            values="Count", 
            names="Season", 
            hole=0.6,
            color_discrete_sequence=["#8A8A8A", "#FFC0CB", "#3A3B3C", "#556B2F"]
        )

    # Styling the donut plot frame to match the premium minimalist UI
    fig_pie.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
        font_color="#1A1A1A",
        legend=dict(
            orientation="v",
