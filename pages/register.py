import streamlit as st
import pandas as pd
import os
import re
from layout import base_layout

# MUST BE FIRST
st.set_page_config(
    page_title="Register | CleanDrive",
    page_icon="🌱",
    layout="wide"
)

# ALWAYS RENDER NAVBAR
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

# CENTER FORM
left, center, right = st.columns([1, 2, 1])

with center:
    st.title("📝 Register")

    # Username (Name or Car Number)
    username = st.text_input("Username (Name or Car Number)").strip().upper()
    password = st.text_input("Password", type="password").strip()
    confirm = st.text_input("Confirm Password", type="password").strip()

    car_pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
    name_pattern = r"^[A-Z ]{3,30}$"

    if st.button("Create Account"):

        if not username or not password or not confirm:
            st.error("All fields are required")

        elif not (re.match(car_pattern, username) or re.match(name_pattern, username)):
            st.error("Username must be a valid name or car number (e.g., AP09AB1234)")

        elif password != confirm:
            st.error("Passwords do not match")

        else:
            if os.path.exists("users.csv"):
                df = pd.read_csv("users.csv")
                df["username"] = df["username"].astype(str).str.strip().str.upper()
            else:
                df = pd.DataFrame(columns=["username", "password"])

            if username in df["username"].values:
                st.error("Username already registered")
            else:
                df.loc[len(df)] = [username, password]
                df.to_csv("users.csv", index=False)
                st.success("Account created successfully!")
                st.info("You can now log in")
