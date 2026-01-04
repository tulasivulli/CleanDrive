import streamlit as st
import random
from pathlib import Path  
 # ✅ added
import navbar
from layout import base_layout

# --------------------------------------------------
# PAGE CONFIG (ABSOLUTELY FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="Login | CleanDrive",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# BASE LAYOUT (NAVBAR COMES FROM HERE)
# --------------------------------------------------
base_layout()
# -----------------------------
# 🔐 Access Control
# -----------------------------
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login to access AI Assistant")
    st.switch_page("pages/login.py")

# -----------------------------
# Load external CSS (added)
# -----------------------------
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

with open("pages/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -----------------------------
# Demo AI Logic
# -----------------------------
import random

def contains_any(text, keywords):
    return any(word in text for word in keywords)

def demo_ai_response(question):
    q = question.lower()

    fuel_words = ["fuel", "petrol", "diesel", "gas", "octane"]
    emission_words = ["emission", "co2", "pollution", "smoke", "exhaust"]
    mileage_words = ["mileage", "average", "kmpl", "efficiency", "consumption"]
    maintenance_words = ["maintenance", "service", "servicing", "repair", "oil"]
    electric_words = ["electric", "ev", "hybrid", "battery"]

    fuel_responses = [
        """**Fuel Efficiency Guidance**
    • Use manufacturer-recommended fuel grade  
    • Avoid mixing fuel types  
    • Maintain steady driving speed  

    Proper fuel usage improves mileage and reduces CO₂ emissions.""",
        """**Why Fuel Choice Matters**
    • Correct fuel ensures proper combustion  
    • Prevents engine knocking  
    • Improves long-term engine health  

    Fuel quality directly impacts performance and efficiency.""",
        """**Fuel Consumption Reduction Tips**
    • Avoid aggressive acceleration  
    • Do not overload the vehicle  
    • Keep fuel system clean  

    These habits reduce unnecessary fuel wastage.""",
        """**Impact of Poor Fuel Usage**
    • Incomplete combustion  
    • Higher emissions  
    • Reduced mileage  

    Using correct fuel prevents engine inefficiency.""",
        """**Smart Fuel Practices**
    • Refuel from trusted stations  
    • Follow vehicle fuel recommendations  
    • Combine fuel efficiency with smooth driving  

    This helps lower running costs and emissions."""
    ]

    emission_responses = [
        """**Understanding CO₂ Emissions**
    • Engine size affects emission levels  
    • Aggressive driving increases pollution  
    • Poor maintenance worsens emissions  

    Smooth driving helps reduce environmental impact.""",
        """**Emission Control Tips**
    • Maintain emission systems regularly  
    • Avoid sudden braking and acceleration  
    • Reduce idle time in traffic  

    These steps help control pollution.""",
        """**Why Emissions Increase**
    • Faulty exhaust system  
    • Incorrect fuel usage  
    • Poor engine condition  

    Timely servicing reduces harmful emissions.""",
        """**Reducing Vehicle Pollution**
    • Plan routes to avoid congestion  
    • Maintain steady speeds  
    • Keep engine tuned  

    These practices lower carbon output.""",
        """**Environmental Impact Awareness**
    • High emissions affect air quality  
    • Vehicles contribute to climate change  
    • Cleaner driving protects health  

    Responsible driving reduces pollution."""
    ]

    mileage_responses = [
        """**Improving Vehicle Mileage**
    • Maintain correct tire pressure  
    • Drive at constant speed  
    • Reduce unnecessary vehicle load  

    Better mileage saves fuel and money.""",
        """**Low Mileage Causes**
    • Sudden acceleration  
    • Overloaded vehicle  
    • Poor maintenance  

    Fixing these improves fuel efficiency.""",
        """**Mileage Optimization Tips**
    • Use cruise control on highways  
    • Avoid frequent short trips  
    • Switch off engine during long stops  

    These habits improve average fuel economy.""",
        """**Fuel Economy Best Practices**
    • Gentle braking  
    • Proper gear shifting  
    • Regular servicing  

    Good driving habits lead to better mileage.""",
        """**Why Mileage Matters**
    • Reduces fuel costs  
    • Lowers emissions  
    • Improves vehicle lifespan  

    Efficient driving benefits both user and environment."""
    ]

    maintenance_responses = [
        """**Vehicle Maintenance Importance**
    • Regular servicing improves efficiency  
    • Oil changes reduce engine friction  
    • Air filter cleaning improves combustion  

    Maintenance lowers emissions and fuel usage.""",
        """**Benefits of Regular Servicing**
    • Better engine performance  
    • Improved fuel economy  
    • Reduced breakdown risk  

    Well-maintained vehicles pollute less.""",
        """**Essential Maintenance Checks**
    • Engine oil level  
    • Tire pressure  
    • Brake condition  

    Routine checks improve vehicle reliability.""",
        """**Impact of Poor Maintenance**
    • Increased fuel consumption  
    • Higher emissions  
    • Reduced engine life  

    Timely servicing prevents these issues.""",
        """**Smart Maintenance Habits**
    • Follow service schedule  
    • Fix issues early  
    • Use genuine spare parts  

    Maintenance ensures long-term efficiency."""
    ]

    electric_responses = [
        """**Electric & Hybrid Vehicles**
    • Very low or zero emissions  
    • Energy-efficient transportation  
    • Environment-friendly technology  

    They support sustainable mobility.""",
        """**Why Choose EVs**
    • Reduced fuel dependency  
    • Lower running costs  
    • Cleaner air  

    Electric vehicles are future-ready.""",
        """**Hybrid Vehicle Advantages**
    • Combines fuel and electric power  
    • Better fuel efficiency  
    • Lower emissions  

    Hybrids are a practical eco-option.""",
        """**Environmental Benefits of EVs**
    • No tailpipe emissions  
    • Reduced noise pollution  
    • Lower carbon footprint  

    EVs help fight climate change.""",
        """**Transition to Electric Mobility**
    • Government incentives available  
    • Growing charging infrastructure  
    • Sustainable transportation future  

    EV adoption supports clean energy goals."""
    ]

    if contains_any(q, fuel_words):
        return random.choice(fuel_responses)
    if contains_any(q, mileage_words):
        return random.choice(mileage_responses)
    if contains_any(q, emission_words):
        return random.choice(emission_responses)
    if contains_any(q, maintenance_words):
        return random.choice(maintenance_responses)
    if contains_any(q, electric_words):
        return random.choice(electric_responses)

    return (
        "**Eco-Friendly Driving Advice**\n"
        "• Drive smoothly and avoid harsh braking\n"
        "• Maintain your vehicle regularly\n"
        "• Reduce unnecessary fuel usage\n\n"
        "These practices improve efficiency and reduce environmental impact."
    )

# -----------------------------
# 🧠 Initialize Chat History
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Display Chat History
# -----------------------------
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**AI:** {chat['answer']}")
    st.markdown("---")

# -----------------------------
# Input Form (Enter = Send)
# -----------------------------
with st.form(key="chat_form", clear_on_submit=True):
    question = st.text_input(
        "Eco-Driving Advisory Assistant",
        placeholder="Ask for eco-driving advice, fuel efficiency tips, or emission reduction guidance…"
    )
    send = st.form_submit_button("Send")

if send and question.strip():
    answer = demo_ai_response(question)
    st.session_state.chat_history.append({
        "question": question,
        "answer": answer
    })
    st.rerun()

