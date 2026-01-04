import streamlit as st
import pandas as pd
import os
import re
from layout import base_layout

# PAGE CONFIG
st.set_page_config(
    page_title="Login | CleanDrive",
    page_icon="🌱",
    layout="wide"
)

# NAVBAR
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

# OPTIONAL CSS
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# CENTERED LOGIN FORM
left, center, right = st.columns([1, 2, 1])

with center:
    st.title("🔐 Login")

    username = st.text_input("Username (Name or Car Number)").strip().upper()
    password = st.text_input("Password", type="password").strip()

    car_pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
    name_pattern = r"^[A-Z ]{3,30}$"

    if st.button("Login"):

        if not username or not password:
            st.error("All fields are required")

        elif not (re.match(car_pattern, username) or re.match(name_pattern, username)):
            st.error("Enter a valid name or car number")

        else:
            users_file = os.path.join(os.getcwd(), "users.csv")

            if not os.path.exists(users_file):
                st.error("User database not found. Please register first.")
            else:
                df = pd.read_csv(users_file)

                df["username"] = df["username"].astype(str).str.strip().str.upper()
                df["password"] = df["password"].astype(str).str.strip()

                user = df[
                    (df["username"] == username) &
                    (df["password"] == password)
                ]

                if not user.empty:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful!")
                    st.switch_page("pages/app.py")
                else:
                    st.error("Invalid username or password")
