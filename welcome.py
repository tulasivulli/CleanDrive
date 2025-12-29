import streamlit as st
import streamlit.components.v1 as components

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="CleanDrive",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# Header (Streamlit native)
# -----------------------------
st.markdown(
    """
    <div style="display:flex; align-items:center; gap:12px; padding:20px;">
        <div style="font-size:28px;">🌱</div>
        <div style="
            font-size:26px;
            font-weight:700;
            background: linear-gradient(90deg, #22c55e, #16a34a);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        ">
            CleanDrive
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HERO SECTION (components.html — FIXED)
# -----------------------------
components.html(
    """
    <style>
        body {
            background-color: #0e1117;
            color: white;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
        }

        .hero {
            text-align: center;
            margin-top: 60px;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 18px;
            border-radius: 999px;
            background: rgba(34,197,94,0.12);
            color: #22c55e;
            font-size: 14px;
            margin-bottom: 24px;
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
            max-width: 620px;
            margin: 24px auto;
            font-size: 18px;
            color: #9ca3af;
        }
    </style>

    <div class="hero">
        <div class="badge">🌿 Make every ride a greener one</div>

        <div class="title">
            Track Your Vehicle's <br/>
            <span class="gradient-text">Carbon Footprint</span>
        </div>

        <div class="subtitle">
            Understand your CO₂ emissions, get personalized eco-driving tips,
            and contribute to a cleaner environment with our AI-powered platform.
        </div>
    </div>
    """,
    height=420
)

# -----------------------------
# CTA Buttons (Streamlit native)
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
# Feature Cards
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

card_css = """
<style>
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 26px;
    transition: all 0.3s ease;
}
.card:hover {
    border-color: #22c55e;
    transform: translateY(-6px);
}
.card p {
    color: #9ca3af;
    font-size: 14px;
}
</style>
"""

st.markdown(card_css, unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Predict Emissions</h3>
            <p>Calculate your vehicle’s CO₂ output using our ML-powered prediction model.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f2:
    st.markdown(
        """
        <div class="card">
            <h3>💡 Eco Tips</h3>
            <p>Get personalized eco-driving recommendations to reduce environmental impact.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with f3:
    st.markdown(
        """
        <div class="card">
            <h3>🤖 AI Assistant</h3>
            <p>Ask our chatbot about eco-driving, mileage, emissions, and sustainability.</p>
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
        color:#9ca3af;
    ">
        © 2025 CleanDrive. Drive clean, drive green.
    </div>
    """,
    unsafe_allow_html=True
)

