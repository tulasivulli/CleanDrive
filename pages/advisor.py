import warnings
warnings.filterwarnings("ignore")

import streamlit as st
from layout import base_layout

# --------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="CleanDrive | Eco Advisor",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# NAVBAR + SIDEBAR HIDE (SAME AS OTHER PAGES)
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
# ACCESS CONTROL (SAME LOGIC)
# --------------------------------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to access the Eco Advisor")
    st.switch_page("pages/login.py")

# --------------------------------------------------
# LOAD GLOBAL CSS (SAME FILE)
# --------------------------------------------------
with open("pages/style.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:40px;">
        <h1>Eco Advisor</h1>
        <p style="color:#9ca3af; font-size:16px;">
            Driving advices to reduce CO₂ emissions and protect the environment
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# ECO ADVISOR – 10 GUIDANCE BOXES
# --------------------------------------------------

st.markdown("""
<style>
.advisor-card {
    background-color: #ecfdf5;
    padding: 24px;
    border-radius: 16px;
    border-left: 8px solid #22c55e;
    border: 1.5px solid #22c55e;
    box-shadow: 0px 6px 14px rgba(0,0,0,0.15);
    margin-bottom: 28px;
    transition: all 0.3s ease-in-out;
}
.advisor-card:hover {
    transform: scale(1.04);
    box-shadow: 0px 14px 32px rgba(34,197,94,0.45);
    background-color: #d1fae5;
}
.advisor-card h3 {
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

boxes = [
    ("🌍 Why Reducing CO₂ Emissions Matters", [
        "CO₂ emissions are a major cause of global warming",
        "Vehicle emissions significantly impact air quality",
        "Increased pollution leads to serious health problems",
        "Lower emissions help protect ecosystems and wildlife",
        "Fuel-efficient driving reduces carbon footprint",
        "Reduced emissions support climate sustainability goals",
        "Responsible driving improves quality of life",
        "Small individual actions create large environmental impact",
    ]),

    ("🚗 Smart Driving Habits", [
        "Maintain steady vehicle speed",
        "Avoid sudden acceleration",
        "Reduce harsh braking",
        "Drive within speed limits",
        "Anticipate traffic movement",
        "Avoid aggressive driving",
        "Follow lane discipline",
        "Reduce unnecessary idling"
    ]),

    ("🛠 Vehicle Maintenance Practices", [
        "Service vehicle regularly",
        "Maintain correct tyre pressure",
        "Replace air filters on time",
        "Use recommended engine oil",
        "Fix engine issues promptly",
        "Maintain wheel alignment",
        "Monitor dashboard warnings",
        "Keep fuel system clean"
    ]),

    ("⛽ Fuel Efficiency Tips", [
        "Use fuel-efficient driving modes",
        "Avoid driving with low fuel",
        "Choose correct fuel type",
        "Drive at optimal speeds",
        "Avoid fuel leakage",
        "Track fuel consumption",
        "Reduce fuel wastage",
        "Maintain consistent mileage"
    ]),

    ("⚙️ Engine & Emission Control", [
        "Maintain proper engine tuning",
        "Avoid engine overheating",
        "Check oxygen sensors regularly",
        "Maintain catalytic converter",
        "Avoid excessive engine revving",
        "Use clean fuel",
        "Follow emission regulations",
        "Fix exhaust issues immediately"
    ]),

    ("🗺 Route Planning & Traffic Management", [
        "Avoid peak-hour traffic",
        "Plan trips in advance",
        "Use navigation apps",
        "Select less congested routes",
        "Avoid short cold-engine trips",
        "Reduce stop-and-go driving",
        "Combine multiple trips",
        "Prefer smooth traffic roads"
    ]),

    ("📦 Load & Vehicle Usage", [
        "Avoid unnecessary overloading",
        "Remove unused roof racks",
        "Reduce excess luggage",
        "Avoid towing when not needed",
        "Balance vehicle load properly",
        "Follow manufacturer load limits",
        "Use vehicle appropriate to need",
        "Remove unused accessories"
    ]),

    ("🚶 Alternative Transportation Choices", [
        "Use public transport when possible",
        "Practice carpooling",
        "Walk for short distances",
        "Use bicycles for nearby travel",
        "Opt for hybrid or electric vehicles",
        "Reduce single-passenger trips",
        "Use ride-sharing services",
        "Support sustainable mobility"
    ]),

    ("🌍 Environmental Awareness", [
        "CO₂ causes global warming",
        "Vehicle emissions harm air quality",
        "Small actions reduce pollution",
        "Fuel efficiency lowers emissions",
        "Cleaner driving protects ecosystems",
        "Reduced pollution improves health",
        "Individual efforts matter",
        "Sustainability starts with drivers"
    ]),

    ("📊 How CleanDrive Helps", [
        "Predicts CO₂ emissions using ML",
        "Shows emission levels clearly",
        "Encourages eco-conscious decisions",
        "Combines prediction with awareness",
        "Acts as a green driving assistant",
        "Supports emission reduction goals",
        "Improves user driving behavior",
        "Promotes a cleaner future"
    ])
]

# --------------------------------------------------
# DISPLAY BOXES IN 2-COLUMN GRID
# --------------------------------------------------

for i in range(0, len(boxes), 2):
    col1, col2 = st.columns(2)

    # First box
    with col1:
        title, points = boxes[i]
        st.markdown(
            f"""
            <div class="advisor-card">
                <h3>{title}</h3>
                <ul>
                    {''.join([f"<li>{p}</li>" for p in points])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Second box (check exists)
    if i + 1 < len(boxes):
        with col2:
            title, points = boxes[i + 1]
            st.markdown(
                f"""
                <div class="advisor-card">
                    <h3>{title}</h3>
                    <ul>
                        {''.join([f"<li>{p}</li>" for p in points])}
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
