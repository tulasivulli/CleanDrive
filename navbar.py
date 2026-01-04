import streamlit as st

def navbar():
    # ---------- CSS for navbar buttons ----------
    st.markdown("""
        <style>
        /* Only navbar buttons look like text links */
        .nav-btn div[data-testid="stButton"] > button {
            background: none !important;
            border: none !important;
            padding: 0 !important;
            margin: 0 !important;
            font-size: 15px;
            font-weight: 700;
            color: #e5e7eb;
            cursor: pointer;
            line-height: 1.2;
        }

        .nav-btn div[data-testid="stButton"] > button:hover {
            color: #22c55e;
            text-decoration: underline;
        }

        .nav-btn div[data-testid="stButton"] > button:focus {
            outline: none;
            box-shadow: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # ---------- Navbar items ----------
    pages = {
        "Home": "welcome.py",
        "App": "pages/app.py",
        "Eco-Advisor": "pages/advisor.py",
        "Logout": "logout"
    }

    # Columns for logo + navbar buttons
    cols = st.columns([4.5, 0.4, 0.4, 0.6, 0.7], gap="small")

    # Logo & Title
    with cols[0]:
        st.markdown(
            "<span style='font-size:26px; margin-right:6px;'>🌱</span>"
            "<span style='font-size:22px; font-weight:800; background: linear-gradient(90deg,#22c55e,#16a34a); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>CleanDrive</span>",
            unsafe_allow_html=True
        )

    # Navbar buttons (styled as text)
    for i, (label, path) in enumerate(pages.items()):
        with cols[i + 1]:
            st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
            if st.button(label, key=f"nav_{label}"):
                if path == "logout":
                    st.session_state.show_logout_dialog = True  # trigger dialog
                else:
                    st.switch_page(path)
            st.markdown('</div>', unsafe_allow_html=True)

    # ---------- Logout Confirmation Dialog ----------
    if st.session_state.get("show_logout_dialog", False):
        @st.dialog("Logout Confirmation")
        def logout_dialog():
            st.write("Are you sure you want to logout?")

            c1, c2 = st.columns(2)

            with c1:
                if st.button("Cancel"):
                    st.session_state.show_logout_dialog = False
                    st.rerun()

            with c2:
                if st.button("Logout"):
                    st.session_state.clear()
                    st.switch_page("welcome.py")

        logout_dialog()

