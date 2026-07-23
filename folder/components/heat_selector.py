import streamlit as st
import pandas as pd

def heat_selector(df):

    st.subheader("🔥 Heat Selection")

    c1, c2 = st.columns([3,1])

    with c1:

        heat = st.selectbox(
            "Select Heat",
            df.index,
            format_func=lambda x: f"H{x+1:05d}"
        )

    with c2:

        st.write("")
        st.write("")

        if st.button("⟳ Refresh"):
            st.rerun()

    return df.iloc[heat]