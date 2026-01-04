import streamlit as st
from layout import base_layout

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="CleanDrive",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# BASE LAYOUT (includes navbar)
# -----------------------------
base_layout()
st.markdown(
    """
    <style>
    /* Hide Streamlit sidebar */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Header (Hero Section)
# -----------------------------
st.markdown(
    """
    <style>
        .hero {
            text-align: center;
            margin-top: 60px;
            color: black;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 18px;
            border-radius: 999px;
            background: rgba(34,197,94,0.15);
            color: #22c55e;
            font-size: 14px;
            margin-bottom: 24px;
            font-weight: 600;
        }
        .title {
            font-size: 52px;
            font-weight: 800;
            line-height: 1.2;
        }
        .gradient-text {
            background: linear-gradient(90deg, #22c55e, #16a34a);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            max-width: 640px;
            margin: 24px auto;
            font-size: 18px;
            color: #6b7280;
        }
    </style>

    <div class="hero">
        <div class="badge">🌿 Make every ride a greener one</div>
        <div class="title">
            Track Your Vehicle's <br/>
            <span class="gradient-text">Carbon Footprint</span>
        </div>
        <div class="subtitle">
            Understand your vehicle’s CO₂ emissions, receive eco-driving guidance,
            and make environmentally responsible transportation choices with CleanDrive.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# CTA Buttons
# -----------------------------
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    b1, b2 = st.columns(2)
    with b1:
        if st.button("Create account", use_container_width=True):
            st.switch_page("pages/register.py")
    with b2:
        if st.button("Sign In", use_container_width=True):
            st.switch_page("pages/login.py")

# -----------------------------
# Feature Cards (UPDATED)
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

card_css = """
<style>
.card {
    background: rgba(255,255,255,0.08);   /* visible by default */
    border: 1.5px solid rgba(34,197,94,0.5);
    border-radius: 18px;
    padding: 28px;
    transition: all 0.3s ease;
}
.card:hover {
    border-color: #22c55e;
    transform: translateY(-6px);
    box-shadow: 0px 8px 20px rgba(34,197,94,0.25);
}
.card h3 {
    margin-bottom: 10px;
}
.card p {
    color: #374151;
    font-size: 15px;
    line-height: 1.6;
}
</style>
"""

st.markdown(card_css, unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown(
        """
        <div class="card">
            <h3>📊 CO₂ Emission Prediction</h3>
            <p>
                Predict your vehicle’s carbon dioxide emissions using a
                machine learning–based estimation model for better awareness.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        """
        <div class="card">
            <h3>💡 Personalized Eco Tips</h3>
            <p>
                Get personalized eco-driving recommendations to reduce environmental impact
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f3:
    st.markdown(
        """
        <div class="card">
            <h3>🌱 Eco Advisory</h3>
            <p>
                Access static eco-driving recommendations and best practices
                designed to help reduce vehicle emissions and promote sustainability.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:80px;
        font-size:14px;
        color:#6b7280;
    ">
        © 2025 CleanDrive. Drive clean, drive green.
    </div>
    """,
    unsafe_allow_html=True
)
