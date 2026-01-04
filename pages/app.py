import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components
from layout import base_layout

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="CleanDrive | CO₂ Predictor",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# NAVBAR + SIDEBAR HIDE
# --------------------------------------------------
base_layout()

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# ACCESS CONTROL
# --------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to access predictions")
    st.switch_page("pages/login.py")

# ✅ READ CAR NUMBER FROM SESSION
car_number = st.session_state.get("username", "Driver")

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------
with open("pages/style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Read-only input styling
st.markdown("""
<style>
input[data-baseweb="input"][aria-labelledby="combined_display"] {
    pointer-events: none;
    background-color: white !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# GREEN BUTTON HOVER STYLE
# --------------------------------------------------
st.markdown(
    """
    <style>
    div.stButton > button:hover {
        background-color: lightgreen !important;
        color: white !important;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
rf_model = joblib.load("rf_model (2).pkl")
model_columns = joblib.load("model_columns (2).pkl")

# --------------------------------------------------
# ECO TIPS
# --------------------------------------------------
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

# --------------------------------------------------
# PERSONALIZED TITLE
# --------------------------------------------------
st.markdown(
    f"""
    <div style="text-align:center; margin-bottom:20px;">
        <h1>
            🚗 Welcome <span style="color:#16a34a;">{car_number}</span> to CleanDrive
        </h1>
        <p style="color:black;">
            Predict your vehicle’s CO₂ emissions and receive eco-driving insights
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# INPUTS
# --------------------------------------------------
left, right = st.columns(2)

with left:
    engine_size = st.number_input("Engine Size (L)", 0.5, 10.0, step=0.1)
    cylinders = st.number_input("Cylinders", 1, 16)
    mileage = st.number_input("Vehicle Mileage (km)", 0, 500000, step=1000)
    vehicle_age = st.number_input("Vehicle Age (Years)", 0, 30)

with right:
    city_kmpl = st.number_input("Fuel City (km/l)", min_value=1.0, step=0.1)
    highway_kmpl = st.number_input("Fuel Highway (km/l)", min_value=1.0, step=0.1)

    valid_mileage = highway_kmpl > city_kmpl

    city_l_100 = 100 / city_kmpl
    highway_l_100 = 100 / highway_kmpl
    combined_l_100 = (city_l_100 + highway_l_100) / 2
    combined_kmpl = 100 / combined_l_100

    st.text_input(
        "Combined Mileage (km/l)",
        value=f"{combined_kmpl:.2f}",
        key="combined_display"
    )

    fuel_label = st.selectbox(
        "Fuel Type",
        ["Petrol", "Premium Petrol", "Diesel", "Ethanol / Flex Fuel", "Natural Gas (CNG)"]
    )

    fuel_map = {
        "Petrol": "X",
        "Premium Petrol": "Z",
        "Diesel": "D",
        "Ethanol / Flex Fuel": "E",
        "Natural Gas (CNG)": "N"
    }

    fuel_type = fuel_map[fuel_label]

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------
predict_clicked = st.button(
    "🚀 Predict CO₂ Emission",
    use_container_width=True,
    key="predict_co2_button"
)

# --------------------------------------------------
# EMISSION LEVEL LEGEND
# --------------------------------------------------
st.markdown(
    """
    <div style="display:flex; justify-content:center; gap:15px; margin:6px 0 0 0;">
        <div style="background-color:#2ecc71; color:white; padding:8px 15px; border-radius:8px; font-weight:600;">
            Low: &lt; 150 g/km
        </div>
        <div style="background-color:#f39c12; color:white; padding:8px 15px; border-radius:8px; font-weight:600;">
            Medium: 150 - 249 g/km
        </div>
        <div style="background-color:#e74c3c; color:white; padding:8px 15px; border-radius:8px; font-weight:600;">
            High: ≥ 250 g/km
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Scroll target (continuous scroll)
st.markdown('<div id="scroll-target"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# PREDICTION + AUTO SCROLL
# --------------------------------------------------
if predict_clicked:

    if not valid_mileage:
        st.error("Highway mileage must be greater than City mileage.")
    else:
        input_data = pd.DataFrame(
            [[engine_size, cylinders,
              city_l_100, highway_l_100, combined_l_100,
              fuel_type, vehicle_age, mileage]],
            columns=[
                'Engine Size(L)', 'Cylinders',
                'Fuel Consumption City (L/100 km)',
                'Fuel Consumption Hwy (L/100 km)',
                'Fuel Consumption Comb (L/100 km)',
                'Fuel Type', 'Vehicle Age', 'Mileage'
            ]
        )

        input_data = pd.get_dummies(input_data)
        input_data = input_data.reindex(columns=model_columns, fill_value=0)

        prediction = rf_model.predict(input_data)[0]

        emission_level = (
            "Low" if prediction < 150 else
            "Medium" if prediction < 250 else
            "High"
        )

        components.html(
            """
            <script>
                const el = window.parent.document.getElementById("scroll-target");
                if (el) {
                    el.scrollIntoView({ behavior: "smooth", block: "start" });
                }
            </script>
            """,
            height=0
        )

        # --------------------------------------------------
        # CENTERED + COLOR-CODED RESULT CARD
        # --------------------------------------------------
        if emission_level == "Low":
            bg, border, text = "#e8f8f5", "#2ecc71", "#1e8449"
        elif emission_level == "Medium":
            bg, border, text = "#fef5e7", "#f39c12", "#9c640c"
        else:
            bg, border, text = "#fdecea", "#e74c3c", "#922b21"

        st.markdown(
            f"""
            <div style="display:flex; justify-content:center; width:100%;">
                <div style="
                    background:{bg};
                    border-left:8px solid {border};
                    padding:16px 20px;
                    border-radius:10px;
                    margin-top:6px;
                    margin-bottom:8px;
                    width:520px;
                    max-width:90%;
                ">
                    <h3 style="margin:0; color:{text}; text-align:center;">
                        🚗 Predicted CO₂ Emission
                    </h3>
                    <p style="font-size:28px; font-weight:700; margin:6px 0; color:{text}; text-align:center;">
                        {prediction:.2f} g/km
                    </p>
                    <p style="font-size:18px; margin:0; color:{text}; text-align:center;">
                        Emission Level: <b>{emission_level}</b>
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

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
