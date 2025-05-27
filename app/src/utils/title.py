import streamlit as st


def title(title: str, subtitle: str):

    st.markdown(
        f"""
        <div style=padding: 10px 0;'>
            <h1 style='color: white; font-size: 42px; text-align: center;'>{title}</h1>
            <p style='color: white; font-size: 18px;text-align: center;'>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
