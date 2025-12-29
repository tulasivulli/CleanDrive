import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Register | CleanDrive", layout="centered")

st.title("📝 Register")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm = st.text_input("Confirm Password", type="password")

if st.button("Create Account"):
    if not username or not password:
        st.error("All fields are required")
    elif password != confirm:
        st.error("Passwords do not match")
    else:
        if os.path.exists("users.csv"):
            df = pd.read_csv("users.csv")
        else:
            df = pd.DataFrame(columns=["username", "password"])

        if username in df["username"].values:
            st.error("Username already exists")
        else:
            df.loc[len(df)] = [username, password]
            df.to_csv("users.csv", index=False)
            st.success("Account created successfully!")
            st.info("You can now log in")
