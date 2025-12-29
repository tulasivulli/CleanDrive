import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Login | CleanDrive", layout="centered")

st.title("🔐 Login")

username = st.text_input("Username").strip()
password = st.text_input("Password", type="password").strip()

if st.button("Login"):
    users_file = os.path.join(os.getcwd(), "users.csv")

    if not os.path.exists(users_file):
        st.error("User database not found. Please register first.")
    else:
        df = pd.read_csv(users_file)

        # Normalize for safety
        df["username"] = df["username"].astype(str).str.strip()
        df["password"] = df["password"].astype(str).str.strip()

        user = df[
            (df["username"].str.lower() == username.lower()) &
            (df["password"] == password)
        ]

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login successful! Redirecting...")
            st.switch_page("pages/app.py")
        else:
            st.error("Invalid username or password")
