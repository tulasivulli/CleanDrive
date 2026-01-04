import streamlit as st
from navbar import navbar

def base_layout():

    # 🔧 REMOVE STREAMLIT TOP GAP (GLOBAL)
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 0rem !important;
        }

        header {
            visibility: hidden;
            height: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 🔝 NAVBAR AT VERY TOP
    navbar()
