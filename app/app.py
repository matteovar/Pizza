import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.page1 import visual as show_visual

st.set_page_config(page_title="Sales App", layout="wide")


def main():
    with st.sidebar:
        # CSS ajustado para centralização perfeita
        st.markdown(
            """
            <style>
                .st-emotion-cache-8atqhb.e1mlolmg0 {
                    display: flex !important;
                    flex-direction: column !important;
                    justify-content: center !important;
                    height: 100%    !important;
                    padding-top: 2% !important;
                    padding-bottom: 0 !important;
                }
                /* Ajuste para o container do menu */
                .st-emotion-cache-8atqhb.e1mlolmg0 > div {
                    width: 100% !important;
                    margin-top: 0 !important;
                    margin-bottom: 0 !important;
                }
                
                /* Ajuste para a lista de itens */
                .st-emotion-cache-8atqhb.e1mlolmg0 ul {
                    padding: 0 !important;
                    margin: 0 !important;
                    
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title=None,
            options=[
                "General Informations",
            ],
            icons=["info-circle", "bar-chart-line", "gift", "people"],
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#031e57",
                    "height": "100%",
                },
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0",
                    "padding": "10px 5px",
                },
            },
        )

    # Navegação para cada página
    if selected == "General Informations":
        show_visual()


if __name__ == "__main__":
    main()