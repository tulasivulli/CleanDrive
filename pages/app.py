import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config (MUST BE FIRST)
# -----------------------------
st.set_page_config(
    page_title="CleanDrive – CO₂ Predictor",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------
# 🔐 Access Control
# -----------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to access predictions")
    st.switch_page("pages/login.py")

# -----------------------------
# 🔝 Top Bar (Right-aligned Logout)
# -----------------------------
top_left, top_right = st.columns([6, 1])

with top_right:
    if st.button("Logout", key="logout_main"):
        st.session_state.show_logout_dialog = True

# -----------------------------
# 🔐 Logout Confirmation Dialog
# -----------------------------
if st.session_state.get("show_logout_dialog", False):

    @st.dialog("Logout Confirmation")
    def logout_dialog():
        st.write(
            "Are you sure you want to logout?\n\n"
            
        )

        c1, c2 = st.columns(2)

        with c1:
            if st.button("Cancel", key="logout_cancel"):
                st.session_state.show_logout_dialog = False
                st.rerun()

        with c2:
            if st.button("Logout", key="logout_confirm"):
                st.session_state.logged_in = False
                st.session_state.username = ""
                st.session_state.show_logout_dialog = False
                st.switch_page("welcome.py")

    logout_dialog()

# -----------------------------
# Load external CSS
# -----------------------------
with open("pages/style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
rf_model = joblib.load("rf_model (2).pkl")
model_columns = joblib.load("model_columns (2).pkl")

# -----------------------------
# Eco Tips
# -----------------------------
ECO_TIPS = {
    "Low": [
        "Maintain regular servicing",
        "Use recommended fuel grade",
        "Drive smoothly",
        "Maintain tire pressure",
        "Avoid sudden acceleration",
        "Change engine oil on time",
        "Reduce vehicle load"
    ],
    "Medium": [
        "Service engine regularly",
        "Avoid long idling",
        "Maintain steady speed",
        "Check wheel alignment",
        "Avoid aggressive driving",
        "Limit AC usage",
        "Plan routes efficiently"
    ],
    "High": [
        "Use public transport",
        "Check emission system",
        "Switch to hybrid/EV",
        "Avoid peak traffic",
        "Fix exhaust issues",
        "Combine short trips",
        "Learn eco-driving"
    ]
}

# -----------------------------
# Page Title
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:25px;">
        <h1>🚗 CleanDrive – CO₂ Emission Predictor</h1>
        <p style="color:#cfcfcf;">
            Predict emissions and get eco-driving tips
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Input Fields
# -----------------------------
left, right = st.columns(2)

with left:
    engine_size = st.number_input("Engine Size (L)", 0.5, 10.0, step=0.1)
    cylinders = st.number_input("Cylinders", 1, 16)
    mileage = st.number_input("Mileage (km)", 0, 500000, step=1000)
    vehicle_age = st.number_input("Vehicle Age (Years)", 0, 30)

with right:
    fuel_city = st.number_input("Fuel City (L/100 km)", 1.0, 30.0)
    fuel_hwy = st.number_input("Fuel Highway (L/100 km)", 1.0, 30.0)
    fuel_comb = st.number_input("Fuel Combined (L/100 km)", 1.0, 30.0)
    fuel_type = st.selectbox("Fuel Type", ["X", "Z", "D", "E", "N"])

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🚀 Predict CO₂ Emission", use_container_width=True):

    input_data = pd.DataFrame(
        [[engine_size, cylinders, fuel_city, fuel_hwy, fuel_comb,
          fuel_type, vehicle_age, mileage]],
        columns=[
            'Engine Size(L)', 'Cylinders',
            'Fuel Consumption City (L/100 km)',
            'Fuel Consumption Hwy (L/100 km)',
            'Fuel Consumption Comb (L/100 km)',
            'Fuel Type', 'Vehicle Age', 'Mileage'
        ]
    )

    input_data = pd.get_dummies(input_data, drop_first=True)
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    prediction = rf_model.predict(input_data)[0]

    emission_level = (
        "Low" if prediction < 150 else
        "Medium" if prediction < 250 else
        "High"
    )

    st.success(f"Predicted CO₂ Emission: {prediction:.2f} g/km")
    st.info(f"Emission Level: {emission_level}")

    tips = ECO_TIPS[emission_level]

    st.markdown(
        f"""
        <div class="eco-wrapper">
            <div class="eco-title">🌿 Smart Eco Tips</div>
            <div class="eco-track">
                {''.join([f'<div class="eco-pill">🌱 {tip}</div>' for tip in tips])}
                {''.join([f'<div class="eco-pill">🌱 {tip}</div>' for tip in tips])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
