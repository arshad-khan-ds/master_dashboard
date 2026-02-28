import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Arshad Khan | Strategic Tourism Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Corporate Minimalist CSS (Pure White & Navy)
st.markdown("""
    <style>
    /* Reset to Pure White */
    .stApp { background-color: #FFFFFF; }
    
    /* Hide Sidebar */
    [data-testid="stSidebar"] { display: none; }

    /* Formal Serif Heading */
    h1 {
        color: #002B36;
        font-family: 'Times New Roman', serif;
        text-align: center;
        font-size: 3rem;
        margin-top: 10px;
    }
    
    .sub-header {
        text-align: center;
        color: #666666;
        font-family: 'Arial', sans-serif;
        font-size: 0.85rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 50px;
    }

    /* Metric Styling - Authoritative & Sharp */
    [data-testid="stMetricValue"] {
        font-family: 'Times New Roman', serif;
        font-size: 2.4rem !important;
        color: #002B36;
    }

    /* Flat Navy Buttons */
    .stLinkButton > a {
        width: 100%;
        border-radius: 0px !important;
        background-color: #002B36 !important;
        color: white !important;
        border: none !important;
        height: 3rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        text-decoration: none;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
st.markdown('<h1>Strategic Tourism Intelligence Portfolio</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Independent Audit Suite • Arshad Khan • 2026</p>', unsafe_allow_html=True)

# 4. Main Content Grid
col1, col2, col3 = st.columns(3)

# --- PILLAR 1: G20 TOURISM DIVIDEND (MACRO) ---
with col1:
    st.caption("I. MACRO-LEVEL AUDIT")
    st.subheader("The G20 Tourism Dividend")
    st.write("""
    Causal impact analysis utilizing a **Synthetic Control Method** to isolate India's 
    'G20 Premium'. The model identifies a **$2.18 Billion surplus** in international 
    receipts (2023-2024) attributed to global diplomatic leadership and branding.
    """)
    st.markdown("---")
    st.metric(label="Cumulative Surplus", value="$2.18B", delta="+4.7%")
    st.link_button("Access Interactive Model", "https://g20-dividend.streamlit.app/")

# --- PILLAR 2: DELHI MARKET AUDIT (MESO) ---
with col2:
    st.caption("II. MESO-LEVEL AUDIT")
    st.subheader("Delhi PDIS Market Audit")
    st.write("""
    Market resilience audit identifying environmental tipping points. Analysis confirms 
    **30°C as the Yield Ceiling**, beyond which RevPAR growth stagnates regardless of 
    demand volume, necessitating a pivot toward climate-controlled 'Sanctuary Assets'.
    """)
    st.markdown("---")
    st.metric(label="Yield Ceiling", value="30°C", delta="-0.70 Heat Elasticity", delta_color="inverse")
    st.link_button("Access Market Audit", "https://delhi-strategic-tourism-intelligence.streamlit.app/")

# --- PILLAR 3: TAJ MAHAL LUSTER AUDIT (MICRO) ---
with col3:
    st.caption("III. MICRO-LEVEL AUDIT")
    st.subheader("Taj Mahal Luster Audit")
    st.write("""
    Sentiment audit utilizing **BERT NLP** to identify 'Luster Decay'. 
    Analysis isolates the **'Politeness Gap'**, a phenomenon where high numerical 
    ratings mask structural dissatisfaction regarding infrastructure and air quality.
    """)
    st.markdown("---")
    st.metric(label="Politeness Gap", value="High", delta="Sentiment Risk", delta_color="inverse")
    st.link_button("Access Sentiment Model", "https://taj-mahal.streamlit.app/")

# 5. Formal Footer
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style="border-top: 1px solid #EEEEEE; padding-top: 20px; text-align: center;">
        <p style="color: #999; font-size: 0.8rem; font-family: Arial;">
            © 2026 Arshad Khan | All Rights Reserved <br>
            Confidential Strategic Intelligence 
        </p>
    </div>
""", unsafe_allow_html=True)