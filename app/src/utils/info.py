import streamlit as st


def info(info: str):
    st.markdown(
        f"""
        <div class="container">
            <div class="delay-info">
                <span class="delay-time">{info}</span>
            </div>
        </div>

        <style>
            .container {{
                display: flex;
                justify-content: center;  /* centraliza horizontalmente */
                margin-top: 50px;
                margin-bottom: 50px;
            }}
            .delay-info {{
                display: inline-block;
                font-size: 22px;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #fff;
                text-align: center;
                border: 1px solid #373739;
                border-radius: 10px;
                padding: 10px 20px;
                background-color: #070707;
            }}
            .delay-time {{
                font-weight: bold;
                color: #e74c3c;
            }}
            .time {{
                font-size: 24px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
