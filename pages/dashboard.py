import streamlit as st

st.set_page_config(page_title="Dashboard | CleanDrive", layout="wide")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first")
    st.switch_page("pages/login.py")

st.title(f"👋 Welcome, {st.session_state.username}")

st.success("You are now logged in to CleanDrive")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("welcome.py")
