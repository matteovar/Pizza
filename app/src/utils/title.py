import streamlit as st

def title(title:str):
    """
    Function to set the title of the Streamlit app.
    
    Parameters:
    title (str): The title to be displayed in the app.
    """
    st.markdown(
        f"""
        <style>
            .stTitle {{
                color: white;
                font-size: 24px;
                text-align: center;
            }}
        </style>
        <h1 class="stTitle">{title}</h1>
        """,
        unsafe_allow_html=True,
    )